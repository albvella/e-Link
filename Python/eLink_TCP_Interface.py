import socket
import threading
from fastcrc import crc32 as crc
import base64
from datetime import datetime
import threading
import queue

class eLinkTCPServer:
    def __init__(self, host='esdplab.unipa.it', port=9000, handler=None):
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
        self.running = True
        print(f"TCP Server listening on {self.host}:{self.port}")
        threading.Thread(target=self._accept_loop, daemon=True).start()

    def stop(self):
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


    def send_command(self, client_sock, command, cfg_var=None, cfg_idx=None, cfg_val=None, buffer_size=20):
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
            client_sock.sendall(payload.encode())
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    def receive_measure(self, client_sock, filename=None, chunk_size=2048):
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
            print(f"[Thread] Saved received data to {filename}")

        t = threading.Thread(target=worker, daemon=True)
        t.start()
        return t

    def send_OTA(self, client_sock, filename, chunk_size=1024):
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
        def worker():
            self.OTA_routine(client_sock, filename)
        t = threading.Thread(target=worker, daemon=True)
        t.start()
        return t

    def _accept_loop(self):
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
                        print(f"Log from {addr}: {data}")
                        self.client_log_queues[addr].put(data)
                    elif data.startswith(b'R:'):
                        print(f"Reply from {addr}: {data}")
                        self.client_reply_queues[addr].put(data)
                    elif len(data) > 400:
                        print(f"Measure from {addr}: {data}")
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
    if(data.startswith(b'L:')):
        print(f"Log: {data}")
    elif(data.startswith(b'R:')):
        print(f"Reply: {data}")
    else:
        print(f"Received Measure: {data}")

if __name__ == "__main__":
    server = eLinkTCPServer(port=9000, handler=rx_handler)
    server.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop()
