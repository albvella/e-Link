import socket
import threading
from fastcrc import crc32 as crc
import base64
from datetime import datetime
import queue

class eLinkTCPServer:
    """
    Server TCP per la gestione di dispositivi e-Link.
    Gestisce connessioni multiple, invio comandi, ricezione misure, OTA e code di messaggi.
    """
    def __init__(self, host='esdplab.unipa.it', port=9000, handler=None):
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
        self.clients = {}
        self.client_log_queues = {}
        self.client_reply_queues = {} 
        self.client_meas_queues = {}
        self.allowed_commands = ["IDL", "SRT", "PNG", "SND", "MSR", "OTA", "SET", "GET", "RST"]

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
            if cfg_var is not None and cfg_idx is not None and cfg_val is not None:
                payload = f"+CMD,{command},{cfg_var},{cfg_idx},{cfg_val}"
            elif cfg_var is not None and cfg_val is not None:
                payload = f"+CMD,{command},0,{cfg_val}"
            else:
                payload = f"+CMD,{command}"

            try:
                client_sock.sendall(payload.encode())
            except Exception as e:
                print(f"Error sending command: {e}")
        t = threading.Thread(target=worker, daemon=True)
        t.start()


    def receive_measure(self, client_sock, filename=None):
        """
        Riceve dati di misura dal client e li salva su file.

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
                while True:
                    try:
                        try:
                            chunk = self.client_meas_queues[client_sock.getpeername()].get(timeout=5)
                        except queue.Empty:
                            print("Receive Timeout!")
                            break
                        if not chunk:
                            break
                        try:
                            bin_data = base64.b64decode(chunk)
                            f.write(bin_data)
                        except Exception as e:
                            print(f"Base64 decode error: {e}")
                            break
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
                print(f"Client List: {list(self.clients.keys())}")
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
        with client_sock:
            while True:
                try:
                    data = client_sock.recv(4096)
                    if not data:
                        print(f"Connection closed by {addr}")
                        self.client_reply_queues[addr].queue.clear()
                        self.client_log_queues[addr].queue.clear()
                        self.client_meas_queues[addr].queue.clear()
                        del self.clients[addr]
                        del self.client_reply_queues[addr]
                        del self.client_log_queues[addr]
                        del self.client_meas_queues[addr]
                        break

                    if data.startswith(b'L:'):
                        data = data[2:]
                        self.client_log_queues[addr].put(data)
                    elif data.startswith(b'R:'):
                        data = data[2:]
                        self.client_reply_queues[addr].put(data)
                    elif len(data) > 400:
                        self.client_meas_queues[addr].put(data)
                    else:
                        print(f"Unknown data from {addr}: {data}")
                        break

                    if self.handler:
                        self.handler(data)
                        
                except Exception as e:
                    print(f"Client error {addr}: {e}")
                    break



def rx_handler(data):
    clock_freq = 80000000
    press_FS = 50
    
    msg = {}
    if(data.startswith(b'L:')):
        try:
            data = data[2:]
            parts = data.split(",")
            msg = {
                "ID" : int(parts[0]),
                "Press": int(parts[1]) * press_FS / 4096,
                "FLow": clock_freq / int(parts[2]),
                "ax": int(parts[3]) * 0.061,
                "ay": int(parts[4]) * 0.061,
                "az": int(parts[5]) * 0.061,
                "Vbatt": int(parts[6]) * 0.001,
                "I1": (((int(parts[7]) >>3) if int(parts[7]) < 0x8000 else (int(parts[7]) - 0x10000) >>3) * 0.00004 / 0.08),
                "I2": (((int(parts[8]) >>3) if int(parts[8]) < 0x8000 else (int(parts[8]) - 0x10000) >>3) * 0.00004 / 0.08),
                "I3": (((int(parts[9]) >>3) if int(parts[9]) < 0x8000 else (int(parts[9]) - 0x10000) >>3) * 0.00004 / 0.08),
                "V1": int(parts[10]) * 0.008,
                "V2": int(parts[11]) * 0.008,
                "V3": int(parts[12]) * 0.008,
                "Temp": int(parts[13]) * 0.0625 if int(parts[13]) < 0x8000 else (int(parts[13]) - 0x10000) * 0.0625
            }
        except Exception as e:
            print(f"Data parse error: {e}")

    elif(data.startswith(b'R:')):
        if len(data) > 10:
            try:
                data = data[2:]
                parts = data.split(",")
                msg = {
                    "ID": int(parts[0]),
                    "Firmware Version": float(f"{int(parts[1]) >> 8}.{int(parts[1]) & 0xFF}"),
                    "Uptime": datetime(year=int(parts[2]), month=int(parts[3]), day=int(parts[4]), hour=int(parts[5]), minute=int(parts[6]), second=int(parts[7])),
                    "Vbatt": int(parts[8]) * 0.001,
                    "Sampling Freq": int(parts[9]),
                    "Buffering Secs": int(parts[10]),
                    "V1": int(parts[11]) * 0.008,
                    "V2": int(parts[12]) * 0.008,
                    "V3": int(parts[13]) * 0.008,
                    "I1": (((int(parts[14]) >> 3) if int(parts[14]) < 0x8000 else (int(parts[14]) - 0x10000) >> 3) * 0.00004 / 0.08),
                    "I2": (((int(parts[15]) >> 3) if int(parts[15]) < 0x8000 else (int(parts[15]) - 0x10000) >> 3) * 0.00004 / 0.08),
                    "I3": (((int(parts[16]) >> 3) if int(parts[16]) < 0x8000 else (int(parts[16]) - 0x10000) >> 3) * 0.00004 / 0.08),
                    "Temp": (int(parts[17]) * 0.0625 if int(parts[17]) < 0x8000 else (int(parts[17]) - 0x10000) * 0.0625)
                }
            except Exception as e:
                print(f"Info parse error: {e}")
        else:
            data = data[2:]
            msg = data
    else:
        print(f"Received Measure: {data}")

    rx_cbk_queue.put(msg) 
    return msg


rx_cbk_queue = queue.Queue()

if __name__ == "__main__":
    server = eLinkTCPServer(port=9000, handler=rx_handler)
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
