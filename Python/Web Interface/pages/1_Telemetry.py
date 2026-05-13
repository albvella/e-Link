"""
e-Link Web Interface - Telemetry Real-Time
Visualizzazione plot real-time di pressione, flusso e accelerazioni
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sys
from pathlib import Path
import time

# Aggiungi path per import moduli
sys.path.append(str(Path(__file__).parent.parent.parent))

from db_manager import get_db

# Configurazione pagina
st.set_page_config(
    page_title="Telemetria Real-Time",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Telemetria Real-Time")

# Verifica dispositivo selezionato
if 'selected_device' not in st.session_state or st.session_state['selected_device'] is None:
    st.warning("⚠️ Nessun dispositivo selezionato")
    st.info("Torna alla home page e seleziona un dispositivo dalla sidebar")
    st.stop()

device_id = st.session_state['selected_device']
st.subheader(f"Device {device_id}")

# Inizializza database
db = get_db()

# Controlli
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    # Selezione intervallo temporale
    time_range = st.select_slider(
        "Intervallo temporale:",
        options=["1 minuto", "10 minuti", "1 ora"],
        value="10 minuti"
    )

with col2:
    # Auto-refresh
    auto_refresh = st.checkbox("Auto-refresh", value=True)

with col3:
    # Refresh manuale
    if st.button("🔄 Aggiorna"):
        st.rerun()

# Converti intervallo in minuti
time_range_map = {
    "1 minuto": 1,
    "10 minuti": 10,
    "1 ora": 60
}
minutes = time_range_map[time_range]

st.markdown("---")

# Placeholder per plot e metriche
plot_placeholder = st.empty()
metrics_placeholder = st.empty()

# Loop per auto-refresh
refresh_counter = 0
max_refreshes = 300  # Max 5 minuti di auto-refresh (300 x 1s)

while auto_refresh and refresh_counter < max_refreshes:
    with plot_placeholder.container():
        # Recupera dati telemetria
        data = db.get_telemetry(device_id, minutes=minutes)
        
        if data:
            # Converti in DataFrame
            df = pd.DataFrame(data)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            # Crea plot con subplots
            fig = make_subplots(
                rows=3, cols=1,
                subplot_titles=("Pressione [bar]", "Flusso [L/s]", "Accelerazioni [mg]"),
                vertical_spacing=0.08,
                row_heights=[0.33, 0.33, 0.34]
            )
            
            # Plot 1: Pressione
            fig.add_trace(
                go.Scatter(
                    x=df['timestamp'],
                    y=df['pressure'],
                    name='Pressione',
                    line=dict(color='#1f77b4', width=2),
                    mode='lines'
                ),
                row=1, col=1
            )
            
            # Plot 2: Flusso
            fig.add_trace(
                go.Scatter(
                    x=df['timestamp'],
                    y=df['flow'],
                    name='Flusso',
                    line=dict(color='#2ca02c', width=2),
                    mode='lines'
                ),
                row=2, col=1
            )
            
            # Plot 3: Accelerazioni (3 tracce)
            fig.add_trace(
                go.Scatter(
                    x=df['timestamp'],
                    y=df['ax'],
                    name='Ax',
                    line=dict(color='#d62728', width=1.5),
                    mode='lines'
                ),
                row=3, col=1
            )
            fig.add_trace(
                go.Scatter(
                    x=df['timestamp'],
                    y=df['ay'],
                    name='Ay',
                    line=dict(color='#2ca02c', width=1.5),
                    mode='lines'
                ),
                row=3, col=1
            )
            fig.add_trace(
                go.Scatter(
                    x=df['timestamp'],
                    y=df['az'],
                    name='Az',
                    line=dict(color='#1f77b4', width=1.5),
                    mode='lines'
                ),
                row=3, col=1
            )
            
            # Layout plot
            fig.update_layout(
                height=900,
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
            
            # Assi
            fig.update_xaxes(title_text="Tempo", row=3, col=1)
            fig.update_yaxes(title_text="Pressione [bar]", row=1, col=1)
            fig.update_yaxes(title_text="Flusso [L/s]", row=2, col=1)
            fig.update_yaxes(title_text="Accelerazione [mg]", row=3, col=1)
            
            # Mostra plot
            st.plotly_chart(fig, use_container_width=True)
            
            # Statistiche
            st.markdown("### 📈 Statistiche")
            stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
            
            with stat_col1:
                st.metric("Campioni", len(df))
                st.metric("Pressione media", f"{df['pressure'].mean():.2f} bar")
                st.metric("Pressione max", f"{df['pressure'].max():.2f} bar")
            
            with stat_col2:
                st.metric("Flusso medio", f"{df['flow'].mean():.2f} L/s")
                st.metric("Flusso max", f"{df['flow'].max():.2f} L/s")
                st.metric("Flusso min", f"{df['flow'].min():.2f} L/s")
            
            with stat_col3:
                st.metric("Ax media", f"{df['ax'].mean():.2f} mg")
                st.metric("Ay media", f"{df['ay'].mean():.2f} mg")
                st.metric("Az media", f"{df['az'].mean():.2f} mg")
            
            with stat_col4:
                latest = df.iloc[-1]
                st.metric("Temperatura", f"{latest['temperature']:.1f} °C")
                st.metric("Vbatt", f"{latest['vbatt']:.2f} V")
                st.metric("I1 + I2 + I3", f"{latest['i1'] + latest['i2'] + latest['i3']:.3f} A")
            
        else:
            st.warning(f"Nessun dato disponibile negli ultimi {time_range.lower()}")
            st.info("I dati appariranno qui appena il dispositivo invierà dei log")
    
    # Metriche real-time in tempo reale
    with metrics_placeholder.container():
        latest = db.get_latest_telemetry(device_id)
        if latest:
            st.markdown("---")
            st.markdown("### ⚡ Valori Correnti")
            
            # Tensioni
            st.markdown("**Tensioni:**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Vbatt", f"{latest['vbatt']:.2f} V" if latest['vbatt'] else "N/A")
            with col2:
                st.metric("V1", f"{latest['v1']:.2f} V" if latest['v1'] else "N/A")
            with col3:
                st.metric("V2", f"{latest['v2']:.2f} V" if latest['v2'] else "N/A")
            with col4:
                st.metric("V3", f"{latest['v3']:.2f} V" if latest['v3'] else "N/A")
            
            # Correnti
            st.markdown("**Correnti:**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("I1", f"{latest['i1']:.3f} A" if latest['i1'] else "N/A")
            with col2:
                st.metric("I2", f"{latest['i2']:.3f} A" if latest['i2'] else "N/A")
            with col3:
                st.metric("I3", f"{latest['i3']:.3f} A" if latest['i3'] else "N/A")
            with col4:
                st.metric("Totale", f"{(latest['i1'] + latest['i2'] + latest['i3']):.3f} A")
            
            # Temperatura
            st.markdown("**Altro:**")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Temperatura", f"{latest['temperature']:.1f} °C" if latest['temperature'] else "N/A")
            with col2:
                st.caption(f"Aggiornato: {latest['timestamp']}")
    
    # Incrementa counter e attendi
    refresh_counter += 1
    if auto_refresh:
        time.sleep(1)  # Refresh ogni secondo
        st.rerun()
    else:
        break

# Se non è auto-refresh, mostra comunque una volta
if not auto_refresh:
    # Recupera dati telemetria
    data = db.get_telemetry(device_id, minutes=minutes)
    
    if data:
        # Converti in DataFrame
        df = pd.DataFrame(data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Crea plot con subplots
        fig = make_subplots(
            rows=3, cols=1,
            subplot_titles=("Pressione [bar]", "Flusso [L/s]", "Accelerazioni [mg]"),
            vertical_spacing=0.08,
            row_heights=[0.33, 0.33, 0.34]
        )
        
        # Plot 1: Pressione
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['pressure'],
                name='Pressione',
                line=dict(color='#1f77b4', width=2),
                mode='lines'
            ),
            row=1, col=1
        )
        
        # Plot 2: Flusso
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['flow'],
                name='Flusso',
                line=dict(color='#2ca02c', width=2),
                mode='lines'
            ),
            row=2, col=1
        )
        
        # Plot 3: Accelerazioni (3 tracce)
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['ax'],
                name='Ax',
                line=dict(color='#d62728', width=1.5),
                mode='lines'
            ),
            row=3, col=1
        )
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['ay'],
                name='Ay',
                line=dict(color='#2ca02c', width=1.5),
                mode='lines'
            ),
            row=3, col=1
        )
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['az'],
                name='Az',
                line=dict(color='#1f77b4', width=1.5),
                mode='lines'
            ),
            row=3, col=1
        )
        
        # Layout plot
        fig.update_layout(
            height=900,
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
        
        # Assi
        fig.update_xaxes(title_text="Tempo", row=3, col=1)
        fig.update_yaxes(title_text="Pressione [bar]", row=1, col=1)
        fig.update_yaxes(title_text="Flusso [L/s]", row=2, col=1)
        fig.update_yaxes(title_text="Accelerazione [mg]", row=3, col=1)
        
        # Mostra plot
        st.plotly_chart(fig, use_container_width=True)
        
        # Statistiche
        st.markdown("### 📈 Statistiche")
        stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
        
        with stat_col1:
            st.metric("Campioni", len(df))
            st.metric("Pressione media", f"{df['pressure'].mean():.2f} bar")
            st.metric("Pressione max", f"{df['pressure'].max():.2f} bar")
        
        with stat_col2:
            st.metric("Flusso medio", f"{df['flow'].mean():.2f} L/s")
            st.metric("Flusso max", f"{df['flow'].max():.2f} L/s")
            st.metric("Flusso min", f"{df['flow'].min():.2f} L/s")
        
        with stat_col3:
            st.metric("Ax media", f"{df['ax'].mean():.2f} mg")
            st.metric("Ay media", f"{df['ay'].mean():.2f} mg")
            st.metric("Az media", f"{df['az'].mean():.2f} mg")
        
        with stat_col4:
            latest = df.iloc[-1]
            st.metric("Temperatura", f"{latest['temperature']:.1f} °C")
            st.metric("Vbatt", f"{latest['vbatt']:.2f} V")
            st.metric("I Totale", f"{latest['i1'] + latest['i2'] + latest['i3']:.3f} A")
        
        # Metriche real-time
        st.markdown("---")
        st.markdown("### ⚡ Valori Correnti")
        
        latest_data = db.get_latest_telemetry(device_id)
        if latest_data:
            # Tensioni
            st.markdown("**Tensioni:**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Vbatt", f"{latest_data['vbatt']:.2f} V" if latest_data['vbatt'] else "N/A")
            with col2:
                st.metric("V1", f"{latest_data['v1']:.2f} V" if latest_data['v1'] else "N/A")
            with col3:
                st.metric("V2", f"{latest_data['v2']:.2f} V" if latest_data['v2'] else "N/A")
            with col4:
                st.metric("V3", f"{latest_data['v3']:.2f} V" if latest_data['v3'] else "N/A")
            
            # Correnti
            st.markdown("**Correnti:**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("I1", f"{latest_data['i1']:.3f} A" if latest_data['i1'] else "N/A")
            with col2:
                st.metric("I2", f"{latest_data['i2']:.3f} A" if latest_data['i2'] else "N/A")
            with col3:
                st.metric("I3", f"{latest_data['i3']:.3f} A" if latest_data['i3'] else "N/A")
            with col4:
                total_current = latest_data['i1'] + latest_data['i2'] + latest_data['i3']
                st.metric("Totale", f"{total_current:.3f} A")
            
            # Temperatura
            st.markdown("**Altro:**")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Temperatura", f"{latest_data['temperature']:.1f} °C" if latest_data['temperature'] else "N/A")
            with col2:
                st.caption(f"Aggiornato: {latest_data['timestamp']}")
    
    else:
        st.warning(f"Nessun dato disponibile negli ultimi {time_range.lower()}")
        st.info("I dati appariranno qui appena il dispositivo invierà dei log")
