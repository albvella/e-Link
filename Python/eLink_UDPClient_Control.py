#!/usr/bin/env python3
import threading
import time
from eLink_UDP_Interface import eLinkUDPServer, rx_cbk_queue
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
    print("\n===  eLink Device Control Interface (UDP) ===")
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
            cmd = input("eLink-UDP> ").strip().split()
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
                else:
                    print(f"Failed to send idle command to device {device_id}")

            elif cmd[0] == "ping" and len(cmd) >= 2:
                device_id = int(cmd[1])
                if server.send_command_to_device(device_id, "PNG"):
                    print(f"Ping command sent to device {device_id}")
                else:
                    print(f"Failed to send ping command to device {device_id}")

            elif cmd[0] == "start" and len(cmd) >= 2:
                device_id = int(cmd[1])
                if server.send_command_to_device(device_id, "SRT"):
                    print(f"Start command sent to device {device_id}")
                else:
                    print(f"Failed to send start command to device {device_id}")

            elif cmd[0] == "log" and len(cmd) >= 3:
                device_id = int(cmd[1])
                state = cmd[2]
                command = f"SND,{state}"
                if server.send_command_to_device(device_id, "SND", state):
                    print(f"Log command (state: {state}) sent to device {device_id}")
                else:
                    print(f"Failed to send log command to device {device_id}")

            elif cmd[0] == "measure" and len(cmd) >= 2:
                device_id = int(cmd[1])
                if server.send_command_to_device(device_id, "MSR"):
                    print(f"Measure command sent to device {device_id}")
                else:
                    print(f"Failed to send measure command to device {device_id}")

            elif cmd[0] == "reset" and len(cmd) >= 2:
                device_id = int(cmd[1])
                if server.send_command_to_device(device_id, "RST"):
                    print(f"Reset command sent to device {device_id}")
                else:
                    print(f"Failed to send reset command to device {device_id}")

            elif cmd[0] == "get":
                if len(cmd) >= 3:
                    device_id = int(cmd[1])
                    var_name = cmd[2]
                    idx = int(cmd[3]) if len(cmd) >= 4 else 0
                    
                    if server.send_command_to_device(device_id, "GET", var_name, idx):
                        print(f"Get command sent to device {device_id} for {var_name}[{idx}]")
                    else:
                        print(f"Failed to send get command to device {device_id}")
                else:
                    print("Usage: get <device_id> <variable> [index]")

            elif cmd[0] == "set":
                if len(cmd) >= 4:
                    device_id = int(cmd[1])
                    var_name = cmd[2]
                    
                    if len(cmd) == 4:
                        # set <id> <var> <val> - idx=0
                        idx = 0
                        val = cmd[3]
                    else:
                        # set <id> <var> <idx> <val>
                        idx = int(cmd[3])
                        val = cmd[4]
                    
                    if server.send_command_to_device(device_id, "SET", var_name, idx, val):
                        print(f"Set command sent to device {device_id}: {var_name}[{idx}] = {val}")
                    else:
                        print(f"Failed to send set command to device {device_id}")
                else:
                    print("Usage: set <device_id> <variable> <value> OR set <device_id> <variable> <index> <value>")

            elif cmd[0] == "ota":
                if len(cmd) >= 3:
                    device_id = int(cmd[1])
                    file_path = cmd[2]
                    
                    print(f"Starting OTA update for device {device_id} with file {file_path}...")
                    if server.send_ota_file(device_id, file_path):
                        print(f"OTA update initiated for device {device_id}")
                    else:
                        print(f"Failed to start OTA update for device {device_id}")
                else:
                    print("Usage: ota <device_id> <file_path>")

            else:
                print("Unknown command or insufficient arguments")
                print("Type 'quit' to exit, 'monitor' to return to connection monitor, or use available commands")
                
        except ValueError as e:
            print(f"Invalid number format: {e}")
        except Exception as e:
            print(f"Command error: {e}")

def connection_monitor(server):
    """
    Monitora continuamente le connessioni e i dati ricevuti in background.
    """
    last_device_count = 0
    
    while server.running:
        try:
            # Monitor connessioni
            current_devices = server.get_connected_devices()
            if len(current_devices) != last_device_count:
                # Rileva nuove connessioni
                if len(current_devices) > last_device_count:
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
                        print(f"   {k:<20}: {v}")  
                else:
                    if not str(ret).startswith("H:") and ret != "ACK":
                        pass
        except:
            pass

def rx_handler(data, addr, server_instance):
    """
    Handler per processare i dati ricevuti dai client UDP.
    Adattato per la signature UDP (con parametro addr).
    """
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
    elif(data.startswith(b'H:')):
        time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
        print(f"Heartbeat received from device {data[2:].decode('utf-8').strip()} at {time}.")
    else:
        print(f"Received from {addr}: {len(data)} bytes")

    rx_cbk_queue.put(msg) 
    return msg


if __name__ == "__main__":
    # Avvia il server UDP
    server = eLinkUDPServer(handler=rx_handler)
    server.start()

    print(f"eLink UDP Server started on port {server.port}")
    print("Monitoring for incoming UDP packets...")
    
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
        print("\nUDP Server stopped.")