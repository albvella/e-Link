#!/usr/bin/env python3
"""
eLink TCP Server - Daemon Mode
Basato identicamente su eLink_Client_Control.py ma senza input da tastiera
e con salvataggio automatico nel database per l'interfaccia web.
"""
import threading
import time
import sys
import signal
import sqlite3
from pathlib import Path
from eLink_TCP_Interface import eLinkTCPServer, rx_cbk_queue
from datetime import datetime

# Importa database manager per web interface
sys.path.append(str(Path(__file__).parent / "Web Interface"))
try:
    from db_manager import get_db  # type: ignore
    DB_AVAILABLE = True
    print("✅ Database manager loaded successfully")
except ImportError:
    DB_AVAILABLE = False
    print("⚠️  Database manager not available. Web interface data logging disabled.")

# Flag per shutdown graceful
shutdown_flag = False

def signal_handler(sig, frame):
    """Gestisce SIGINT e SIGTERM per shutdown graceful"""
    global shutdown_flag
    
    if shutdown_flag:
        # Evita doppio processing del signal
        return
    
    print("\n🛑 Shutdown signal received. Stopping server...")
    shutdown_flag = True

def process_command_queue(server):
    """Processa comandi dalla coda database e li invia ai dispositivi"""
    if not DB_AVAILABLE:
        return
        
    try:
        db = get_db()
        pending_commands = db.get_pending_commands()
        
        for cmd in pending_commands:
            device_id = cmd['device_id']
            command = cmd['command']
            parameters = cmd['parameters']
            cmd_id = cmd['id']
            
            # Prepara parametri per invio (corretto per i parametri di send_command_to_device)
            if parameters:
                # Converte parametri CSV in lista
                param_list = parameters.split(',') if parameters else []
                
                # Gestisce i parametri correttamente per la funzione send_command_to_device
                if len(param_list) == 1:
                    success = server.send_command_to_device(device_id, command, param_list[0])
                elif len(param_list) == 2:
                    success = server.send_command_to_device(device_id, command, param_list[0], param_list[1])
                elif len(param_list) == 3:
                    success = server.send_command_to_device(device_id, command, param_list[0], param_list[1], param_list[2])
                else:
                    # Troppi parametri, usa solo i primi 3
                    success = server.send_command_to_device(device_id, command, param_list[0], param_list[1], param_list[2])
                    print(f"⚠️ Avviso: comando {command} ha troppi parametri, usati solo i primi 3")
            else:
                success = server.send_command_to_device(device_id, command)
            
            # Aggiorna status nel database
            if success:
                db.mark_command_sent(cmd_id, "Command sent successfully")
            else:
                db.mark_command_failed(cmd_id, "Failed to send command")
                print(f"❌ Errore invio comando {command} a device {device_id}")
                
    except Exception as e:
        print(f"❌ Errore processamento coda comandi: {e}")

def connection_monitor(server):
    """Monitor delle connessioni e dei dati ricevuti - IDENTICO a eLink_Client_Control + database"""
    last_device_count = 0
    
    while not shutdown_flag:
        try:
            # Controlla nuove connessioni (IDENTICO al client control)
            current_devices = server.get_connected_devices()
            if len(current_devices) != last_device_count:
                if len(current_devices) > last_device_count:
                    # Nuove connessioni - usa stessa logica del client control
                    for device_id in current_devices:
                        if last_device_count == 0 or device_id not in (server.get_connected_devices()[:last_device_count] if last_device_count > 0 else []):
                            print(f"\nNEW CONNECTION: Device ID {device_id} connected!")
                            
                            # Aggiunta daemon-specific: aggiorna stato nel database
                            if DB_AVAILABLE:
                                try:
                                    db = get_db()
                                    ip_addr = None
                                    if hasattr(server, 'device_clients') and device_id in server.device_clients:
                                        ip_addr = server.device_clients[device_id][0]
                                    db.update_device_status(device_id, "connected", ip_addr)
                                except Exception as e:
                                    print(f"Database error updating device status: {e}")
                
                print(f"Connected devices: {current_devices} (Total: {len(current_devices)})")
                last_device_count = len(current_devices)
            
            # Monitor dati ricevuti (IDENTICO al client control)
            ret = rx_cbk_queue.get(timeout=1)
            if ret is not None:
                if isinstance(ret, dict) and len(ret) > 1:
                    print(f"\n[Device {ret.get('ID', '?')}] Data received:")
                    for k, v in ret.items():
                        print(f"   {k:<20}: {v}")  
                else:
                    if not ret.startswith("H:") and ret != "ACK":
                        print(f"\n[Response] {ret}")
                        
                        # Aggiunta daemon-specific: salva risposte nel database  
                        if DB_AVAILABLE and isinstance(ret, str):
                            try:
                                db = get_db()
                                response_data = ret if ret.startswith('R:') else f"R:{ret}"
                                db.insert_device_response(None, response_data)
                                print(f"💾 Risposta salvata nel DB: {response_data[:50]}...")
                            except Exception as e:
                                print(f"Database error saving response: {e}")
                                
            # Aggiunta daemon-specific: processa coda comandi dalla web interface
            try:
                process_command_queue(server)
            except Exception as e:
                if not shutdown_flag:
                    print(f"Command queue processing error: {e}")
                
        except Exception as e:
            if not shutdown_flag:
                print(f"Monitor error: {e}")
        except:
            # Timeout normale dalla coda - ignora (come nel client control)
            pass

def rx_handler(data):
    """Handler per dati ricevuti - IDENTICO a eLink_Client_Control.py"""
    clock_freq = 80000000
    press_FS = 50
    
    msg = {}
    if(data.startswith(b'L:')):
        try:
            data_str = data[2:].decode('utf-8').strip()  
            parts = data_str.split(",")
            
            # Parsing dei dati
            device_id = int(parts[0])
            pressure = int(parts[1]) * press_FS / 4096
            flow = (clock_freq / int(parts[2])) if int(parts[2]) != 0 else 0
            ax = (int(parts[3]) - 65536 if int(parts[3]) > 32767 else int(parts[3])) * 0.061
            ay = (int(parts[4]) - 65536 if int(parts[4]) > 32767 else int(parts[4])) * 0.061
            az = (int(parts[5]) - 65536 if int(parts[5]) > 32767 else int(parts[5])) * 0.061
            vbatt = int(parts[6]) * 0.001
            i1 = (((int(parts[7]) >>3) if int(parts[7]) < 0x8000 else (int(parts[7]) - 0x10000) >>3) * 0.00004 / 0.08)
            i2 = (((int(parts[8]) >>3) if int(parts[8]) < 0x8000 else (int(parts[8]) - 0x10000) >>3) * 0.00004 / 0.08)
            i3 = (((int(parts[9]) >>3) if int(parts[9]) < 0x8000 else (int(parts[9]) - 0x10000) >>3) * 0.00004 / 0.08)
            v1 = int(parts[10]) * 0.001
            v2 = int(parts[11]) * 0.001
            v3 = int(parts[12]) * 0.001
            temperature = (int(parts[13]) * 0.0625 if int(parts[13]) < 0x8000 else (int(parts[13]) - 0x10000) * 0.0625)
            
            # Salva nel database per web interface (aggiunta daemon-specific)
            if DB_AVAILABLE:
                try:
                    db = get_db()
                    db.insert_telemetry(device_id, {
                        'pressure': pressure,
                        'flow': flow,
                        'ax': ax,
                        'ay': ay,
                        'az': az,
                        'vbatt': vbatt,
                        'v1': v1,
                        'v2': v2,
                        'v3': v3,
                        'i1': i1,
                        'i2': i2,
                        'i3': i3,
                        'temperature': temperature
                    })
                except Exception as e:
                    print(f"Database error: {e}")
            
            # Crea messaggio formattato per display (IDENTICO al client control)
            msg = {
                "ID": device_id,
                "Press [bar]": f"{pressure:.4f}",
                "FLow [L/s]": f"{flow:.4f}",
                "ax [mg]": f"{ax:.4f}",
                "ay [mg]": f"{ay:.4f}",
                "az [mg]": f"{az:.4f}",
                "Vbatt [V]": f"{vbatt:.4f}",
                "I1 [A]": f"{i1:.4f}",
                "I2 [A]": f"{i2:.4f}",
                "I3 [A]": f"{i3:.4f}",
                "V1 [V]": f"{v1:.4f}",
                "V2 [V]": f"{v2:.4f}",
                "V3 [V]": f"{v3:.4f}",
                "Temp [°C]": f"{temperature:.4f}"
            }
        except Exception as e:
            print(f"Data parse error: {e}")

    elif(data.startswith(b'R:')):
        try:
            data_str = data[2:].decode('utf-8').strip()  
            parts = data_str.split(",")
            
            # Salva la risposta nel database (aggiunta daemon-specific)
            if DB_AVAILABLE and len(parts) > 0:
                try:
                    device_id = int(parts[0])  # Il primo campo è sempre il device_id
                    db = get_db()
                    response_data = f"R:{data_str}"
                    db.insert_device_response(device_id, response_data)
                    print(f"💾 Risposta R: salvata nel DB per dispositivo {device_id}: {response_data[:50]}...")
                except Exception as e:
                    print(f"Database error saving R: response: {e}")
            
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
        print(f"Heartbeat received from device {data[2:].decode('utf-8').strip()}.")
    else:
        print(f"Received Measure: {len(data)} bytes")

    rx_cbk_queue.put(msg) 
    return msg


if __name__ == "__main__":
    # Setup signal handlers per shutdown graceful
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    print("=" * 60)
    print("🚀 e-Link TCP Server - Daemon Mode")
    print("=" * 60)
    
    # Pulisci database all'avvio
    if DB_AVAILABLE:
        try:
            db = get_db()
            # Segna tutti i dispositivi come disconnessi all'avvio
            with db.lock:
                with sqlite3.connect(str(db.db_path)) as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        UPDATE devices 
                        SET status = 'disconnected'
                        WHERE status = 'connected'
                    """)
                    disconnected_count = cursor.rowcount
                    conn.commit()
            
            if disconnected_count > 0:
                print(f"🧹 Database cleanup: {disconnected_count} dispositivi segnati come disconnessi")
            else:
                print("🧹 Database cleanup: nessun dispositivo da disconnettere")
        except Exception as e:
            print(f"⚠️ Errore pulizia database: {e}")
    
    # Avvia il server
    server = eLinkTCPServer(handler=rx_handler)
    server.start()

    print(f"✅ TCP Server started on port {server.port}")
    print(f"📡 Listening on 0.0.0.0:{server.port}")
    print(f"💾 Database logging: {'ENABLED' if DB_AVAILABLE else 'DISABLED'}")
    print("=" * 60)
    print("\n👀 Monitoring connections and telemetry...")
    print("   Press Ctrl+C to stop\n")
    
    # Avvia il monitor connessioni
    monitor_thread = threading.Thread(target=connection_monitor, args=(server,), daemon=True)
    monitor_thread.start()
    
    try:
        # Loop principale - attende shutdown signal
        while not shutdown_flag:
            time.sleep(1)
    except KeyboardInterrupt:
        if not shutdown_flag:
            print("\n🛑 Keyboard interrupt received.")
            shutdown_flag = True
    
    # Shutdown graceful
    if not shutdown_flag:
        print("\n🛑 Stopping server...")
    
    server.stop()
    
    # Pulisci database alla chiusura
    if DB_AVAILABLE:
        try:
            db = get_db()
            # Segna tutti i dispositivi come disconnessi alla chiusura
            with db.lock:
                with sqlite3.connect(str(db.db_path)) as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        UPDATE devices 
                        SET status = 'disconnected'
                        WHERE status = 'connected'
                    """)
                    disconnected_count = cursor.rowcount
                    conn.commit()
            
            if disconnected_count > 0:
                print(f"🧹 Database cleanup: {disconnected_count} dispositivi disconnessi")
        except Exception as e:
            print(f"⚠️ Errore pulizia database: {e}")
    
    print("✅ Daemon stopped.")
