"""
e-Link Web Interface - Main Dashboard
Visualizzazione stato dispositivi e navigazione principale
"""

import streamlit as st
import sys
from pathlib import Path

# Aggiungi path per import moduli
sys.path.append(str(Path(__file__).parent.parent))

from db_manager import get_db

# Configurazione pagina
st.set_page_config(
    page_title="e-Link Control Panel",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titolo principale
st.title("🔗 e-Link Control Panel")
st.markdown("---")

# Inizializza database
db = get_db()

# Sidebar: Selezione dispositivo
with st.sidebar:
    st.header("📱 Dispositivi")
    
    # Recupera dispositivi connessi
    devices = db.get_connected_devices()
    
    if devices:
        st.success(f"✅ {len(devices)} dispositivo/i connesso/i")
        
        # Selezione dispositivo
        device_options = {f"Device {d['device_id']}": d['device_id'] for d in devices}
        selected_device_name = st.selectbox(
            "Seleziona dispositivo:",
            options=list(device_options.keys())
        )
        selected_device = device_options[selected_device_name]
        
        # Salva in session state
        st.session_state['selected_device'] = selected_device
        
        # Info dispositivo selezionato
        device_info = next((d for d in devices if d['device_id'] == selected_device), None)
        if device_info:
            st.info(f"""
            **Device ID:** {device_info['device_id']}  
            **IP:** {device_info['ip_address']}  
            **Last Seen:** {device_info['last_seen']}
            """)
    else:
        st.warning("⚠️ Nessun dispositivo connesso")
        st.session_state['selected_device'] = None
    
    st.markdown("---")
    
    # Statistiche database
    st.subheader("📊 Statistiche")
    stats = db.get_db_stats()
    st.metric("Record totali", stats['total_records'])
    st.metric("Dispositivi", stats['devices_count'])
    
    # Pulizia manuale database
    if st.button("🧹 Pulisci dati vecchi"):
        deleted = db.cleanup_old_data()
        st.success(f"Eliminati {deleted} record")

# Main content
if 'selected_device' in st.session_state and st.session_state['selected_device']:
    device_id = st.session_state['selected_device']
    
    st.header(f"📊 Dashboard Device {device_id}")
    
    # Recupera ultimo record telemetria
    latest = db.get_latest_telemetry(device_id)
    
    if latest:
        # Timestamp ultimo aggiornamento
        st.caption(f"Ultimo aggiornamento: {latest['timestamp']}")
        
        # Metriche principali in colonne
        st.subheader("⚡ Tensioni")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Vbatt",
                value=f"{latest['vbatt']:.2f} V" if latest['vbatt'] else "N/A"
            )
        
        with col2:
            st.metric(
                label="V1",
                value=f"{latest['v1']:.2f} V" if latest['v1'] else "N/A"
            )
        
        with col3:
            st.metric(
                label="V2",
                value=f"{latest['v2']:.2f} V" if latest['v2'] else "N/A"
            )
        
        with col4:
            st.metric(
                label="V3",
                value=f"{latest['v3']:.2f} V" if latest['v3'] else "N/A"
            )
        
        st.subheader("🔋 Correnti")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="I1",
                value=f"{latest['i1']:.3f} A" if latest['i1'] else "N/A"
            )
        
        with col2:
            st.metric(
                label="I2",
                value=f"{latest['i2']:.3f} A" if latest['i2'] else "N/A"
            )
        
        with col3:
            st.metric(
                label="I3",
                value=f"{latest['i3']:.3f} A" if latest['i3'] else "N/A"
            )
        
        st.subheader("📊 Altri Sensori")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                label="🌡️ Temperatura",
                value=f"{latest['temperature']:.1f} °C" if latest['temperature'] else "N/A"
            )
        
        with col2:
            st.metric(
                label="📈 Pressione",
                value=f"{latest['pressure']:.2f} bar" if latest['pressure'] else "N/A"
            )
        
        st.markdown("---")
        
        # Link rapidi alle sezioni
        st.subheader("🚀 Azioni Rapide")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📊 Visualizza Telemetria", use_container_width=True):
                st.switch_page("pages/1_Telemetry.py")
        
        with col2:
            if st.button("📁 Visualizza Misure", use_container_width=True):
                st.switch_page("pages/2_Measures.py")
        
        with col3:
            if st.button("⚙️ Invia Comandi", use_container_width=True):
                st.switch_page("pages/3_Commands.py")
        
    else:
        st.warning("Nessun dato telemetria disponibile per questo dispositivo.")
        st.info("I dati appariranno qui appena il dispositivo invierà il primo log.")

else:
    # Nessun dispositivo selezionato
    st.info("👈 Seleziona un dispositivo dalla sidebar per iniziare")
    
    st.markdown("""
    ## Benvenuto nel Control Panel e-Link
    
    Questa interfaccia ti permette di:
    
    - 📊 **Visualizzare telemetria real-time** (pressione, flusso, accelerazioni)
    - 📁 **Analizzare misure complete** salvate su file binario
    - ⚙️ **Inviare comandi** ai dispositivi connessi
    - 🔧 **Configurare parametri** dei sensori
    
    ### Come iniziare:
    
    1. Assicurati che il **TCP Server** sia attivo
    2. Connetti un dispositivo e-Link alla rete
    3. Seleziona il dispositivo dalla **sidebar**
    4. Naviga tra le diverse sezioni usando il menu
    
    ### Note:
    
    - I dati telemetria sono mantenuti per **1 ora** (buffer circolare)
    - Le misure complete sono salvate in `data/measures/`
    - Il database è aggiornato automaticamente ogni volta che arriva un log
    """)

# Footer
st.markdown("---")
st.caption("e-Link Control Panel v1.0 | Developed for Smart_Joint Project")
