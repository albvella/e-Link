"""
e-Link Telemetry Page - Dash Component
Visualizzazione grafici real-time convertita da Streamlit
"""

import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime, timedelta
import sys
from pathlib import Path

# Aggiungi path per import moduli
sys.path.append(str(Path(__file__).parent.parent))

def create_telemetry_layout():
    """Crea il layout per la pagina telemetria"""
    return html.Div([
        # Header
        html.H2([
            html.I(className="fas fa-chart-line me-2"),
            "Telemetria Real-Time"
        ], className="mb-4"),
        
        # Controlli
        dbc.Row([
            dbc.Col([
                html.Label("Intervallo temporale:", className="fw-bold"),
                dcc.RadioItems(
                    id="time-range-selector",
                    options=[
                        {"label": "1 minuto", "value": 1},
                        {"label": "10 minuti", "value": 10},
                        {"label": "1 ora", "value": 60}
                    ],
                    value=10,
                    className="mb-3",
                    inline=True
                )
            ], width=6),
            dbc.Col([
                dbc.Form([
                    dbc.Checkbox(
                        id="auto-refresh-checkbox",
                        label="Auto-refresh",
                        value=True,
                        className="me-3"
                    ),
                    dbc.Button(
                        [html.I(className="fas fa-sync-alt me-2"), "Aggiorna"],
                        id="refresh-button",
                        color="primary",
                        size="sm"
                    )
                ], className="d-flex align-items-center")
            ], width=6)
        ], className="mb-4"),
        
        html.Hr(),
        
        # Area grafici
        html.Div(id="telemetry-plots"),
        
        # Area statistiche
        html.Div(id="telemetry-stats"),
        
        # Store per device corrente
        dcc.Store(id="telemetry-device-store")
    ])

def register_telemetry_callbacks(app, db_manager):
    """Registra i callback per la pagina telemetria"""
    
    @app.callback(
        [Output("telemetry-plots", "children"),
         Output("telemetry-stats", "children")],
        [Input("time-range-selector", "value"),
         Input("refresh-button", "n_clicks"),
         Input("telemetry-device-store", "data"),
         Input("interval-component", "n_intervals")],
        prevent_initial_call=False
    )
    def update_telemetry_plots(time_range_minutes, refresh_clicks, device_data, n_intervals):
        if not device_data or not device_data.get("device_id"):
            return (
                dbc.Alert("Seleziona un dispositivo per visualizzare la telemetria", color="warning"),
                ""
            )
        
        device_id = device_data["device_id"]
        
        # Recupera dati dal database
        db = db_manager()
        data = db.get_telemetry(device_id, minutes=time_range_minutes)
        
        if not data:
            return (
                dbc.Alert([
                    html.I(className="fas fa-info-circle me-2"),
                    "Nessun dato telemetria disponibile per questo dispositivo nell'intervallo selezionato."
                ], color="info"),
                ""
            )
        
        # Converti in DataFrame
        df = pd.DataFrame(data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Crea grafici
        plots = create_telemetry_plots(df)
        
        # Crea statistiche
        stats = create_telemetry_stats(df)
        
        return plots, stats

def create_telemetry_plots(df):
    """Crea i grafici telemetria"""
    # Crea subplots
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
            mode='lines',
            hovertemplate='<b>Pressione</b><br>' +
                         'Tempo: %{x}<br>' +
                         'Valore: %{y:.2f} bar<extra></extra>'
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
            mode='lines',
            hovertemplate='<b>Flusso</b><br>' +
                         'Tempo: %{x}<br>' +
                         'Valore: %{y:.2f} L/s<extra></extra>'
        ),
        row=2, col=1
    )
    
    # Plot 3: Accelerazioni (3 tracce)
    colors = {'ax': '#d62728', 'ay': '#2ca02c', 'az': '#1f77b4'}
    labels = {'ax': 'Ax', 'ay': 'Ay', 'az': 'Az'}
    
    for axis in ['ax', 'ay', 'az']:
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df[axis],
                name=labels[axis],
                line=dict(color=colors[axis], width=1.5),
                mode='lines',
                hovertemplate=f'<b>{labels[axis]}</b><br>' +
                             'Tempo: %{x}<br>' +
                             'Valore: %{y:.2f} mg<extra></extra>'
            ),
            row=3, col=1
        )
    
    # Layout
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
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # Assi
    fig.update_xaxes(title_text="Tempo", row=3, col=1)
    fig.update_yaxes(title_text="Pressione [bar]", row=1, col=1)
    fig.update_yaxes(title_text="Flusso [L/s]", row=2, col=1)
    fig.update_yaxes(title_text="Accelerazione [mg]", row=3, col=1)
    
    # Stile griglia
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    return dcc.Graph(
        figure=fig,
        config={'displayModeBar': True, 'toImageButtonOptions': {'format': 'png'}}
    )

def create_telemetry_stats(df):
    """Crea le statistiche telemetria"""
    if df.empty:
        return ""
    
    latest = df.iloc[-1]
    
    return html.Div([
        html.H4([
            html.I(className="fas fa-chart-bar me-2"),
            "Statistiche"
        ], className="mb-3"),
        
        dbc.Row([
            # Statistiche generali
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("📊 Generali"),
                    dbc.CardBody([
                        html.P([html.Strong("Campioni: "), str(len(df))]),
                        html.P([html.Strong("Intervallo: "), 
                               f"{df['timestamp'].min().strftime('%H:%M:%S')} - {df['timestamp'].max().strftime('%H:%M:%S')}"])
                    ])
                ])
            ], width=3),
            
            # Statistiche pressione
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("💧 Pressione"),
                    dbc.CardBody([
                        html.P([html.Strong("Media: "), f"{df['pressure'].mean():.2f} bar"]),
                        html.P([html.Strong("Max: "), f"{df['pressure'].max():.2f} bar"]),
                        html.P([html.Strong("Min: "), f"{df['pressure'].min():.2f} bar"])
                    ])
                ])
            ], width=3),
            
            # Statistiche flusso
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("🌊 Flusso"),
                    dbc.CardBody([
                        html.P([html.Strong("Media: "), f"{df['flow'].mean():.2f} L/s"]),
                        html.P([html.Strong("Max: "), f"{df['flow'].max():.2f} L/s"]),
                        html.P([html.Strong("Min: "), f"{df['flow'].min():.2f} L/s"])
                    ])
                ])
            ], width=3),
            
            # Statistiche accelerazioni
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("📐 Accelerazioni"),
                    dbc.CardBody([
                        html.P([html.Strong("Ax media: "), f"{df['ax'].mean():.2f} mg"]),
                        html.P([html.Strong("Ay media: "), f"{df['ay'].mean():.2f} mg"]),
                        html.P([html.Strong("Az media: "), f"{df['az'].mean():.2f} mg"])
                    ])
                ])
            ], width=3)
        ], className="mb-4"),
        
        # Valori attuali
        html.H5("🔄 Valori Attuali", className="mb-3"),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("🌡️ Temperatura", className="text-warning"),
                        html.H4(f"{latest['temperature']:.1f} °C")
                    ])
                ])
            ], width=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("🔋 Tensione Batteria", className="text-primary"),
                        html.H4(f"{latest['vbatt']:.2f} V")
                    ])
                ])
            ], width=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("⚡ Corrente Totale", className="text-success"),
                        html.H4(f"{latest['i1'] + latest['i2'] + latest['i3']:.3f} A")
                    ])
                ])
            ], width=4)
        ])
    ])