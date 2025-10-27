#!/usr/bin/env python3
import threading
import time
from eLink_TCP_Interface import eLinkTCPServer, rx_cbk_queue
from datetime import datetime

def wait_for_connections(server):
    """
    Aspetta le connessioni e permette all'utente di decidere quando iniziare.
    """
    print("\n Waiting for device connections...")
    print(" Commands available while waiting:")
    print("  list          - Show connected devices")
    print("  start         - Start command interface")
    print("  quit          - Exit program")
    print("=" * 50)
    
    while True:
        try:
            cmd = input("Monitor> ").strip().split()
            if not cmd:
                continue
                
            if cmd[0] == "quit":
                server.stop()
                return False
                
            elif cmd[0] == "list":
                devices = server.get_connected_devices()
                if devices:
                    print(f"Connected devices: {devices} (Total: {len(devices)})")
                else:
                    print("No devices connected")
                    
            elif cmd[0] == "start":
                devices = server.get_connected_devices()
                if devices:
                    print(f"Starting command interface with {len(devices)} connected device(s): {devices}")
                    return True
                else:
                    print("No devices connected. Connect at least one device before starting.")
                    
            else:
                print("Unknown command. Use 'list', 'start', or 'quit'")
                
        except KeyboardInterrupt:
            server.stop()
            return False
        except Exception as e:
            print(f"Error: {e}")

def command_interface(server):
    """
    Interfaccia a riga di comando per inviare comandi ai dispositivi.
    """
    print("\n===  eLink Device Control Interface ===")
    print("Available commands:")
    print("  list            - Show connected devices")
    print("  ping <id>       - Ping device (id=0 for broadcast)")
    print("  idle <id>       - Set device to idle state")
    print("  start <id>      - Start measurement operation on device")
    print("  log <id> <state> - Set logging state on device")
    print("  measure <id>    - Request measurement from device")
    print("  reset <id>      - Reset device")
    print("  get <id> <var>  - Get configuration variable (idx=0)")
    print("  get <id> <var> <idx> - Get configuration variable with index")
    print("  set <id> <var> <val> - Set configuration variable (idx=0)")  
    print("  set <id> <var> <idx> <val> - Set configuration variable with index")
    print("  ota <id> <file> - Start OTA firmware update")
    print("  monitor         - Return to connection monitor")
    print("  quit            - Exit program")
    print("  Note: <id> is device ID, <var> is variable name, <idx> is index (optional for set), <val> is value.")
    print(f"  Allowed variables: {', '.join(server.allowed_vars)}")
    print("=" * 45 + "\n")
    
    while True:
        try:
            cmd = input("eLink> ").strip().split()
            if not cmd:
                continue
                
            if cmd[0] == "quit":
                server.stop()
                break
                
            elif cmd[0] == "monitor":
                print("Returning to connection monitor...")
                return "monitor"
                
            elif cmd[0] == "list":
                devices = server.get_connected_devices()
                if devices:
                    print(f"Connected devices: {devices}")
                else:
                    print("No devices connected")

            elif cmd[0] == "idle" and len(cmd) >= 2:
                device_id = int(cmd[1])
                if server.send_command_to_device(device_id, "IDL"):
                    print(f"Idle command sent to device {device_id}")
 
            elif cmd[0] == "start" and len(cmd) >= 2:
                device_id = int(cmd[1])
                if server.send_command_to_device(device_id, "SRT"):
                    print(f"Start command sent to device {device_id}")
                    
            elif cmd[0] == "ping" and len(cmd) >= 2:
                device_id = int(cmd[1])
                if server.send_command_to_device(device_id, "PNG"):
                    print(f"Ping sent to device {device_id}")

            elif cmd[0] == "log" and len(cmd) >= 3:
                device_id = int(cmd[1])
                log_state = cmd[2]
                command = f"SND,{log_state}"
                if server.send_command_to_device(device_id, command):
                    print(f"Toggle logging sent to device {device_id}")

            elif cmd[0] == "measure" and len(cmd) >= 2:
                device_id = int(cmd[1])
                if server.send_command_to_device(device_id, "MSR"):
                    print(f"Measure requested to device {device_id}")
                    client_sock = server.get_client_by_device_id(device_id)
                    if client_sock:
                        print(f"Starting measure reception for device {device_id}...")
                        server.receive_measure(client_sock)  
                    else:
                        print(f"Warning: Device {device_id} socket not found")
                else:
                    print(f"Failed to send measure command to device {device_id}")
                    
            elif cmd[0] == "ota" and len(cmd) >= 3:
                device_id = int(cmd[1])
                firmware_file = cmd[2]
                client_sock = server.get_client_by_device_id(device_id)
                if client_sock:
                    print(f"Starting OTA update for device {device_id} with file {firmware_file}...")
                    server.OTA(client_sock, firmware_file)
                else:
                    print(f"Device ID {device_id} not found")

            elif cmd[0] == "reset" and len(cmd) >= 2:
                device_id = int(cmd[1])
                if server.send_command_to_device(device_id, "RST"):
                    print(f"Reset sent to device {device_id}")
                    
            elif cmd[0] == "get" and len(cmd) >= 3:
                device_id = int(cmd[1])
                var_name = cmd[2]
                if len(cmd) == 3:  # get <id> <var> (senza indice)
                    var_idx = 0  # Usa indice 0 di default
                    if server.send_command_to_device(device_id, "GET", var_name, var_idx, 0):
                        print(f"Get {var_name} sent to device {device_id}")
                elif len(cmd) >= 4:  # get <id> <var> <idx> (con indice)
                    var_idx = int(cmd[3])
                    if server.send_command_to_device(device_id, "GET", var_name, var_idx, 0):
                        print(f"Get {var_name}[{var_idx}] sent to device {device_id}")
                    
            elif cmd[0] == "set" and len(cmd) >= 4:
                if len(cmd) == 4:  # set <id> <var> <val> (senza indice)
                    device_id = int(cmd[1])
                    var_name = cmd[2]
                    value = cmd[3]
                    var_idx = 0  # Usa indice 0 di default quando non specificato
                    if server.send_command_to_device(device_id, "SET", var_name, var_idx, value):
                        print(f"Set {var_name}={value} sent to device {device_id}")
                elif len(cmd) >= 5:  # set <id> <var> <idx> <val> (con indice)
                    device_id = int(cmd[1])
                    var_name = cmd[2]
                    var_idx = int(cmd[3])
                    value = cmd[4]
                    if server.send_command_to_device(device_id, "SET", var_name, var_idx, value):
                        print(f"Set {var_name}[{var_idx}]={value} sent to device {device_id}")
                    
            else:
                print("Invalid command. Type 'quit' to exit.")
                
        except ValueError:
            print("Invalid device ID. Must be a number.")
        except KeyboardInterrupt:
            server.stop()
            break
        except Exception as e:
            print(f"Error: {e}")

def connection_monitor(server):
    """
    Monitor delle connessioni e dei dati ricevuti dai dispositivi.
    """
    last_device_count = 0
    
    while True:
        try:
            # Controlla nuove connessioni
            current_devices = server.get_connected_devices()
            if len(current_devices) != last_device_count:
                if len(current_devices) > last_device_count:
                    new_devices = set(current_devices) - set(server.get_connected_devices() if last_device_count == 0 else [])
                    for device_id in current_devices:
                        if last_device_count == 0 or device_id not in (server.get_connected_devices()[:last_device_count] if last_device_count > 0 else []):
                            print(f"\nNEW CONNECTION: Device ID {device_id} connected!")
                
                print(f"Connected devices: {current_devices} (Total: {len(current_devices)})")
                last_device_count = len(current_devices)
            
            # Monitor dati ricevuti
            ret = rx_cbk_queue.get(timeout=1)
            if ret is not None:
                if isinstance(ret, dict) and len(ret) > 1:
                    print(f"\n[Device {ret.get('ID', '?')}] Data received:")
                    for k, v in ret.items():
                        print(f"   {k}: {v}")
                else:
                    if not ret.startswith("H:"):
                        print(f"\n[Response] {ret}")
        except:
            pass



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
    elif(data.startswith(b'H:')):
        print(f"Heartbeat received from device {data[2:].decode('utf-8').strip()}.")
    else:
        print(f"Received Measure: {len(data)} bytes")

    rx_cbk_queue.put(msg) 
    return msg


if __name__ == "__main__":
    # Avvia il server
    server = eLinkTCPServer(handler=rx_handler)
    server.start()

    print(f"eLink TCP Server started on port {server.port}")
    print("Monitoring for incoming connections...")
    
    # Avvia il monitor connessioni in background
    monitor_thread = threading.Thread(target=connection_monitor, args=(server,), daemon=True)
    monitor_thread.start()
    
    try:
        while True:
            # Prima fase: aspetta connessioni
            if wait_for_connections(server):
                # Seconda fase: interfaccia comandi
                result = command_interface(server)
                if result != "monitor":
                    break
            else:
                break
                
    except KeyboardInterrupt:
        server.stop()
        print("\nServer stopped.")