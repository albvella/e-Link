"""
e-Link Web Interface - Dash Application
Interfaccia web convertita da Streamlit a Dash
"""

import dash
from dash import dcc, html, Input, Output, State, callback_context, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Aggiungi path per import moduli
current_dir = Path(__file__).resolve().parent
parent_dir = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(current_dir))
sys.path.insert(0, str(parent_dir))

from db_manager import get_db

# Modalità Database-Only (senza TCP server proprio)

# Database Command Interface per comunicare con daemon via DB
class DatabaseCommandInterface:
    """Interfaccia comandi via database - il daemon leggerà da qui"""
    
    def __init__(self):
        self.db = get_db()
    
    def get_connected_devices(self):
        """Ottiene dispositivi connessi dal database"""
        try:
            devices = self.db.get_connected_devices()
            device_ids = [d.get('device_id', 0) for d in devices if d.get('device_id')]
            # Dispositivi recuperati dal database
            return device_ids
        except Exception as e:
            print(f"❌ Errore lettura dispositivi: {e}")
            return []
    
    def send_command_to_device(self, device_id, command, *args):
        """Accoda comando nel database - daemon lo invierà"""
        try:
            # Prepara parametri se presenti
            parameters = ','.join(map(str, args)) if args else None
            
            # Accoda comando
            command_id = self.db.queue_command(
                device_id=device_id,
                command=command,
                parameters=parameters,
                source='web_interface'
            )
            
            # Comando accodato nel database
            return True
            
        except Exception as e:
            print(f"❌ Errore accodamento comando: {e}")
            return False
    
    def stop(self):
        """Nessuna pulizia necessaria per interfaccia DB"""
        pass

# Inizializza interfaccia comandi database
tcp_server = DatabaseCommandInterface()

# Definisci classi TCP server alternative
class TCPServerProxy:
    """Proxy per connettersi a un TCP server esistente"""
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 21001
    
    def get_connected_devices(self):
        # Per ora ritorna dispositivi di esempio
        # TODO: Implementare comunicazione con server esistente
        return [101, 102, 103]
    
    def send_command_to_device(self, device_id, command, *args):
        # Proxy al database command interface
        # TODO: Inviare comando al server esistente via socket
        return True
    
    def stop(self):
        pass

class MockTCPServer:
    """Server TCP mock quando non disponibile"""
    def get_connected_devices(self):
        return []
    def send_command_to_device(self, *args):
        return False
    def stop(self):
        pass

# Interfaccia comandi già inizializzata sopra con DatabaseCommandInterface

# Inizializza app Dash con Bootstrap
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
    suppress_callback_exceptions=True,
    title="e-Link Control Panel"
)

# Layout principale
app.layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H1([
                html.I(className="fas fa-link me-2"),
                "e-Link Control Panel"
            ], className="text-primary mb-0"),
            html.Hr()
        ])
    ]),
    
    # Contenuto principale
    dbc.Row([
        # Sidebar
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H4([
                        html.I(className="fas fa-mobile-alt me-2"),
                        "Dispositivi"
                    ], className="mb-0")
                ]),
                dbc.CardBody([
                    # Status dispositivi
                    html.Div(id="device-status"),
                    
                    # Selezione dispositivo
                    html.Div(id="device-selector"),
                    
                    html.Hr(),
                    
                    # Statistiche
                    html.H5([
                        html.I(className="fas fa-chart-bar me-2"),
                        "Statistiche"
                    ]),
                    html.Div(id="database-stats"),
                    
                    html.Hr(),
                    
                    # Pulizia database
                    dbc.Button(
                        [html.I(className="fas fa-broom me-2"), "Pulisci dati vecchi"],
                        id="cleanup-btn",
                        color="warning",
                        size="sm",
                        className="w-100"
                    ),
                    html.Div(id="cleanup-feedback")
                ])
            ])
        ], width=3),
        
        # Content area
        dbc.Col([
            # Navigation tabs
            dbc.Tabs([
                dbc.Tab(label="🏠 Dashboard", tab_id="dashboard"),
                dbc.Tab(label="📊 Telemetria", tab_id="telemetry"),
                dbc.Tab(label="📁 Misure", tab_id="measures"),
                dbc.Tab(label="⚙️ Comandi", tab_id="commands")
            ], id="tabs", active_tab="dashboard"),
            
            html.Hr(),
            
            # Content area
            html.Div(id="tab-content")
        ], width=9)
    ]),
    
    # Footer
    html.Hr(),
    html.Footer([
        html.P("e-Link Control Panel v2.0 | Convertito da Streamlit a Dash", 
               className="text-muted small text-center")
    ]),
    
    # Store per dati condivisi
    dcc.Store(id="selected-device-store"),
    dcc.Store(id="devices-store"),
    
    # Interval per aggiornamenti automatici
    dcc.Interval(
        id="interval-component",
        interval=10*1000,  # 10 secondi (ridotto per evitare troppi errori)
        n_intervals=0
    )
], fluid=True)

# Callback per aggiornare la lista dispositivi
@app.callback(
    [Output("device-status", "children"),
     Output("device-selector", "children"),
     Output("database-stats", "children"),
     Output("devices-store", "data")],
    [Input("interval-component", "n_intervals")],
    prevent_initial_call=False
)
def update_sidebar(n):
    try:
        db = get_db()
        
        # Ottieni dispositivi connessi dal TCP server
        try:
            connected_device_ids = tcp_server.get_connected_devices()
            devices = []
            for device_id in connected_device_ids:
                devices.append({
                    'device_id': device_id,
                    'status': 'connected',
                    'last_seen': datetime.now().isoformat()
                })
        except Exception as e:
            print(f"Errore get_connected_devices TCP: {e}")
            devices = []
        
        # Prova a ottenere statistiche con fallback
        try:
            stats = db.get_db_stats()
        except Exception as e:
            print(f"Errore get_db_stats: {e}")
            stats = {'total_records': 0, 'devices_count': 0}
        
        # Status dispositivi
        if devices:
            status = dbc.Alert([
                html.I(className="fas fa-check-circle me-2"),
                f"{len(devices)} dispositivo/i connesso/i"
            ], color="success", className="mb-3")
        else:
            status = dbc.Alert([
                html.I(className="fas fa-exclamation-triangle me-2"),
                "Nessun dispositivo connesso"
            ], color="warning", className="mb-3")
        
        # Selezione dispositivo
        if devices and len(devices) > 0:
            device_options = []
            for d in devices:
                try:
                    device_id = d.get('device_id', 'N/A')
                    device_options.append({"label": f"Device {device_id}", "value": device_id})
                except Exception as e:
                    print(f"Errore processando dispositivo: {e}")
                    continue
            
            if device_options:
                selector = [
                    html.Label("Seleziona dispositivo:", className="fw-bold"),
                    dcc.Dropdown(
                        id="device-dropdown",
                        options=device_options,
                        value=device_options[0]["value"] if device_options else None,
                        className="mb-3"
                    )
                ]
                
                # Info dispositivo corrente
                try:
                    device_info = devices[0]  # Primo dispositivo per default
                    device_details = dbc.Card([
                        dbc.CardBody([
                            html.P([html.Strong("Device ID: "), str(device_info.get('device_id', 'N/A'))], className="mb-1"),
                            html.P([html.Strong("IP: "), str(device_info.get('ip_address', 'N/A'))], className="mb-1"),
                            html.P([html.Strong("Last Seen: "), str(device_info.get('last_seen', 'N/A'))], className="mb-0")
                        ])
                    ], className="bg-light")
                    selector.append(device_details)
                except Exception as e:
                    print(f"Errore info dispositivo: {e}")
            else:
                selector = html.P("Errore caricamento dispositivi", className="text-muted")
        else:
            selector = html.P("Nessun dispositivo disponibile", className="text-muted")
        
        # Statistiche database
        try:
            stats_content = [
                dbc.Row([
                    dbc.Col([
                        html.H6("Record totali", className="text-muted mb-0"),
                        html.H5(str(stats.get('total_records', 0)), className="mb-0")
                    ])
                ], className="mb-2"),
                dbc.Row([
                    dbc.Col([
                        html.H6("Dispositivi", className="text-muted mb-0"),
                        html.H5(str(stats.get('devices_count', 0)), className="mb-0")
                    ])
                ])
            ]
        except Exception as e:
            print(f"Errore statistiche: {e}")
            stats_content = [
                html.P("Errore caricamento statistiche", className="text-muted")
            ]
        
        return status, selector, stats_content, devices
        
    except Exception as e:
        print(f"Errore generale callback sidebar: {e}")
        # Fallback in caso di errori
        error_status = dbc.Alert([
            html.I(className="fas fa-exclamation-circle me-2"),
            "Errore connessione database"
        ], color="danger", className="mb-3")
        
        error_selector = html.P("Database non disponibile", className="text-muted")
        error_stats = [html.P("Statistiche non disponibili", className="text-muted")]
        
        return error_status, error_selector, error_stats, []

# Callback per gestire selezione dispositivo
@app.callback(
    Output("selected-device-store", "data"),
    [Input("device-dropdown", "value")],
    prevent_initial_call=True
)
def update_selected_device(device_id):
    try:
        return {"device_id": device_id}
    except Exception as e:
        print(f"Errore selezione dispositivo: {e}")
        return {"device_id": None}

# Callback per pulizia database
@app.callback(
    Output("cleanup-feedback", "children"),
    [Input("cleanup-btn", "n_clicks")],
    prevent_initial_call=True
)
def cleanup_database(n_clicks):
    try:
        if n_clicks:
            db = get_db()
            deleted = db.cleanup_old_data()
            return dbc.Alert(f"Eliminati {deleted} record", color="success", dismissable=True)
        return ""
    except Exception as e:
        print(f"Errore pulizia database: {e}")
        return dbc.Alert("Errore durante la pulizia", color="danger", dismissable=True)

# Callback principale per il contenuto delle tabs
@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"),
     Input("selected-device-store", "data"),
     Input("interval-component", "n_intervals")]
)
def render_tab_content(active_tab, selected_device_data, n_intervals):
    device_id = selected_device_data.get("device_id") if selected_device_data else None
    
    if active_tab == "dashboard":
        return render_dashboard(device_id)
    elif active_tab == "telemetry":
        return render_telemetry(device_id)
    elif active_tab == "measures":
        return render_measures(device_id)
    elif active_tab == "commands":
        return render_commands(device_id)
    
    return html.Div("Seleziona una tab")

def render_dashboard(device_id):
    """Renderizza dashboard principale"""
    if not device_id:
        return dbc.Alert([
            html.I(className="fas fa-info-circle me-2"),
            html.Div([
                html.H4("Benvenuto nel Control Panel e-Link"),
                html.P("Seleziona un dispositivo dalla sidebar per iniziare"),
                html.Hr(),
                html.H5("Funzionalità disponibili:"),
                html.Ul([
                    html.Li("📊 Visualizzare telemetria real-time (pressione, flusso, accelerazioni)"),
                    html.Li("📁 Analizzare misure complete salvate su file binario"),
                    html.Li("⚙️ Inviare comandi ai dispositivi connessi"),
                    html.Li("🔧 Configurare parametri dei sensori")
                ]),
                html.H5("Come iniziare:"),
                html.Ol([
                    html.Li("Assicurati che il TCP Server sia attivo"),
                    html.Li("Connetti un dispositivo e-Link alla rete"),
                    html.Li("Seleziona il dispositivo dalla sidebar"),
                    html.Li("Naviga tra le diverse sezioni usando le tab")
                ]),
                html.Hr(),
                html.P([
                    html.Strong("Note: "),
                    "I dati telemetria sono mantenuti per 1 ora (buffer circolare). ",
                    "Le misure complete sono salvate in data/measures/. ",
                    "Il database è aggiornato automaticamente ogni volta che arriva un log."
                ], className="text-muted small")
            ])
        ], color="info")
    
    # Recupera ultimo record telemetria
    db = get_db()
    latest = db.get_latest_telemetry(device_id)
    
    if not latest:
        return dbc.Alert([
            html.I(className="fas fa-exclamation-circle me-2"),
            "Nessun dato telemetria disponibile per questo dispositivo. ",
            "I dati appariranno qui appena il dispositivo invierà il primo log."
        ], color="warning")
    
    # Dashboard con metriche
    return html.Div([
        html.H2([
            html.I(className="fas fa-tachometer-alt me-2"),
            f"Dashboard Device {device_id}"
        ]),
        html.P(f"Ultimo aggiornamento: {latest['timestamp']}", className="text-muted"),
        
        # Tensioni
        html.H4([html.I(className="fas fa-bolt me-2"), "Tensioni"]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Vbatt", className="card-title"),
                        html.H3(f"{latest['vbatt']:.2f} V" if latest['vbatt'] else "N/A", 
                               className="text-primary")
                    ])
                ])
            ], width=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("V1", className="card-title"),
                        html.H3(f"{latest['v1']:.2f} V" if latest['v1'] else "N/A", 
                               className="text-primary")
                    ])
                ])
            ], width=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("V2", className="card-title"),
                        html.H3(f"{latest['v2']:.2f} V" if latest['v2'] else "N/A", 
                               className="text-primary")
                    ])
                ])
            ], width=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("V3", className="card-title"),
                        html.H3(f"{latest['v3']:.2f} V" if latest['v3'] else "N/A", 
                               className="text-primary")
                    ])
                ])
            ], width=3)
        ], className="mb-4"),
        
        # Correnti
        html.H4([html.I(className="fas fa-battery-half me-2"), "Correnti"]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("I1", className="card-title"),
                        html.H3(f"{latest['i1']:.3f} A" if latest['i1'] else "N/A", 
                               className="text-success")
                    ])
                ])
            ], width=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("I2", className="card-title"),
                        html.H3(f"{latest['i2']:.3f} A" if latest['i2'] else "N/A", 
                               className="text-success")
                    ])
                ])
            ], width=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("I3", className="card-title"),
                        html.H3(f"{latest['i3']:.3f} A" if latest['i3'] else "N/A", 
                               className="text-success")
                    ])
                ])
            ], width=4)
        ], className="mb-4"),
        
        # Altri sensori
        html.H4([html.I(className="fas fa-thermometer-half me-2"), "Altri Sensori"]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("🌡️ Temperatura", className="card-title"),
                        html.H3(f"{latest['temperature']:.1f} °C" if latest['temperature'] else "N/A", 
                               className="text-warning")
                    ])
                ])
            ], width=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("📈 Pressione", className="card-title"),
                        html.H3(f"{latest['pressure']:.2f} bar" if latest['pressure'] else "N/A", 
                               className="text-info")
                    ])
                ])
            ], width=6)
        ])
    ])

def render_telemetry(device_id):
    """Renderizza pagina telemetria"""
    if not device_id:
        return dbc.Alert("Seleziona un dispositivo per visualizzare la telemetria", color="warning")
    
    from telemetry_page import create_telemetry_layout
    return create_telemetry_layout()

def render_measures(device_id):
    """Renderizza pagina misure"""
    if not device_id:
        return dbc.Alert("Seleziona un dispositivo per visualizzare le misure", color="warning")
    
    from measures_page import create_measures_layout
    return create_measures_layout()

def render_commands(device_id):
    """Renderizza pagina comandi"""
    if not device_id:
        return dbc.Alert("Seleziona un dispositivo per inviare comandi", color="warning")
    
    from commands_page import create_commands_layout
    return create_commands_layout()

# Registra callback delle pagine secondarie
try:
    from telemetry_page import register_telemetry_callbacks
    register_telemetry_callbacks(app, get_db)
except ImportError:
    pass

try:
    from measures_page import register_measures_callbacks
    measures_dir = Path(__file__).parent.parent / "data" / "measures"
    register_measures_callbacks(app, str(measures_dir))
except ImportError:
    pass

try:
    from commands_page import register_commands_callbacks
    register_commands_callbacks(app, tcp_server)
except ImportError:
    pass

if __name__ == "__main__":
    import atexit
    
    # Registra la funzione di chiusura
    def cleanup():
        if hasattr(tcp_server, 'stop'):
            tcp_server.stop()
    
    atexit.register(cleanup)
    
    # Applicazione avviata in modalità database
    app.run_server(debug=True, host="0.0.0.0", port=21002)