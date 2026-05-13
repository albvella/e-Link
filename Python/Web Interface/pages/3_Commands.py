"""
e-Link Web Interface - Command Center
Interfaccia per invio comandi e configurazione dispositivi
"""

import streamlit as st
import sys
from pathlib import Path

# Aggiungi path per import moduli
sys.path.append(str(Path(__file__).parent.parent.parent))

from eLink_TCP_Interface import eLinkTCPServer
from db_manager import get_db

# Configurazione pagina
st.set_page_config(
    page_title="Centro Comandi",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Centro Comandi")

# Verifica dispositivo selezionato
if 'selected_device' not in st.session_state or st.session_state['selected_device'] is None:
    st.warning("⚠️ Nessun dispositivo selezionato")
    st.info("Torna alla home page e seleziona un dispositivo dalla sidebar")
    st.stop()

device_id = st.session_state['selected_device']
st.subheader(f"Device {device_id}")

# Inizializza database
db = get_db()

# Recupera socket del dispositivo (TODO: implementare funzione per ottenere socket da device_id)
# Per ora mostriamo l'interfaccia anche senza connessione diretta al server TCP

st.markdown("---")

# Tabs per categorie comandi
tab1, tab2, tab3 = st.tabs(["🔧 Comandi Base", "⚙️ Configurazione", "📡 Comandi Avanzati"])

with tab1:
    st.subheader("Comandi Base")
    st.markdown("Comandi rapidi per il controllo del dispositivo")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏁 Start Misura (SRT)", use_container_width=True):
            st.info("Comando SRT inviato")
            st.warning("⚠️ Funzionalità in fase di sviluppo - Richiede integrazione con TCP server")
            # TODO: tcp_server.send_command(client_sock, "SRT")
    
    with col2:
        if st.button("⏹️ Idle (IDL)", use_container_width=True):
            st.info("Comando IDL inviato")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
            # TODO: tcp_server.send_command(client_sock, "IDL")
    
    with col3:
        if st.button("🏓 Ping (PNG)", use_container_width=True):
            st.info("Comando PNG inviato")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
            # TODO: tcp_server.send_command(client_sock, "PNG")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Richiedi Misura (MSR)", use_container_width=True):
            st.info("Comando MSR inviato - Attendi ricezione misura...")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
            # TODO: tcp_server.send_command(client_sock, "MSR")
    
    with col2:
        if st.button("🔄 Reset (RST)", use_container_width=True):
            if st.checkbox("Conferma reset dispositivo", key="confirm_reset"):
                st.error("Comando RST inviato - Dispositivo in reset")
                st.warning("⚠️ Funzionalità in fase di sviluppo")
                # TODO: tcp_server.send_command(client_sock, "RST")
            else:
                st.warning("Seleziona la checkbox di conferma")
    
    st.markdown("---")
    
    st.subheader("Controllo Invio Dati")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("▶️ Avvia Invio Log (SND,1)", use_container_width=True):
            st.success("Invio log abilitato")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
            # TODO: tcp_server.send_command(client_sock, "SND", cfg_var="1")
    
    with col2:
        if st.button("⏸️ Ferma Invio Log (SND,0)", use_container_width=True):
            st.info("Invio log disabilitato")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
            # TODO: tcp_server.send_command(client_sock, "SND", cfg_var="0")

with tab2:
    st.subheader("Configurazione Parametri")
    st.markdown("Modifica i parametri di configurazione del dispositivo")
    
    # Sezione parametri base
    st.markdown("### Parametri Campionamento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        samp_freq = st.selectbox(
            "Frequenza Campionamento [Hz]",
            options=[800, 1600],
            index=0,
            help="Frequenza di acquisizione dati"
        )
        
        if st.button("💾 Imposta SAMP_FREQ", key="set_samp_freq"):
            st.success(f"Frequenza impostata a {samp_freq} Hz")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
            # TODO: tcp_server.send_command(client_sock, "SET", cfg_var="SAMP_FREQ", cfg_val=str(samp_freq))
    
    with col2:
        buffer_secs = st.slider(
            "Buffering [secondi]",
            min_value=5,
            max_value=30,
            value=10,
            help="Durata buffer circolare per acquisizione"
        )
        
        if st.button("💾 Imposta BUFFER_SECS", key="set_buffer"):
            st.success(f"Buffer impostato a {buffer_secs} secondi")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
            # TODO: tcp_server.send_command(client_sock, "SET", cfg_var="BUFFER_SECS", cfg_val=str(buffer_secs))
    
    st.markdown("---")
    
    # Sezione timeout e log
    st.markdown("### Timeout e Logging")
    
    col1, col2 = st.columns(2)
    
    with col1:
        conn_timeout = st.number_input(
            "Connection Timeout [ms]",
            min_value=1000,
            max_value=60000,
            value=5000,
            step=1000,
            help="Timeout connessione TCP"
        )
        
        if st.button("💾 Imposta CONN_TIMEOUT", key="set_timeout"):
            st.success(f"Timeout impostato a {conn_timeout} ms")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
    
    with col2:
        log_period = st.number_input(
            "Log Period [ms]",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            help="Periodo invio log telemetria"
        )
        
        if st.button("💾 Imposta LOG_PERIOD", key="set_log_period"):
            st.success(f"Log period impostato a {log_period} ms")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
    
    st.markdown("---")
    
    # Sezione soglie
    st.markdown("### Soglie Rilevamento")
    
    hammer_th = st.number_input(
        "Hammer Threshold [ADC counts]",
        min_value=0,
        max_value=4095,
        value=500,
        help="Soglia rilevamento colpo d'ariete"
    )
    
    if st.button("💾 Imposta HAMMER_TH", key="set_hammer"):
        st.success(f"Soglia hammer impostata a {hammer_th}")
        st.warning("⚠️ Funzionalità in fase di sviluppo")
    
    st.markdown("#### Soglie Alta/Bassa per Ora del Giorno")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        hour_idx = st.selectbox("Ora", options=list(range(24)), index=12, key="hour_select")
    
    with col2:
        high_th = st.number_input(
            "High Threshold [ADC]",
            min_value=0,
            max_value=4095,
            value=3000,
            key="high_th_input"
        )
        
        if st.button("💾 Imposta HIGH_TH", key="set_high"):
            st.success(f"HIGH_TH[{hour_idx}] = {high_th}")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
            # TODO: tcp_server.send_command(client_sock, "SET", cfg_var="HIGH_TH", cfg_idx=hour_idx, cfg_val=str(high_th))
    
    with col3:
        low_th = st.number_input(
            "Low Threshold [ADC]",
            min_value=0,
            max_value=4095,
            value=500,
            key="low_th_input"
        )
        
        if st.button("💾 Imposta LOW_TH", key="set_low"):
            st.success(f"LOW_TH[{hour_idx}] = {low_th}")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
            # TODO: tcp_server.send_command(client_sock, "SET", cfg_var="LOW_TH", cfg_idx=hour_idx, cfg_val=str(low_th))

with tab3:
    st.subheader("Comandi Avanzati")
    st.markdown("Configurazione avanzata e OTA")
    
    st.markdown("### 📡 Connessione TCP")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tcp_ip = st.text_input(
            "TCP Server IP",
            value="192.168.1.100",
            help="Indirizzo IP server TCP"
        )
        
        if st.button("💾 Imposta TCP_IP", key="set_tcp_ip"):
            st.success(f"TCP IP impostato a {tcp_ip}")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
            # TODO: tcp_server.send_command(client_sock, "SET", cfg_var="TCP_IP", cfg_val=tcp_ip)
    
    with col2:
        tcp_port = st.text_input(
            "TCP Server Port",
            value="21001",
            help="Porta server TCP"
        )
        
        if st.button("💾 Imposta TCP_PORT", key="set_tcp_port"):
            st.success(f"TCP Port impostato a {tcp_port}")
            st.warning("⚠️ Funzionalità in fase di sviluppo")
            # TODO: tcp_server.send_command(client_sock, "SET", cfg_var="TCP_PORT", cfg_val=tcp_port)
    
    st.markdown("---")
    
    # OTA Update
    st.markdown("### 🔄 OTA Update")
    st.warning("⚠️ Attenzione: l'aggiornamento OTA richiede diversi minuti e il dispositivo sarà offline durante il processo")
    
    ota_file = st.file_uploader("Seleziona file firmware (.bin)", type=["bin"], key="ota_file")
    
    if ota_file:
        st.info(f"File selezionato: {ota_file.name} ({ota_file.size / 1024:.2f} KB)")
        
        if st.button("🚀 Avvia OTA Update", key="start_ota"):
            st.error("⚠️ FUNZIONALITÀ OTA IN FASE DI SVILUPPO")
            st.info("""
            Procedura OTA:
            1. Salva file firmware temporaneamente
            2. Invia comando OTA al dispositivo
            3. Trasferisci file in chunk (512 bytes)
            4. Verifica CRC32
            5. Applica aggiornamento
            6. Riavvia dispositivo
            
            Tempo stimato: ~5-10 minuti per 256 KB
            """)
            # TODO: Implementare OTA routine
    
    st.markdown("---")
    
    # Lettura configurazione
    st.markdown("### 📖 Lettura Configurazione")
    
    get_var = st.selectbox(
        "Variabile da leggere:",
        options=["DEVICE_ID", "SAMP_FREQ", "BUFFER_SECS", "CONN_TIMEOUT", 
                 "LOG_PERIOD", "HAMMER_TH", "TCP_IP", "TCP_PORT"],
        key="get_var"
    )
    
    if st.button("📖 Leggi Valore", key="get_value"):
        st.info(f"Lettura {get_var}...")
        st.warning("⚠️ Funzionalità in fase di sviluppo")
        # TODO: tcp_server.send_command(client_sock, "GET", cfg_var=get_var)

# Info box
st.markdown("---")
st.info("""
### ℹ️ Note Implementazione

**Stato attuale:**
- ✅ Interfaccia utente completa
- ⚠️ Integrazione con TCP server in fase di sviluppo

**Prossimi step:**
1. Implementare funzione per recuperare socket client da device_id
2. Collegare pulsanti alle funzioni `send_command()` del TCP server
3. Gestire risposte asincrone dai dispositivi
4. Implementare callback per aggiornamento UI dopo risposta

**Come procedere:**
Il TCP server è già funzionante e gestisce i comandi. Serve solo collegare questa
interfaccia web al server esistente tramite import diretto o comunicazione locale.
""")
