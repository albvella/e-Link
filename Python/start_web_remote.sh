#!/bin/bash
# Script per avviare Dash Web Interface accessibile da remoto
# Uso: ./start_web_remote.sh
# Convertito da Streamlit a Dash

echo "🚀 Avvio e-Link Web Interface - Dash (Remote Access)"
echo "====================================================="
echo ""

# Ottieni IP del server
SERVER_IP=$(hostname -I | awk '{print $1}')

# Porta Dash (cambiata a 21002)
DASH_PORT=21002

echo "📡 Server IP: $SERVER_IP"
echo "🌐 URL: http://$SERVER_IP:$DASH_PORT"
echo ""
echo "⚠️  Assicurati che:"
echo "   - Il firewall permetta connessioni sulla porta $DASH_PORT"
echo "   - eLink_Client_Control.py sia già in esecuzione"
echo ""
echo "🔄 Convertito da Streamlit a Dash per migliori performance e flessibilità"
echo ""
echo "Avvio in corso..."
echo ""

# Vai nella cartella Web Interface e avvia Dash
cd "Web Interface"
python3 dash_app.py
