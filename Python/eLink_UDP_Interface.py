import socket
import threading
from fastcrc import crc32 as crc
import base64
from datetime import datetime
import queue
import time
import pytz

class eLinkUDPServer:
    """
    Server UDP per la gestione di dispositivi e-Link.
    Gestisce connessioni multiple, invio comandi, ricezione misure, OTA e code di messaggi.
    """
    def __init__(self, host='0.0.0.0', port=21003, handler=None):
        """
        Inizializza il server UDP.

        Args:
            host (str): Indirizzo host su cui ascoltare.
            port (int): Porta su cui ascoltare.
            handler (callable, optional): Funzione di callback per processare i dati ricevuti.
        """
        self.host = host
        self.port = port
        self.handler = handler  # function to process received data
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.running = False
        self.threads = []
        self.clients = {}  # addr -> last_seen_timestamp
        self.device_clients = {}  # device_id -> addr
        self.client_log_queues = {}
        self.client_reply_queues = {} 
        self.client_meas_queues = {}
        self.client_timeout = 300  # 5 minutes timeout for UDP clients
        self.allowed_commands = ["IDL", "SRT", "PNG", "SND,1", "SND,0", "MSR", "OTA", "SET", "GET", "RST"]
        self.allowed_vars = ["DEVICE_ID", "SAMP_FREQ", "BUFFER_SECS", "CONN_TIMEOUT", "LOG_PERIOD", "HAMMER_TH", "HIGH_TH", "LOW_TH", "TCP_IP", "TCP_PORT"]

    def start(self):
        """
        Avvia il server UDP e inizia ad accettare pacchetti.
        """
        self.running = True
        print(f"UDP Server listening on {self.host}:{self.port}")
        threading.Thread(target=self._receive_loop, daemon=True).start()
        threading.Thread(target=self._cleanup_loop, daemon=True).start()

    def stop(self):
        """
        Ferma il server UDP, chiude il socket e pulisce le code.
        """
        self.running = False
        for addr, queue in self.client_log_queues.items():
            queue.queue.clear()
        for addr, queue in self.client_reply_queues.items():
            queue.queue.clear()
        for addr, queue in self.client_meas_queues.items():
            queue.queue.clear()
        self.clients.clear()
        self.device_clients.clear()
        self.client_log_queues.clear()
        self.client_reply_queues.clear()
        self.client_meas_queues.clear()
        self.server_socket.close()
        print("UDP Server stopped")

    def _receive_loop(self):
        """
        Loop principale per ricevere pacchetti UDP.
        """
        while self.running:
            try:
                data, addr = self.server_socket.recvfrom(4096)
                self._handle_client_data(addr, data)
            except Exception as e:
                if self.running:
                    print(f"UDP receive error: {e}")

    def _cleanup_loop(self):
        """
        Loop per pulire i client UDP inattivi.
        """
        while self.running:
            current_time = time.time()
            inactive_clients = []
            
            for addr, last_seen in self.clients.items():
                if current_time - last_seen > self.client_timeout:
                    inactive_clients.append(addr)
            
            for addr in inactive_clients:
                print(f"UDP client {addr} timed out, removing...")
                self._remove_client(addr)
            
            time.sleep(30)  # Check every 30 seconds

    def _handle_client_data(self, addr, data):
        """
        Gestisce i dati ricevuti da un client UDP.
        """
        # Update last seen timestamp
        self.clients[addr] = time.time()
        
        # Initialize client queues if new
        if addr not in self.client_log_queues:
            self.client_log_queues[addr] = queue.Queue()
            self.client_reply_queues[addr] = queue.Queue()
            self.client_meas_queues[addr] = queue.Queue()
            print(f"\n=== NEW UDP CLIENT CONNECTED ===")
            print(f"Address: {addr[0]}:{addr[1]}")
            print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
            print("=" * 35)

        # Extract device ID if available
        if data.startswith(b'H:') or data.startswith(b'R:'):
            try:
                data_str = data.decode('utf-8')
                if ':' in data_str:
                    device_id = int(data_str.split(':')[1].split(',')[0])
                    if device_id not in self.device_clients:
                        print(f"\n*** DEVICE ID {device_id} REGISTERED ***")
                        print(f"From: {addr[0]}:{addr[1]}")
                        print("*" * 35)
                    self.device_clients[device_id] = addr
            except Exception as e:
                pass  # Ignore ID extraction errors

        # Process data with handler
        if self.handler:
            try:
                threading.Thread(target=self.handler, args=(data, addr, self), daemon=True).start()
            except Exception as e:
                print(f"Handler error: {e}")

    def _remove_client(self, addr):
        """
        Rimuove un client e pulisce le sue risorse.
        """
        if addr in self.clients:
            del self.clients[addr]
        
        if addr in self.client_log_queues:
            del self.client_log_queues[addr]
        
        if addr in self.client_reply_queues:
            del self.client_reply_queues[addr]
            
        if addr in self.client_meas_queues:
            del self.client_meas_queues[addr]

        # Remove from device mapping
        device_to_remove = None
        for device_id, client_addr in self.device_clients.items():
            if client_addr == addr:
                device_to_remove = device_id
                break
        
        if device_to_remove is not None:
            del self.device_clients[device_to_remove]

    def send_command(self, client_addr, command, cfg_var=None, cfg_idx=None, cfg_val=None):
        """
        Invia un comando al client tramite UDP.

        Args:
            client_addr (tuple): Indirizzo del client (IP, porta).
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
                    print(f"Configuration commands require all parameters (var, idx, val)")
                    return False

            checksum = crc(payload.encode("utf-8"))
            payload_with_checksum = payload + f",{checksum}\n"

            try:
                self.server_socket.sendto(payload_with_checksum.encode('utf-8'), client_addr)
                print(f"Command sent to {client_addr}: {payload}")
                return True
            except Exception as e:
                print(f"Failed to send command to {client_addr}: {e}")
                return False

        threading.Thread(target=worker, daemon=True).start()

    def send_command_to_device(self, device_id, command, cfg_var=None, cfg_idx=None, cfg_val=None):
        """
        Invia un comando a un dispositivo specifico tramite device ID.

        Args:
            device_id (int): ID del dispositivo.
            command (str): Comando da inviare.
            cfg_var (str, optional): Variabile di configurazione.
            cfg_idx (int, optional): Indice di configurazione.
            cfg_val (str/int, optional): Valore di configurazione.

        Returns:
            bool: True se il comando è stato inviato, False altrimenti.
        """
        if device_id == 0:  # Broadcast to all devices
            success_count = 0
            for addr in self.clients.keys():
                if self.send_command(addr, command, cfg_var, cfg_idx, cfg_val):
                    success_count += 1
            print(f"Broadcast command sent to {success_count} device(s)")
            return success_count > 0
        elif device_id in self.device_clients:
            client_addr = self.device_clients[device_id]
            return self.send_command(client_addr, command, cfg_var, cfg_idx, cfg_val)
        else:
            print(f"Device {device_id} not found or not connected")
            return False

    def get_connected_devices(self):
        """
        Restituisce la lista degli ID dei dispositivi connessi.

        Returns:
            list: Lista degli ID dei dispositivi connessi.
        """
        return list(self.device_clients.keys())

    def get_connected_clients(self):
        """
        Restituisce la lista degli indirizzi dei client connessi.

        Returns:
            list: Lista degli indirizzi dei client connessi.
        """
        return list(self.clients.keys())

    def print_connection_status(self):
        """
        Stampa lo stato delle connessioni UDP attive.
        """
        print(f"\n=== UDP CONNECTION STATUS ===")
        print(f"Active clients: {len(self.clients)}")
        print(f"Registered devices: {len(self.device_clients)}")
        
        if self.clients:
            print("\nActive UDP clients:")
            for addr, last_seen in self.clients.items():
                age = time.time() - last_seen
                print(f"  {addr[0]}:{addr[1]} - Last seen: {age:.1f}s ago")
        
        if self.device_clients:
            print("\nRegistered devices:")
            for device_id, addr in self.device_clients.items():
                print(f"  Device {device_id} - {addr[0]}:{addr[1]}")
        
        print("=" * 30)

    def send_ota_file(self, device_id, file_path):
        """
        Invia un file OTA a un dispositivo specifico.

        Args:
            device_id (int): ID del dispositivo.
            file_path (str): Percorso del file da inviare.

        Returns:
            bool: True se l'OTA è stato avviato, False altrimenti.
        """
        if device_id not in self.device_clients:
            print(f"Device {device_id} not found or not connected")
            return False

        client_addr = self.device_clients[device_id]

        def ota_worker():
            try:
                with open(file_path, 'rb') as file:
                    file_content = file.read()

                # Encode file content in base64
                encoded_content = base64.b64encode(file_content).decode('utf-8')

                # Send OTA start command
                if not self.send_command(client_addr, "OTA"):
                    print("Failed to send OTA start command")
                    return False

                # Wait a bit for device to prepare
                time.sleep(2)

                # Send file in chunks (UDP packet size limit)
                chunk_size = 1000  # Conservative chunk size for UDP
                total_chunks = len(encoded_content) // chunk_size + (1 if len(encoded_content) % chunk_size else 0)

                for i in range(total_chunks):
                    start_idx = i * chunk_size
                    end_idx = min((i + 1) * chunk_size, len(encoded_content))
                    chunk = encoded_content[start_idx:end_idx]

                    # Send chunk with sequence number
                    ota_packet = f"OTA,{i},{total_chunks},{chunk}"
                    checksum = crc(ota_packet.encode("utf-8"))
                    ota_packet_with_checksum = ota_packet + f",{checksum}\n"

                    try:
                        self.server_socket.sendto(ota_packet_with_checksum.encode('utf-8'), client_addr)
                        print(f"OTA chunk {i+1}/{total_chunks} sent to device {device_id}")
                        time.sleep(0.1)  # Small delay between chunks
                    except Exception as e:
                        print(f"Failed to send OTA chunk {i+1}: {e}")
                        return False

                print(f"OTA file transfer completed for device {device_id}")
                return True

            except FileNotFoundError:
                print(f"OTA file not found: {file_path}")
                return False
            except Exception as e:
                print(f"OTA transfer error: {e}")
                return False

        threading.Thread(target=ota_worker, daemon=True).start()
        return True

    def get_log_queue(self, device_id):
        """
        Restituisce la coda dei log per un dispositivo specifico.

        Args:
            device_id (int): ID del dispositivo.

        Returns:
            queue.Queue: Coda dei log o None se il dispositivo non è connesso.
        """
        if device_id in self.device_clients:
            client_addr = self.device_clients[device_id]
            return self.client_log_queues.get(client_addr)
        return None

    def get_reply_queue(self, device_id):
        """
        Restituisce la coda delle risposte per un dispositivo specifico.

        Args:
            device_id (int): ID del dispositivo.

        Returns:
            queue.Queue: Coda delle risposte o None se il dispositivo non è connesso.
        """
        if device_id in self.device_clients:
            client_addr = self.device_clients[device_id]
            return self.client_reply_queues.get(client_addr)
        return None

    def get_meas_queue(self, device_id):
        """
        Restituisce la coda delle misure per un dispositivo specifico.

        Args:
            device_id (int): ID del dispositivo.

        Returns:
            queue.Queue: Coda delle misure o None se il dispositivo non è connesso.
        """
        if device_id in self.device_clients:
            client_addr = self.device_clients[device_id]
            return self.client_meas_queues.get(client_addr)
        return None


def rx_handler(data, addr, server_instance):
    """
    Handler per processare i dati ricevuti dai client UDP.

    Args:
        data (bytes): Dati ricevuti.
        addr (tuple): Indirizzo del client.
        server_instance: Istanza del server UDP.

    Returns:
        dict or str: Dati processati.
    """
    # Timezone italiana
    italy_tz = pytz.timezone('Europe/Rome')
    
    # Decode data
    try:
        data_str = data.decode('utf-8').strip()
    except:
        return None

    # Constants for data parsing
    press_FS = 10  # bar
    clock_freq = 32000000  # Hz
    
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
                        "Uptime": datetime(year=int(parts[2]) + 2000, month=int(parts[3]), day=int(parts[4]), hour=int(parts[5]), minute=int(parts[6]), second=int(parts[7])),
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
    server = eLinkUDPServer(handler=rx_handler)
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