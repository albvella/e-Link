#!/bin/bash
# Script unificato per e-Link System
# Avvia solo eLink_Server_Daemon - Dash si connette via database

echo "🚀 Avvio e-Link System Unificato"
echo "======================================"
echo ""

# Ottieni IP del server
SERVER_IP=$(hostname -I | awk '{print $1}')

echo "📡 Server IP: $SERVER_IP"
echo ""
echo "Verifica firewall Ubuntu:"
echo "  sudo ufw allow 21001/tcp  # TCP Server"  
echo "  sudo ufw allow 21002/tcp  # Web Interface (Dash)"
echo ""

# Directory base
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "📂 Working directory: $BASE_DIR"
echo ""

# Libera porta se necessario
echo "🔍 Verificando porta 21001..."
if python3 check_port.py --port 21001 | grep -q "is in use"; then
    echo "⚠️  Porta 21001 occupata. Liberando..."
    python3 check_port.py --port 21001 --kill
    sleep 2
fi

echo "=============================================="
echo "✅ Sistema avviato!"
echo ""
echo "📊 TCP Server: tcp://$SERVER_IP:21001"
echo "🌐 Dash Web Interface: http://$SERVER_IP:21002"
echo ""
echo "🔄 Architettura Database-Driven:"
echo "   - eLink_Server_Daemon: gestisce TCP + legge comandi da DB"
echo "   - Dash App: interfaccia web + scrive comandi su DB"
echo ""
echo "Per fermare: ./stop_all.sh"
echo "=============================================="
echo ""

# Avvia daemon con gestione comandi database integrata
cd "$BASE_DIR"
echo "🚀 Avvio eLink_Server_Daemon con gestione comandi..."
python3 eLink_Server_Daemon.py