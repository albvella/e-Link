"""
e-Link Measures Page - Dash Component
Visualizzazione misure da file .bin convertita da Streamlit
"""

import dash
from dash import dcc, html, Input, Output, State, callback, callback_context, ALL
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import base64
import io
import sys
from pathlib import Path

# Aggiungi path per import moduli
sys.path.append(str(Path(__file__).parent.parent))

def create_measures_layout():
    """Crea il layout per la pagina misure"""
    return html.Div([
        # Header
        html.H2([
            html.I(className="fas fa-folder me-2"),
            "Visualizza Misure Complete"
        ], className="mb-4"),
        
        # Tabs per selezione sorgente
        dbc.Tabs([
            dbc.Tab(
                label="📂 File Salvati",
                tab_id="saved-files",
                children=[
                    html.Div(id="saved-files-content", className="mt-3")
                ]
            ),
            dbc.Tab(
                label="📤 Upload File",
                tab_id="upload-file",
                children=[
                    html.Div(id="upload-content", className="mt-3")
                ]
            )
        ], id="measures-tabs", active_tab="saved-files"),
        
        html.Hr(),
        
        # Controlli per decompressione
        dbc.Row([
            dbc.Col([
                html.Label("Frequenza campionamento [Hz]:", className="fw-bold"),
                dbc.Input(
                    id="sampling-freq-input",
                    type="number",
                    value=800,
                    step=100,
                    min=100,
                    max=10000
                )
            ], width=6),
            dbc.Col([
                html.Label("Fullscale pressione [bar]:", className="fw-bold"),
                dbc.Input(
                    id="pressure-fullscale-input",
                    type="number",
                    value=50,
                    step=10,
                    min=1,
                    max=1000
                )
            ], width=6)
        ], className="mb-3"),
        
        # Pulsante visualizzazione
        dbc.Row([
            dbc.Col([
                dbc.Button(
                    [html.I(className="fas fa-chart-line me-2"), "Visualizza Misura"],
                    id="visualize-measure-btn",
                    color="primary",
                    size="lg",
                    disabled=True,
                    className="w-100"
                )
            ])
        ], className="mb-4"),
        
        # Area risultati
        html.Div(id="measure-results"),
        
        # Store per file selezionato
        dcc.Store(id="selected-file-store"),
        dcc.Store(id="uploaded-file-store")
    ])

def register_measures_callbacks(app, measures_dir):
    """Registra i callback per la pagina misure"""
    
    @app.callback(
        Output("saved-files-content", "children"),
        [Input("measures-tabs", "active_tab")]
    )
    def update_saved_files_list(active_tab):
        if active_tab != "saved-files":
            return ""
        
        # Lista file .bin nella cartella
        try:
            bin_files = sorted([f.name for f in Path(measures_dir).glob("*.bin")], reverse=True)
        except:
            bin_files = []
        
        if not bin_files:
            return dbc.Alert([
                html.I(className="fas fa-info-circle me-2"),
                "Nessuna misura disponibile nella cartella data/measures/. ",
                "Le misure ricevute tramite comando MSR verranno salvate qui automaticamente."
            ], color="info")
        
        # Lista file con info
        file_items = []
        for filename in bin_files[:10]:  # Mostra solo i primi 10
            try:
                file_path = Path(measures_dir) / filename
                file_size = file_path.stat().st_size
                file_items.append(
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.H6(filename, className="mb-1"),
                                    html.Small(f"Dimensione: {file_size / 1024:.2f} KB", className="text-muted")
                                ], width=8),
                                dbc.Col([
                                    dbc.Button(
                                        "Seleziona",
                                        id={"type": "select-file-btn", "index": filename},
                                        color="outline-primary",
                                        size="sm"
                                    )
                                ], width=4, className="d-flex align-items-center justify-content-end")
                            ])
                        ])
                    ], className="mb-2")
                )
            except:
                continue
        
        return html.Div(file_items)
    
    @app.callback(
        Output("upload-content", "children"),
        [Input("measures-tabs", "active_tab")]
    )
    def update_upload_content(active_tab):
        if active_tab != "upload-file":
            return ""
        
        return html.Div([
            html.H5("Carica file dal tuo computer"),
            dcc.Upload(
                id="upload-data",
                children=html.Div([
                    html.I(className="fas fa-cloud-upload-alt fa-2x mb-3"),
                    html.Br(),
                    "Trascina qui un file .bin oppure clicca per selezionarlo"
                ]),
                style={
                    'width': '100%',
                    'height': '200px',
                    'lineHeight': '200px',
                    'borderWidth': '2px',
                    'borderStyle': 'dashed',
                    'borderRadius': '10px',
                    'textAlign': 'center',
                    'margin': '10px',
                    'cursor': 'pointer'
                },
                multiple=False,
                accept=".bin"
            ),
            html.Div(id="upload-feedback")
        ])
    
    @app.callback(
        [Output("selected-file-store", "data"),
         Output("visualize-measure-btn", "disabled")],
        [Input({"type": "select-file-btn", "index": ALL}, "n_clicks")],
        [State({"type": "select-file-btn", "index": ALL}, "id")]
    )
    def handle_file_selection(n_clicks, ids):
        if not any(n_clicks) or not any(n_clicks):
            return {}, True
        
        # Trova quale bottone è stato cliccato
        ctx = callback_context
        if not ctx.triggered:
            return {}, True
        
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        button_data = eval(button_id)  # Parse JSON string to dict
        filename = button_data["index"]
        
        return {"filename": filename, "source": "saved"}, False
    
    @app.callback(
        [Output("uploaded-file-store", "data"),
         Output("upload-feedback", "children"),
         Output("visualize-measure-btn", "disabled", allow_duplicate=True)],
        [Input("upload-data", "contents")],
        [State("upload-data", "filename")],
        prevent_initial_call=True
    )
    def handle_file_upload(contents, filename):
        if not contents:
            return {}, "", True
        
        try:
            # Decodifica file
            content_type, content_string = contents.split(',')
            decoded = base64.b64decode(content_string)
            
            # Verifica che sia un file .bin
            if not filename.endswith('.bin'):
                return {}, dbc.Alert("Formato file non supportato. Solo file .bin sono accettati.", 
                                   color="danger"), True
            
            file_size = len(decoded)
            
            feedback = dbc.Alert([
                html.I(className="fas fa-check-circle me-2"),
                f"File caricato: {filename} ({file_size / 1024:.2f} KB)"
            ], color="success")
            
            return {"content": content_string, "filename": filename}, feedback, False
            
        except Exception as e:
            return {}, dbc.Alert(f"Errore nel caricamento: {str(e)}", color="danger"), True
    
    @app.callback(
        Output("measure-results", "children"),
        [Input("visualize-measure-btn", "n_clicks")],
        [State("selected-file-store", "data"),
         State("uploaded-file-store", "data"),
         State("sampling-freq-input", "value"),
         State("pressure-fullscale-input", "value"),
         State("measures-tabs", "active_tab")],
        prevent_initial_call=True
    )
    def visualize_measure(n_clicks, selected_file, uploaded_file, sampling_freq, pressure_fullscale, active_tab):
        if not n_clicks:
            return ""
        
        try:
            # Determina la sorgente del file
            if active_tab == "saved-files" and selected_file:
                file_path = Path(measures_dir) / selected_file["filename"]
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                filename = selected_file["filename"]
            elif active_tab == "upload-file" and uploaded_file:
                file_data = base64.b64decode(uploaded_file["content"])
                filename = uploaded_file["filename"]
            else:
                return dbc.Alert("Nessun file selezionato", color="warning")
            
            # Import decompressor (lazy import per evitare errori se modulo non disponibile)
            try:
                from eLink_Decompress_Measure import eLink_Decompress_Measure
            except ImportError:
                return dbc.Alert("Modulo eLink_Decompress_Measure non disponibile", color="danger")
            
            # Salva temporaneamente per decompressione
            temp_path = Path("/tmp") / "temp_measure.bin"
            temp_path.parent.mkdir(exist_ok=True)
            with open(temp_path, 'wb') as f:
                f.write(file_data)
            
            # Decompressione
            decompressor = eLink_Decompress_Measure(str(temp_path))
            
            # Calcola vettore tempo
            t = np.linspace(0, len(decompressor.ax_data) / sampling_freq, len(decompressor.ax_data))
            
            # Converti dati
            pressure = np.array(decompressor.pressure_data) * pressure_fullscale / 4096
            
            # Flusso
            clock_freq = 80000000
            flow_data = np.array(decompressor.flow_data)
            with np.errstate(divide='ignore', invalid='ignore'):
                flow = np.where(flow_data != 0, clock_freq / flow_data, 0)
            
            # Accelerazioni
            ax = np.array(decompressor.ax_data) * 0.061
            ay = np.array(decompressor.ay_data) * 0.061
            az = np.array(decompressor.az_data) * 0.061
            
            # Pulisci file temporaneo
            temp_path.unlink(missing_ok=True)
            
            # Crea grafici
            plots = create_measure_plots(t, pressure, flow, ax, ay, az)
            
            # Crea statistiche
            stats = create_measure_stats(t, pressure, flow, ax, ay, az, sampling_freq, len(file_data))
            
            return html.Div([plots, stats])
            
        except Exception as e:
            return dbc.Alert([
                html.I(className="fas fa-exclamation-circle me-2"),
                f"Errore nella decompressione: {str(e)}"
            ], color="danger")

def create_measure_plots(t, pressure, flow, ax, ay, az):
    """Crea i grafici delle misure"""
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
            x=t[:len(pressure)],
            y=pressure,
            name='Pressione',
            line=dict(color='#1f77b4', width=1),
            mode='lines',
            hovertemplate='<b>Pressione</b><br>' +
                         'Tempo: %{x:.3f} s<br>' +
                         'Valore: %{y:.2f} bar<extra></extra>'
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
            mode='lines',
            hovertemplate='<b>Flusso</b><br>' +
                         'Tempo: %{x:.3f} s<br>' +
                         'Valore: %{y:.2f} L/s<extra></extra>'
        ),
        row=2, col=1
    )
    
    # Plot 3: Accelerazioni
    colors = {'ax': '#d62728', 'ay': '#2ca02c', 'az': '#1f77b4'}
    labels = {'ax': 'Ax', 'ay': 'Ay', 'az': 'Az'}
    data = {'ax': ax, 'ay': ay, 'az': az}
    
    for axis in ['ax', 'ay', 'az']:
        fig.add_trace(
            go.Scatter(
                x=t,
                y=data[axis],
                name=labels[axis],
                line=dict(color=colors[axis], width=1),
                mode='lines',
                hovertemplate=f'<b>{labels[axis]}</b><br>' +
                             'Tempo: %{x:.3f} s<br>' +
                             'Valore: %{y:.2f} mg<extra></extra>'
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
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # Assi
    fig.update_xaxes(title_text="Tempo [s]", row=3, col=1)
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

def create_measure_stats(t, pressure, flow, ax, ay, az, sampling_freq, file_size):
    """Crea le statistiche delle misure"""
    # Calcola statistiche
    flow_nonzero = flow[flow > 0] if len(flow[flow > 0]) > 0 else [0]
    
    return html.Div([
        html.H4([
            html.I(className="fas fa-chart-bar me-2"),
            "Statistiche Misura"
        ], className="mb-4"),
        
        # Statistiche principali
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("⏱️ Temporali"),
                    dbc.CardBody([
                        html.P([html.Strong("Durata: "), f"{t[-1]:.2f} s"]),
                        html.P([html.Strong("Campioni: "), f"{len(pressure):,}"]),
                        html.P([html.Strong("Frequenza: "), f"{sampling_freq} Hz"])
                    ])
                ])
            ], width=3),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("💧 Pressione"),
                    dbc.CardBody([
                        html.P([html.Strong("Max: "), f"{pressure.max():.2f} bar"]),
                        html.P([html.Strong("Min: "), f"{pressure.min():.2f} bar"]),
                        html.P([html.Strong("Media: "), f"{pressure.mean():.2f} bar"])
                    ])
                ])
            ], width=3),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("🌊 Flusso"),
                    dbc.CardBody([
                        html.P([html.Strong("Max: "), f"{flow.max():.2f} L/s"]),
                        html.P([html.Strong("Min: "), f"{flow_nonzero.min():.2f} L/s"]),
                        html.P([html.Strong("Media: "), f"{flow_nonzero.mean():.2f} L/s"])
                    ])
                ])
            ], width=3),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("📐 Accelerazioni"),
                    dbc.CardBody([
                        html.P([html.Strong("Max (abs): "), f"{max(abs(ax).max(), abs(ay).max(), abs(az).max()):.2f} mg"]),
                        html.P([html.Strong("Ax RMS: "), f"{np.sqrt(np.mean(ax**2)):.2f} mg"]),
                        html.P([html.Strong("Ay RMS: "), f"{np.sqrt(np.mean(ay**2)):.2f} mg"])
                    ])
                ])
            ], width=3)
        ], className="mb-4"),
        
        # Export e compressione
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("📥 Esporta Dati"),
                    dbc.CardBody([
                        # Prepara CSV data
                        html.P("Prepara i dati per il download in formato CSV:"),
                        dbc.Button(
                            [html.I(className="fas fa-download me-2"), "Genera CSV"],
                            id="generate-csv-btn",
                            color="success",
                            className="w-100"
                        ),
                        html.Div(id="csv-download-area")
                    ])
                ])
            ], width=8),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("🗜️ Compressione"),
                    dbc.CardBody([
                        html.P([
                            html.Strong("File originale: "),
                            f"{file_size / 1024:.2f} KB"
                        ]),
                        html.P([
                            html.Strong("Dati non compressi: "),
                            f"{(len(pressure) * 2 + len(flow) * 4 + len(ax) * 2 * 3) / 1024:.2f} KB"
                        ]),
                        html.P([
                            html.Strong("Rapporto: "),
                            f"{(len(pressure) * 2 + len(flow) * 4 + len(ax) * 2 * 3) / file_size:.1f}x"
                        ])
                    ])
                ])
            ], width=4)
        ])
    ])

# Callback per generazione CSV
def register_csv_callback(app):
    @app.callback(
        Output("csv-download-area", "children"),
        [Input("generate-csv-btn", "n_clicks")],
        prevent_initial_call=True
    )
    def generate_csv_download(n_clicks):
        if not n_clicks:
            return ""
        
        return dbc.Alert([
            html.I(className="fas fa-info-circle me-2"),
            "Funzionalità CSV in fase di implementazione completa..."
        ], color="info")