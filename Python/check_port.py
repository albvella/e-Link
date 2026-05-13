#!/usr/bin/env python3
"""
Utility per verificare e liberare la porta TCP 21001
Uso: python check_port.py [--kill]
"""
import socket
import sys
import subprocess
import argparse

def check_port_status(host='127.0.0.1', port=21001):
    """Controlla se la porta è in uso"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
            return False  # Porta libera
        except OSError:
            return True   # Porta occupata

def get_port_process(port=21001):
    """Trova il processo che usa la porta (Linux/macOS)"""
    try:
        # Linux/macOS
        result = subprocess.run(['lsof', '-Pi', f':{port}', '-sTCP:LISTEN'], 
                              capture_output=True, text=True)
        if result.returncode == 0 and result.stdout:
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:  # Header + process line
                parts = lines[1].split()
                return parts[1], parts[0]  # PID, command
    except FileNotFoundError:
        try:
            # Windows netstat fallback
            result = subprocess.run(['netstat', '-ano'], capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if f':{port}' in line and 'LISTENING' in line:
                    parts = line.split()
                    return parts[-1], "Unknown"  # PID, command
        except:
            pass
    return None, None

def kill_port_process(port=21001):
    """Termina il processo che usa la porta"""
    pid, cmd = get_port_process(port)
    if pid:
        try:
            subprocess.run(['kill', '-9', pid], check=True)
            print(f"✅ Processo {cmd} (PID: {pid}) terminato")
            return True
        except subprocess.CalledProcessError:
            try:
                # Windows fallback
                subprocess.run(['taskkill', '/PID', pid, '/F'], check=True)
                print(f"✅ Processo PID {pid} terminato")
                return True
            except:
                print(f"❌ Errore terminando processo PID {pid}")
                return False
    return False

def main():
    parser = argparse.ArgumentParser(description='Check and manage TCP port 21001')
    parser.add_argument('--kill', action='store_true', help='Kill process using the port')
    parser.add_argument('--port', type=int, default=21001, help='Port to check (default: 21001)')
    args = parser.parse_args()

    port = args.port
    print(f"🔍 Checking port {port}...")
    
    if check_port_status(port=port):
        print(f"⚠️  Port {port} is in use")
        
        pid, cmd = get_port_process(port)
        if pid:
            print(f"📍 Process: {cmd} (PID: {pid})")
            
            if args.kill:
                print(f"🔪 Terminating process...")
                if kill_port_process(port):
                    # Verifica se è stato liberato
                    if not check_port_status(port=port):
                        print(f"✅ Port {port} is now free")
                    else:
                        print(f"❌ Port {port} still in use")
                else:
                    print(f"❌ Failed to terminate process")
        else:
            print("❓ Could not identify process")
    else:
        print(f"✅ Port {port} is free")

if __name__ == "__main__":
    main()