#!/bin/bash
# Script completo per avviare entrambi i server
# Uso: ./start_all_remote.sh

echo "🚀 Avvio completo e-Link System (Remote Access)"
echo "==============================================="
echo ""

# Ottieni IP del server
SERVER_IP=$(hostname -I | awk '{print $1}')

# Porta Dash (cambiata a 21002)
DASH_PORT=21002

echo "📡 Server IP: $SERVER_IP"
echo ""
echo "Verifica firewall Ubuntu:"
echo "  sudo ufw allow 21001/tcp  # TCP Server"
echo "  sudo ufw allow $DASH_PORT/tcp  # Web Interface (Dash)"
echo ""

# Directory base (cartella Python dove si trova questo script)
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "📂 Working directory: $BASE_DIR"
echo ""

# Verifica se porta 21001 è libera
echo "🔍 Verificando porta 21001..."
if python3 check_port.py --port 21001 | grep -q "is in use"; then
    echo "⚠️  Porta 21001 occupata. Liberando..."
    python3 check_port.py --port 21001 --kill
    sleep 2
fi

# Avvia TCP Server in background (modalità daemon senza input interattivo)
echo "1️⃣  Avvio TCP Server..."
cd "$BASE_DIR"
python3 eLink_Server_Daemon.py &
TCP_PID=$!

echo "   ✅ TCP Server avviato (PID: $TCP_PID)"
echo ""

# Attendi 3 secondi per far partire il TCP server
sleep 3

# Avvia Dash Web Interface
echo "2️⃣  Avvio Dash Web Interface..."
cd "$BASE_DIR/Web Interface"

echo ""
echo "=============================================="
echo "✅ Sistema avviato con successo!"
echo ""
echo "📊 TCP Server: tcp://$SERVER_IP:21001"
echo "🌐 Dash Web Interface: http://$SERVER_IP:$DASH_PORT"
echo "💾 Command Queue: Database-driven"
echo ""
echo "🏗️ Architettura:"
echo "  e-Link Devices ←→ eLink_Server_Daemon ←→ Database ←→ Dash App"
echo ""
echo "Per fermare i server:"
echo "  kill $TCP_PID              # TCP Server"
echo "  pkill -f dash_app          # Dash Web Interface"
echo "  oppure: ./stop_all.sh"
echo ""
echo "=============================================="
echo ""

# Avvia Dash (foreground)
python3 dash_app.py

# Se Dash termina, ferma anche il TCP server
echo ""
echo "🛑 Fermando TCP Server..."
kill $TCP_PID 2>/dev/null
echo "✅ Sistema arrestato"
