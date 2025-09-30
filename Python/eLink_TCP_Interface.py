import socket
import threading
from fastcrc import crc32 as crc
import base64
from datetime import datetime
import threading

class eLinkTCPServer:
    def __init__(self, host='0.0.0.0', port=9000, handler=None):
        self.host = host
        self.port = port
        self.handler = handler  # function to process received data
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.running = False
        self.threads = []


    def receive_measure(self, client_sock, filename=None, chunk_size=2048):
        if filename is None:
            filename = datetime.now().strftime("%y%m%d_%H%M.bin")
        with open(filename, "ab") as f:
            while True:
                client_sock.settimeout(5)
                try:
                    chunk = client_sock.recv(chunk_size)
                except socket.timeout:
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
        print(f"Saved received data to {filename}")
        return filename

    def receive_measure_threaded(self, client_sock, filename=None, chunk_size=2048):
        if filename is None:
            filename = datetime.now().strftime("%y%m%d_%H%M.bin")

        def worker():
            with open(filename, "ab") as f:
                while True:
                    try:
                        client_sock.settimeout(5)
                        try:
                            chunk = client_sock.recv(chunk_size)
                        except socket.timeout:
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
                    client_sock.settimeout(5)
                    try:
                        ack = client_sock.recv(16)  # attende l'ACK dal client (max 16 byte)
                    except socket.timeout:
                        print("ACK timeout!")
                        break
                    if ack.strip() != b'ACK':
                        print("ACK not received!")
                        break
            print(f"File {filename} sent to client.")
        except Exception as e:
            print(f"Error sending file: {e}")

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
        except Exception as e:
            print(f"Error sending CRC32: {e}")

    def start(self):
        self.running = True
        print(f"TCP Server listening on {self.host}:{self.port}")
        threading.Thread(target=self._accept_loop, daemon=True).start()

    def _accept_loop(self):
        while self.running:
            try:
                client_sock, addr = self.server_socket.accept()
                print(f"Connection from {addr}")
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
                        break
                    print(f"Received from {addr}: {data}")
                    if self.handler:
                        response = self.handler(data)
                        if response:
                            client_sock.sendall(response)
                except Exception as e:
                    print(f"Client error {addr}: {e}")
                    break

    def stop(self):
        self.running = False
        self.server_socket.close()
        print("TCP Server stopped")

# Example handler function
def echo_handler(data):
    return data  # echo back

if __name__ == "__main__":
    server = eLinkTCPServer(port=9000, handler=echo_handler)
    server.start()
    try:
        while True:
            client_sock, addr = server.server_socket.accept()
            print(f"Connessione da {addr}")
            pass
    except KeyboardInterrupt:
        server.stop()
