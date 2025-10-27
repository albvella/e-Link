import socket
import threading
from fastcrc import crc32 as crc
import base64
from datetime import datetime
import queue
import time

class eLinkTCPServer:
    """
    Server TCP per la gestione di dispositivi e-Link.
    Gestisce connessioni multiple, invio comandi, ricezione misure, OTA e code di messaggi.
    """
    def __init__(self, host='0.0.0.0', port=21001, handler=None):
        """
        Inizializza il server TCP.

        Args:
            host (str): Indirizzo host su cui ascoltare.
            port (int): Porta su cui ascoltare.
            handler (callable, optional): Funzione di callback per processare i dati ricevuti.
        """
        self.host = host
        self.port = port
        self.handler = handler  # function to process received data
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.running = False
        self.threads = []
        self.clients = {}  # addr -> socket
        self.device_clients = {}  # device_id -> addr
        self.client_log_queues = {}
        self.client_reply_queues = {} 
        self.client_meas_queues = {}
        self.allowed_commands = ["IDL", "SRT", "PNG", "SND,1", "SND,0", "MSR", "OTA", "SET", "GET", "RST"]
        self.allowed_vars = ["DEVICE_ID", "SAMP_FREQ", "BUFFER_SECS", "CONN_TIMEOUT", "LOG_PERIOD", "HAMMER_TH", "HIGH_TH", "LOW_TH", "TCP_IP", "TCP_PORT"]

    def start(self):
        """
        Avvia il server TCP e inizia ad accettare connessioni.
        """
        self.running = True
        print(f"TCP Server listening on {self.host}:{self.port}")
        threading.Thread(target=self._accept_loop, daemon=True).start()

    def stop(self):
        """
        Ferma il server TCP, chiude tutte le connessioni e pulisce le code.
        """
        self.running = False
        for addr, queue in self.client_log_queues.items():
            queue.queue.clear()
        for addr, queue in self.client_reply_queues.items():
            queue.queue.clear()
        for addr, queue in self.client_meas_queues.items():
            queue.queue.clear()
        for addr, sock in self.clients.items():
            sock.close()
        self.clients.clear()
        self.device_clients.clear()
        self.client_log_queues.clear()
        self.client_reply_queues.clear()
        self.client_meas_queues.clear()
        self.server_socket.close()
        print("TCP Server stopped")


    def send_command(self, client_sock, command, cfg_var=None, cfg_idx=None, cfg_val=None):
        """
        Invia un comando al client tramite socket TCP.

        Args:
            client_sock (socket.socket): Socket del client.
            command (str): Comando da inviare (deve essere tra quelli consentiti).
            cfg_var (str, optional): Variabile di configurazione.
            cfg_idx (int, optional): Indice di configurazione.
            cfg_val (str/int, optional): Valore di configurazione.

        Returns:
            None
        """
        def worker():
            if command not in self.allowed_commands:
                print(f"Command not allowed: {command}")
                print(f"Allowed commands: {self.allowed_commands}")
                return False
            if cfg_var is not None and cfg_var not in self.allowed_vars:
                print(f"Configuration variable not allowed: {cfg_var}")
                print(f"Allowed variables: {self.allowed_vars}")
                return False
            if cfg_var is not None and cfg_idx is not None and cfg_val is not None:
                payload = f"+CMD,{command},{cfg_var},{cfg_idx},{cfg_val}"
            else:
                if command != "SET" and command != "GET":
                    payload = f"+CMD,{command}"
                    if command == "SND" and cfg_var is not None:
                        payload += f",{cfg_var}"
                else:
                    print(f"SET and GET commands require cfg_var and cfg_val (and cfg_idx for SET).")
                    return False

            try:
                client_sock.sendall(payload.encode())
            except Exception as e:
                print(f"Error sending command: {e}")
        t = threading.Thread(target=worker, daemon=True)
        t.start()


    def receive_measure(self, client_sock, filename=None):
        """
        Riceve dati di misura dal client e li salva su file.
        Usa lunghezza minima per rilevare messaggi completi.

        Args:
            client_sock (socket.socket): Socket del client.
            filename (str, optional): Nome del file di destinazione.

        Returns:
            threading.Thread: Thread worker che gestisce la ricezione.
        """
        if filename is None:
            filename = datetime.now().strftime("%y%m%d_%H%M_comp.bin")

        def worker():
            with open(filename, "ab") as f:
                # ✅ BUFFER PER RICOSTRUIRE MESSAGGI FRAMMENTATI
                message_buffer = b""
                min_expected_length = 1380  # ✅ LUNGHEZZA MINIMA per messaggio completo
                
                while True:
                    try:
                        try:
                            # Ricevi chunk dal queue
                            chunk = self.client_meas_queues[client_sock.getpeername()].get(timeout=10)
                        except queue.Empty:
                            print("Receive Timeout!")
                            break
                        
                        if not chunk:
                            break
                        
                        # ✅ ACCUMULA I CHUNK NEL BUFFER
                        message_buffer += chunk
                        print(f"Received chunk: {len(chunk)} bytes, buffer total: {len(message_buffer)} bytes")
                        
                        # ✅ CONTROLLA SE ABBIAMO RAGGIUNTO LA LUNGHEZZA MINIMA
                        if len(message_buffer) >= min_expected_length:
                            try:
                                # ✅ PROCESSA IL BUFFER COME MESSAGGIO COMPLETO
                                print(f"Processing complete message: {len(message_buffer)} bytes")
                                
                                # ✅ DECODE BASE64 DEL MESSAGGIO COMPLETO
                                bin_data = base64.b64decode(message_buffer)
                                f.write(bin_data)
                                print(f"Decoded and saved: {len(bin_data)} bytes")
                                
                                # ✅ RESET DEL BUFFER PER IL PROSSIMO MESSAGGIO
                                message_buffer = b""
                                
                            except Exception as e:
                                print(f"Base64 decode error: {e}")
                                print(f"Message preview: {message_buffer[:50]}...")
                                
                                # ✅ FALLBACK: cerca inizio valido nel buffer
                                # Trova il prossimo carattere Base64 valido
                                valid_start = 0
                                for i in range(len(message_buffer)):
                                    test_char = message_buffer[i:i+1]
                                    if test_char.isalnum() or test_char in b'+/=':
                                        valid_start = i
                                        break
                                
                                if valid_start > 0:
                                    message_buffer = message_buffer[valid_start:]
                                    print(f"Skipped {valid_start} invalid bytes")
                                else:
                                    # Se non trova caratteri validi, scarta tutto
                                    message_buffer = b""
                                
                    except Exception as e:
                        print(f"Socket error: {e}")
                        break
                        
            print(f"Saved received measure to {filename}")

        t = threading.Thread(target=worker, daemon=True)
        t.start()
        return t


    def send_OTA(self, client_sock, filename, chunk_size=1024):
        """
        Invia un file al client per aggiornamento OTA, con conferma ACK per ogni chunk.

        Args:
            client_sock (socket.socket): Socket del client.
            filename (str): Nome del file da inviare.
            chunk_size (int, optional): Dimensione dei chunk inviati.

        Returns:
            bytes or None: Risposta finale del client, None in caso di errore.
        """
        try:
            with open(filename, "rb") as f:
                while True:
                    bin_chunk = f.read(chunk_size)
                    if not bin_chunk:
                        break
                    chunk = base64.b64encode(bin_chunk) 
                    client_sock.sendall(chunk)
                    try:
                        ack = self.client_reply_queues[client_sock.getpeername()].get(timeout=5)  # attende l'ACK dal client 
                    except queue.Empty:
                        print("ACK timeout!")
                        return None
                    if ack.strip() != b'ACK':
                        print("ACK not received!")
                        return None
            client_sock.sendall("EOF".encode())
            reply = self.client_reply_queues[client_sock.getpeername()].get(timeout=5)
            print(f"File {filename} sent to client.")
            return reply
        except Exception as e:
            print(f"Error sending file: {e}")
            return None


    def send_crc32(self, client_sock, filename):
        """
        Calcola e invia il CRC32 del file al client per verifica integrità.

        Args:
            client_sock (socket.socket): Socket del client.
            filename (str): Nome del file da verificare.

        Returns:
            bytes or None: Risposta del client, None in caso di errore.
        """
        crc_var = 0xFFFFFFFF
        try:
            with open(filename, "rb") as f:
                while True:
                    chunk = f.read(4096)
                    if not chunk:
                        break
                    crc_var = crc.jamcrc(chunk, initial=crc_var)
            crc_bytes = crc_var.to_bytes(4, 'big')
            crc_enc = base64.b64encode(crc_bytes)
            client_sock.sendall(crc_enc)
            print(f"CRC32 ({crc_var:#010x}) sent for {filename}.")
            reply = self.client_reply_queues[client_sock.getpeername()].get(timeout=5)
            return reply
        except Exception as e:
            print(f"Error sending CRC32: {e}")
            return None


    def OTA_routine(self, client_sock, filename):
        """
        Esegue la routine completa di aggiornamento OTA: invio comando, file, CRC e verifica.

        Args:
            client_sock (socket.socket): Socket del client.
            filename (str): Nome del file da inviare.

        Returns:
            None
        """
        self.send_command(client_sock, "OTA", buffer_size=16)
        ret = self.client_reply_queues[client_sock.getpeername()].get(timeout=5)
        if ret is None or ret.decode() != "OTA_READY":
            print("Client not ready for OTA.")
            return
        ret = self.send_OTA(client_sock, filename)
        if ret is None or ret.decode() != "OTA_RECEIVED":
            print("Client did not confirm OTA receipt.")
            return
        ret = self.send_crc32(client_sock, filename)
        if ret is None or ret.decode() != "OTA_CRC_OK":
            print("Client reported CRC error.")
            return
        ret = self.client_reply_queues[client_sock.getpeername()].get(timeout=5)
        if ret is not None and ret.decode() == "OTA_SUCCESS":
            print("OTA completed successfully.")
        else:
            print(ret)
            print("OTA failed.")
        return


    def OTA(self, client_sock, filename):
        """
        Avvia la routine OTA in un thread separato.

        Args:
            client_sock (socket.socket): Socket del client.
            filename (str): Nome del file da inviare.

        Returns:
            threading.Thread: Thread worker OTA.
        """
        def worker():
            self.OTA_routine(client_sock, filename)
        t = threading.Thread(target=worker, daemon=True)
        t.start()
        return t

    def _extract_device_id_from_log(self, data, addr):
        """
        Estrae il device_id dai messaggi di log e lo associa all'indirizzo.
        
        Args:
            data (bytes): Dati del messaggio di log.
            addr (tuple): Indirizzo del client.
        """
        try:
            parts = data.decode().split(b",") if isinstance(data, bytes) else data.split(",")
            if len(parts) > 0:
                device_id = int(parts[0])
                if addr not in self.device_clients.values():
                    self.device_clients[device_id] = addr
                    print(f"Device ID {device_id} associated with {addr}")
                    print(f"Device List: {list(self.device_clients.keys())}")
        except Exception as e:
            pass  # Non tutti i messaggi di log contengono device_id

    def _extract_device_id_from_reply(self, data, addr):
        """
        Estrae il device_id dalle risposte e lo associa all'indirizzo.
        
        Args:
            data (bytes): Dati della risposta.
            addr (tuple): Indirizzo del client.
        """
        try:
            if len(data) > 10:  # Risposta completa con info dispositivo
                parts = data.decode().split(",") if isinstance(data, bytes) else data.split(",")
                if len(parts) > 0:
                    device_id = int(parts[0])
                    if addr not in self.device_clients.values():
                        self.device_clients[device_id] = addr
                        print(f"Device ID {device_id} associated with {addr}")
                        print(f"Device List: {list(self.device_clients.keys())}")
        except Exception as e:
            pass  # Non tutte le risposte contengono device_id

    def _disconnect_client(self, addr):
        """
        Disconnette un client e pulisce tutte le strutture dati associate.
        
        Args:
            addr (tuple): Indirizzo del client da disconnettere.
        """
        # Rimuovi device_id dal mapping
        device_id_to_remove = None
        for device_id, client_addr in self.device_clients.items():
            if client_addr == addr:
                device_id_to_remove = device_id
                break
        
        if device_id_to_remove is not None:
            del self.device_clients[device_id_to_remove]
            print(f"Device ID {device_id_to_remove} disconnected")
        
        # Pulisci le code e i dizionari
        if addr in self.client_reply_queues:
            self.client_reply_queues[addr].queue.clear()
            del self.client_reply_queues[addr]
        if addr in self.client_log_queues:
            self.client_log_queues[addr].queue.clear()
            del self.client_log_queues[addr]
        if addr in self.client_meas_queues:
            self.client_meas_queues[addr].queue.clear()
            del self.client_meas_queues[addr]
        if addr in self.clients:
            del self.clients[addr]

    def get_client_by_device_id(self, device_id):
        """
        Ottiene il socket del client tramite device_id.
        
        Args:
            device_id (int): ID del dispositivo.
            
        Returns:
            socket.socket or None: Socket del client o None se non trovato.
        """
        addr = self.device_clients.get(device_id)
        if addr:
            return self.clients.get(addr)
        return None

    def send_command_to_device(self, device_id, command, cfg_var=None, cfg_idx=None, cfg_val=None):
        """
        Invia un comando a un dispositivo specifico tramite device_id.
        
        Args:
            device_id (int): ID del dispositivo.
            command (str): Comando da inviare.
            cfg_var (str, optional): Variabile di configurazione.
            cfg_idx (int, optional): Indice di configurazione.
            cfg_val (str/int, optional): Valore di configurazione.
            
        Returns:
            bool: True se il comando è stato inviato, False altrimenti.
        """
        if device_id == 0:                             # broadcast a tutti i dispositivi
            for dev_id in self.device_clients.keys():
                client_sock = self.get_client_by_device_id(dev_id)
                if client_sock:
                    self.send_command(client_sock, command, cfg_var, cfg_idx, cfg_val)
            return True
        
        client_sock = self.get_client_by_device_id(device_id)
        if client_sock:
            self.send_command(client_sock, command, cfg_var, cfg_idx, cfg_val)
            return True
        else:
            print(f"Device ID {device_id} not found")
            return False

    def get_connected_devices(self):
        """
        Restituisce la lista dei device_id connessi.
        
        Returns:
            list: Lista degli ID dei dispositivi connessi.
        """
        return list(self.device_clients.keys())

    def _request_device_id(self, client_sock, addr):
        """
        Richiede il device_id al client appena connesso e lo associa all'indirizzo.
        
        Args:
            client_sock (socket.socket): Socket del client.
            addr (tuple): Indirizzo del client.
        """
        try:
            # Invia comando PNG per ottenere le info del dispositivo
            payload = "+CMD,PNG"
            client_sock.sendall(payload.encode())
            
            # Avvia un timer per gestire il timeout della risposta
            def timeout_handler():
                import time
                time.sleep(10)  # 10 secondi di timeout
                if addr not in self.device_clients.values():
                    print(f"Device ID timeout for {addr}, disconnecting...")
                    self._disconnect_client(addr)
            
            threading.Thread(target=timeout_handler, daemon=True).start()
            
        except Exception as e:
            print(f"Error requesting device ID from {addr}: {e}")
            self._disconnect_client(addr)


    def _accept_loop(self):
        """
        Loop principale per accettare nuove connessioni client.
        """
        while self.running:
            try:
                client_sock, addr = self.server_socket.accept()
                self.clients[addr] = client_sock
                self.client_reply_queues[addr] = queue.Queue()
                self.client_log_queues[addr] = queue.Queue()
                self.client_meas_queues[addr] = queue.Queue()
                print(f"Connection from {addr}")
                
                time.sleep(0.5)
                self._request_device_id(client_sock, addr)
                
                t = threading.Thread(target=self._client_thread, args=(client_sock, addr), daemon=True)
                t.start()
                self.threads.append(t)
            except Exception as e:
                print(f"Accept error: {e}")


    def _client_thread(self, client_sock, addr):
        """
        Gestisce la comunicazione con un singolo client: ricezione dati e smistamento nelle code.

        Args:
            client_sock (socket.socket): Socket del client.
            addr (tuple): Indirizzo del client.

        Returns:
            None
        """
        client_sock.settimeout(180.0)      # Timeout di 3 minuti
        with client_sock:
            while True:
                try:
                    data = client_sock.recv(4096)
                    if not data:
                        print(f"Connection closed by {addr}")
                        self._disconnect_client(addr)
                        break

                    if data.startswith(b'L:'):
                        data_content = data[2:]
                        self.client_log_queues[addr].put(data_content)
                        self._extract_device_id_from_log(data_content, addr)
                    elif data.startswith(b'R:'):
                        data_content = data[2:]
                        self.client_reply_queues[addr].put(data_content)
                        self._extract_device_id_from_reply(data_content, addr)
                    elif data.startswith(b'H:'):
                        pass
                    elif len(data) > 100:
                        self.client_meas_queues[addr].put(data)
                    else:
                        print(f"Unknown data from {addr}: {data}")

                    if self.handler:
                        self.handler(data)

                except socket.timeout:
                    print(f"Timeout from {addr}, checking connection...")
                    try:
                        client_sock.send(b'')  # Ping test 
                    except:
                        print(f"Client {addr} disconnected (timeout)")
                        self._disconnect_client(addr)
                        break

                except Exception as e:
                    print(f"Client error {addr}: {e}")
                    break

    



def rx_handler(data):
    clock_freq = 80000000
    press_FS = 50
    
    msg = {}
    if(data.startswith(b'L:')):
        try:
            data_str = data[2:].decode('utf-8').strip()  
            parts = data_str.split(",")
            msg = {
                "ID" : int(parts[0]),
                "Press [bar]": f"{int(parts[1]) * press_FS / 4096:.4f}",
                "FLow [L/s]": f"{((clock_freq / int(parts[2])) if int(parts[2]) != 0 else 0):.4f}",
                "ax [mg]": f"{(int(parts[3]) - 65536 if int(parts[3]) > 32767 else int(parts[3])) * 0.061:.4f}",
                "ay [mg]": f"{(int(parts[4]) - 65536 if int(parts[4]) > 32767 else int(parts[4])) * 0.061:.4f}",
                "az [mg]": f"{(int(parts[5]) - 65536 if int(parts[5]) > 32767 else int(parts[5])) * 0.061:.4f}",
                "Vbatt [V]": f"{int(parts[6]) * 0.001:.4f}",
                "I1 [A]": f"{(((int(parts[7]) >>3) if int(parts[7]) < 0x8000 else (int(parts[7]) - 0x10000) >>3) * 0.00004 / 0.08):.4f}",
                "I2 [A]": f"{(((int(parts[8]) >>3) if int(parts[8]) < 0x8000 else (int(parts[8]) - 0x10000) >>3) * 0.00004 / 0.08):.4f}",
                "I3 [A]": f"{(((int(parts[9]) >>3) if int(parts[9]) < 0x8000 else (int(parts[9]) - 0x10000) >>3) * 0.00004 / 0.08):.4f}",
                "V1 [V]": f"{int(parts[10]) * 0.001:.4f}",
                "V2 [V]": f"{int(parts[11]) * 0.001:.4f}",
                "V3 [V]": f"{int(parts[12]) * 0.001:.4f}",
                "Temp [°C]": f"{(int(parts[13]) * 0.0625 if int(parts[13]) < 0x8000 else (int(parts[13]) - 0x10000) * 0.0625):.4f}"
            }
        except Exception as e:
            print(f"Data parse error: {e}")

    elif(data.startswith(b'R:')):
        try:
            data_str = data[2:].decode('utf-8').strip()  
            parts = data_str.split(",")
            
            # Check if this looks like a full info response (many comma-separated values)
            if len(parts) >= 17:
                try:
                    msg = {
                        "ID": int(parts[0]),
                        "Firmware Version": round(float("{}.{}".format(int(parts[1]) >> 8, int(parts[1]) & 0xFF)), 4),
                        "Uptime": datetime(year=int(parts[2]), month=int(parts[3]), day=int(parts[4]), hour=int(parts[5]), minute=int(parts[6]), second=int(parts[7])),
                        "Vbatt [V]": f"{int(parts[8]) * 0.001:.4f}",
                        "Sampling Freq [Hz]": int(parts[9]),
                        "Buffering [s]": int(parts[10]),
                        "V1 [V]":f"{int(parts[11]) * 0.001:.4f}",
                        "V2 [V]": f"{int(parts[12]) * 0.001:.4f}",
                        "V3 [V]": f"{int(parts[13]) * 0.001:.4f}",
                        "I1 [A]": f"{((((int(parts[14]) >> 3) if int(parts[14]) < 0x8000 else (int(parts[14]) - 0x10000) >> 3) * 0.00004 / 0.08)):.4f}",
                        "I2 [A]": f"{((((int(parts[15]) >> 3) if int(parts[15]) < 0x8000 else (int(parts[15]) - 0x10000) >> 3) * 0.00004 / 0.08)):.4f}",
                        "I3 [A]": f"{((((int(parts[16]) >> 3) if int(parts[16]) < 0x8000 else (int(parts[16]) - 0x10000) >> 3) * 0.00004 / 0.08)):.4f}",
                        "Temp [°C]": f"{(int(parts[17]) * 0.0625 if int(parts[17]) < 0x8000 else (int(parts[17]) - 0x10000) * 0.0625):.4f}"
                    }
                except Exception as e:
                    print("Info parse error: {}".format(e))
                    # Fall back to simple string response
                    msg = data_str
                    print("Received Reply: {}".format(data_str))
            else:
                # Simple response (like ping response)
                msg = data_str
                print("Received Reply: {}".format(data_str))
        except Exception as e:
            print("Response decode error: {}".format(e))
            msg = str(data)
    else:
        print(f"Received Measure: {data}")

    rx_cbk_queue.put(msg) 
    return msg



rx_cbk_queue = queue.Queue()

if __name__ == "__main__":
    server = eLinkTCPServer(handler=rx_handler)
    server.start()
    try:
        while True:
            try:
                ret = rx_cbk_queue.get(timeout=1)
                if ret is not None:
                    if len(ret) > 10:
                        for k in ret.keys():
                            print("%-10s: %s" % (str(k), str(ret[k])))
                    else:
                        print("Response:", ret)
            except queue.Empty:
                pass

    except KeyboardInterrupt:
        server.stop()
