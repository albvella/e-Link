#!/bin/bash
# Script per fermare tutti i server
# Uso: ./stop_all.sh

echo "🛑 Fermando e-Link System..."
echo ""

# Ferma Dash Web Interface
echo "1️⃣  Fermando Dash Web Interface..."
pkill -f "dash_app.py"
if [ $? -eq 0 ]; then
    echo "   ✅ Dash Web Interface arrestata"
else
    echo "   ⚠️  Nessuna istanza di Dash trovata"
fi

# Ferma TCP Server
echo "2️⃣  Fermando TCP Server..."
pkill -f "eLink_Server_Daemon.py"
if [ $? -eq 0 ]; then
    echo "   ✅ TCP Server arrestato"
else
    echo "   ⚠️  Nessuna istanza del TCP Server trovata"
fi

# Verifica e libera porta 21001 con utility Python
echo "3️⃣  Verificando porta 21001..."
python3 check_port.py --kill

echo ""
echo "✅ Sistema arrestato"
