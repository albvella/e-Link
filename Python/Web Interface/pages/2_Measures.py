"""
e-Link Web Interface - Measure Viewer
Visualizzazione misure complete da file .bin
"""

import streamlit as st
import sys
from pathlib import Path
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Aggiungi path per import moduli
sys.path.append(str(Path(__file__).parent.parent.parent))

from eLink_Decompress_Measure import eLink_Decompress_Measure

# Configurazione pagina
st.set_page_config(
    page_title="Visualizza Misure",
    page_icon="📁",
    layout="wide"
)

st.title("📁 Visualizza Misure Complete")

# Cartella misure
MEASURES_DIR = Path(__file__).parent.parent.parent / "data" / "measures"
MEASURES_DIR.mkdir(parents=True, exist_ok=True)

st.markdown("---")

# Tabs per selezione sorgente
tab1, tab2 = st.tabs(["📂 File Salvati", "📤 Upload File"])

with tab1:
    st.subheader("File salvati sul server")
    
    # Lista file .bin nella cartella
    bin_files = sorted([f.name for f in MEASURES_DIR.glob("*.bin")], reverse=True)
    
    if bin_files:
        selected_file = st.selectbox("Seleziona misura:", bin_files, key="saved_file")
        file_path = MEASURES_DIR / selected_file
        
        # Info file
        file_size = file_path.stat().st_size
        st.info(f"**File:** `{selected_file}`  \n**Dimensione:** {file_size / 1024:.2f} KB")
        
        load_button = st.button("📊 Visualizza Misura", key="load_saved")
    else:
        st.warning("Nessuna misura disponibile nella cartella `data/measures/`")
        st.info("Le misure ricevute tramite comando MSR verranno salvate qui automaticamente")
        file_path = None
        load_button = False

with tab2:
    st.subheader("Carica file dal tuo computer")
    
    uploaded_file = st.file_uploader("Carica file .bin", type=["bin"], key="upload_file")
    
    if uploaded_file:
        # Salva temporaneamente
        temp_path = Path("/tmp") / "temp_measure.bin"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())
        
        file_path = temp_path
        file_size = temp_path.stat().st_size
        st.info(f"**File:** `{uploaded_file.name}`  \n**Dimensione:** {file_size / 1024:.2f} KB")
        
        load_button = st.button("📊 Visualizza Misura", key="load_upload")
    else:
        file_path = None
        load_button = False

st.markdown("---")

# Decompressione e visualizzazione
if load_button and file_path:
    with st.spinner("Decompressione in corso..."):
        try:
            # Usa la classe esistente per decompressione
            decompressor = eLink_Decompress_Measure(str(file_path))
            
            # Parametri configurabili (TODO: leggere da config dispositivo)
            f = st.sidebar.number_input("Frequenza campionamento [Hz]", value=800, step=100)
            press_fullscale = st.sidebar.number_input("Fullscale pressione [bar]", value=50, step=10)
            
            # Calcola vettore tempo
            t = np.linspace(0, len(decompressor.ax_data) / f, len(decompressor.ax_data))
            
            # Converti dati
            pressure = np.array(decompressor.pressure_data) * press_fullscale / 4096
            
            # Flusso
            clock_freq = 80000000
            flow_data = np.array(decompressor.flow_data)
            with np.errstate(divide='ignore', invalid='ignore'):
                flow = np.where(flow_data != 0, clock_freq / flow_data, 0)
            
            # Accelerazioni
            ax = np.array(decompressor.ax_data) * 0.061
            ay = np.array(decompressor.ay_data) * 0.061
            az = np.array(decompressor.az_data) * 0.061
            
            # Crea plot interattivo
            fig = make_subplots(
                rows=3, cols=1,
                subplot_titles=("Pressione [bar]", "Flusso [L/s]", "Accelerazioni [mg]"),
                vertical_spacing=0.08,
                row_heights=[0.33, 0.33, 0.34]
            )
            
            # Plot 1: Pressione
            fig.add_trace(
                go.Scatter(
                    x=t[:len(pressure)],
                    y=pressure,
                    name='Pressione',
                    line=dict(color='#1f77b4', width=1),
                    mode='lines'
                ),
                row=1, col=1
            )
            
            # Plot 2: Flusso
            fig.add_trace(
                go.Scatter(
                    x=t[:len(flow)],
                    y=flow,
                    name='Flusso',
                    line=dict(color='#2ca02c', width=1),
                    mode='lines'
                ),
                row=2, col=1
            )
            
            # Plot 3: Accelerazioni
            fig.add_trace(
                go.Scatter(
                    x=t,
                    y=ax,
                    name='Ax',
                    line=dict(color='#d62728', width=1),
                    mode='lines'
                ),
                row=3, col=1
            )
            fig.add_trace(
                go.Scatter(
                    x=t,
                    y=ay,
                    name='Ay',
                    line=dict(color='#2ca02c', width=1),
                    mode='lines'
                ),
                row=3, col=1
            )
            fig.add_trace(
                go.Scatter(
                    x=t,
                    y=az,
                    name='Az',
                    line=dict(color='#1f77b4', width=1),
                    mode='lines'
                ),
                row=3, col=1
            )
            
            # Layout
            fig.update_layout(
                height=1000,
                showlegend=True,
                hovermode='x unified',
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                )
            )
            
            fig.update_xaxes(title_text="Tempo [s]", row=3, col=1)
            fig.update_yaxes(title_text="Pressione [bar]", row=1, col=1)
            fig.update_yaxes(title_text="Flusso [L/s]", row=2, col=1)
            fig.update_yaxes(title_text="Accelerazione [mg]", row=3, col=1)
            
            # Mostra plot
            st.plotly_chart(fig, use_container_width=True)
            
            # Statistiche
            st.markdown("### 📈 Statistiche Misura")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Durata", f"{t[-1]:.2f} s")
                st.metric("Campioni totali", len(pressure))
                st.metric("Freq. campionamento", f"{f} Hz")
            
            with col2:
                st.metric("Pressione Max", f"{pressure.max():.2f} bar")
                st.metric("Pressione Min", f"{pressure.min():.2f} bar")
                st.metric("Pressione Media", f"{pressure.mean():.2f} bar")
            
            with col3:
                st.metric("Flusso Max", f"{flow.max():.2f} L/s")
                st.metric("Flusso Min", f"{flow[flow > 0].min():.2f} L/s" if len(flow[flow > 0]) > 0 else "N/A")
                st.metric("Flusso Medio", f"{flow[flow > 0].mean():.2f} L/s" if len(flow[flow > 0]) > 0 else "N/A")
            
            with col4:
                st.metric("Acc Max (abs)", f"{max(abs(ax).max(), abs(ay).max(), abs(az).max()):.2f} mg")
                st.metric("Ax RMS", f"{np.sqrt(np.mean(ax**2)):.2f} mg")
                st.metric("Ay RMS", f"{np.sqrt(np.mean(ay**2)):.2f} mg")
            
            st.markdown("---")
            
            # Export CSV
            st.subheader("📥 Esporta Dati")
            
            # Prepara DataFrame
            csv_data = pd.DataFrame({
                'time': t[:len(pressure)],
                'pressure': pressure,
                'flow': flow[:len(pressure)],
                'ax': ax[:len(pressure)],
                'ay': ay[:len(pressure)],
                'az': az[:len(pressure)]
            })
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.download_button(
                    label="📥 Scarica CSV",
                    data=csv_data.to_csv(index=False),
                    file_name=f"{Path(file_path).stem}_decompressed.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            
            with col2:
                # Info decompressione
                compression_ratio = (len(pressure) * 2 + len(flow) * 4 + len(ax) * 2 * 3) / file_path.stat().st_size
                st.metric("Rapporto compressione", f"{compression_ratio:.1f}x")
            
        except Exception as e:
            st.error(f"❌ Errore nella decompressione: {e}")
            st.exception(e)

else:
    # Info introduttiva
    if not load_button:
        st.info("""
        ### Come visualizzare una misura:
        
        1. Seleziona un file salvato **oppure** carica un file dal tuo computer
        2. Clicca su **"Visualizza Misura"**
        3. Esplora i plot interattivi (zoom, pan, hover)
        4. Scarica i dati decodificati in formato CSV se necessario
        
        ### Formato file:
        
        - File binari compressi (`.bin`)
        - Compressione: ADPCM (pressione/accelerazioni) + RLE (flusso)
        - Rapporto di compressione tipico: **5-10x**
        
        ### Note:
        
        - I plot sono **interattivi**: usa il mouse per zoom/pan
        - L'hover sincronizzato mostra i valori su tutti i grafici
        - La frequenza di campionamento è configurabile dalla sidebar
        """)
