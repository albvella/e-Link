"""
e-Link Commands Page - Dash Component
Centro comandi convertito da Streamlit
"""

import dash
from dash import dcc, html, Input, Output, State, callback, callback_context
import dash_bootstrap_components as dbc
import base64
import sys
from pathlib import Path
from datetime import datetime

# Aggiungi path per import moduli
sys.path.append(str(Path(__file__).parent.parent))

def get_basic_commands_content():
    """Restituisce il contenuto statico dei comandi base"""
    return html.Div([
        html.H4("Comandi rapidi per il controllo del dispositivo"),
        
        # Prima riga comandi
        dbc.Row([
            dbc.Col([
                dbc.Button(
                    [html.I(className="fas fa-play me-2"), "Start Misura (SRT)"],
                    id="srt-cmd-btn",
                    color="success",
                    size="lg",
                    className="w-100 mb-2"
                )
            ], width=4),
            dbc.Col([
                dbc.Button(
                    [html.I(className="fas fa-stop me-2"), "Idle (IDL)"],
                    id="idl-cmd-btn",
                    color="warning",
                    size="lg",
                    className="w-100 mb-2"
                )
            ], width=4),
            dbc.Col([
                dbc.Button(
                    [html.I(className="fas fa-satellite-dish me-2"), "Ping (PNG)"],
                    id="png-cmd-btn",
                    color="info",
                    size="lg",
                    className="w-100 mb-2"
                )
            ], width=4)
        ], className="mb-4"),
        
        html.Hr(),
        
        # Seconda riga comandi
        dbc.Row([
            dbc.Col([
                dbc.Button(
                    [html.I(className="fas fa-chart-line me-2"), "Richiedi Misura (MSR)"],
                    id="msr-cmd-btn",
                    color="primary",
                    size="lg",
                    className="w-100 mb-2"
                )
            ], width=6),
            dbc.Col([
                html.Div([
                    dbc.Checkbox(
                        id="reset-confirm-checkbox",
                        label="Conferma reset dispositivo",
                        value=False,
                        className="mb-2"
                    ),
                    dbc.Button(
                        [html.I(className="fas fa-redo me-2"), "Reset (RST)"],
                        id="rst-cmd-btn",
                        color="danger",
                        size="lg",
                        className="w-100",
                        disabled=True
                    )
                ])
            ], width=6)
        ], className="mb-4"),
        
        html.Hr(),
        
        # Controllo invio dati
        html.H5("Controllo Invio Dati"),
        dbc.Row([
            dbc.Col([
                dbc.Button(
                    [html.I(className="fas fa-play-circle me-2"), "Avvia Invio Log (SND,1)"],
                    id="snd-on-cmd-btn",
                    color="success",
                    size="lg",
                    className="w-100"
                )
            ], width=6),
            dbc.Col([
                dbc.Button(
                    [html.I(className="fas fa-pause-circle me-2"), "Ferma Invio Log (SND,0)"],
                    id="snd-off-cmd-btn",
                    color="secondary",
                    size="lg",
                    className="w-100"
                )
            ], width=6)
        ])
    ])

def get_configuration_content():
    """Restituisce il contenuto statico della configurazione"""
    return html.Div([
        html.H4("Modifica i parametri di configurazione del dispositivo"),
        
        # Parametri campionamento
        html.H5("Parametri Campionamento", className="mt-4"),
        dbc.Row([
            dbc.Col([
                html.Label("Frequenza Campionamento [Hz]:", className="fw-bold"),
                dcc.Dropdown(
                    id="samp-freq-dropdown",
                    options=[
                        {"label": "800 Hz", "value": 800},
                        {"label": "1600 Hz", "value": 1600}
                    ],
                    value=800,
                    className="mb-3"
                ),
                dbc.Button(
                    [html.I(className="fas fa-save me-2"), "Imposta SAMP_FREQ"],
                    id="set-samp-freq-btn",
                    color="primary",
                    className="w-100"
                )
            ], width=6),
            dbc.Col([
                html.Label("Buffering [secondi]:", className="fw-bold"),
                dcc.Slider(
                    id="buffer-secs-slider",
                    min=5,
                    max=30,
                    step=1,
                    value=10,
                    marks={i: str(i) for i in range(5, 31, 5)},
                    className="mb-3"
                ),
                dbc.Button(
                    [html.I(className="fas fa-save me-2"), "Imposta BUFFER_SECS"],
                    id="set-buffer-secs-btn",
                    color="primary",
                    className="w-100"
                )
            ], width=6)
        ], className="mb-4"),
        
        html.Hr(),
        
        # Timeout e logging
        html.H5("Timeout e Logging"),
        dbc.Row([
            dbc.Col([
                html.Label("Connection Timeout [ms]:", className="fw-bold"),
                dbc.Input(
                    id="conn-timeout-input",
                    type="number",
                    value=5000,
                    min=1000,
                    max=60000,
                    step=1000,
                    className="mb-3"
                ),
                dbc.Button(
                    [html.I(className="fas fa-save me-2"), "Imposta CONN_TIMEOUT"],
                    id="set-timeout-btn",
                    color="primary",
                    className="w-100"
                )
            ], width=6),
            dbc.Col([
                html.Label("Log Period [ms]:", className="fw-bold"),
                dbc.Input(
                    id="log-period-input",
                    type="number",
                    value=1000,
                    min=100,
                    max=10000,
                    step=100,
                    className="mb-3"
                ),
                dbc.Button(
                    [html.I(className="fas fa-save me-2"), "Imposta LOG_PERIOD"],
                    id="set-log-period-btn",
                    color="primary",
                    className="w-100"
                )
            ], width=6)
        ], className="mb-4"),
        
        html.Hr(),
        
        # Soglie rilevamento
        html.H5("Soglie Rilevamento"),
        dbc.Row([
            dbc.Col([
                html.Label("Hammer Threshold [ADC counts]:", className="fw-bold"),
                dbc.Input(
                    id="hammer-th-input",
                    type="number",
                    value=500,
                    min=0,
                    max=4095,
                    className="mb-3"
                ),
                dbc.Button(
                    [html.I(className="fas fa-save me-2"), "Imposta HAMMER_TH"],
                    id="set-hammer-th-btn",
                    color="primary",
                    className="w-100"
                )
            ], width=12)
        ], className="mb-4"),
        
        # Soglie per ora del giorno
        html.H6("Soglie Alta/Bassa per Ora del Giorno"),
        dbc.Row([
            dbc.Col([
                html.Label("Ora:", className="fw-bold"),
                dcc.Dropdown(
                    id="hour-selector",
                    options=[{"label": f"{i:02d}:00", "value": i} for i in range(24)],
                    value=12,
                    className="mb-3"
                )
            ], width=4),
            dbc.Col([
                html.Label("High Threshold [ADC]:", className="fw-bold"),
                dbc.Input(
                    id="high-th-input",
                    type="number",
                    value=3000,
                    min=0,
                    max=4095,
                    className="mb-3"
                ),
                dbc.Button(
                    [html.I(className="fas fa-save me-2"), "Imposta HIGH_TH"],
                    id="set-high-th-btn",
                    color="primary",
                    className="w-100"
                )
            ], width=4),
            dbc.Col([
                html.Label("Low Threshold [ADC]:", className="fw-bold"),
                dbc.Input(
                    id="low-th-input",
                    type="number",
                    value=500,
                    min=0,
                    max=4095,
                    className="mb-3"
                ),
                dbc.Button(
                    [html.I(className="fas fa-save me-2"), "Imposta LOW_TH"],
                    id="set-low-th-btn",
                    color="primary",
                    className="w-100"
                )
            ], width=4)
        ])
    ])

def get_advanced_content():
    """Restituisce il contenuto statico dei comandi avanzati"""
    return html.Div([
        html.H4("Configurazione avanzata e OTA"),
        
        # Connessione TCP
        html.H5("📡 Connessione TCP", className="mt-4"),
        dbc.Row([
            dbc.Col([
                html.Label("TCP Server IP:", className="fw-bold"),
                dbc.Input(
                    id="tcp-ip-input",
                    type="text",
                    value="192.168.1.100",
                    className="mb-3"
                ),
                dbc.Button(
                    [html.I(className="fas fa-save me-2"), "Imposta TCP_IP"],
                    id="set-tcp-ip-btn",
                    color="primary",
                    className="w-100"
                )
            ], width=6),
            dbc.Col([
                html.Label("TCP Server Port:", className="fw-bold"),
                dbc.Input(
                    id="tcp-port-input",
                    type="text",
                    value="21001",
                    className="mb-3"
                ),
                dbc.Button(
                    [html.I(className="fas fa-save me-2"), "Imposta TCP_PORT"],
                    id="set-tcp-port-btn",
                    color="primary",
                    className="w-100"
                )
            ], width=6)
        ], className="mb-4"),
        
        html.Hr(),
        
        # OTA Update
        html.H5("🔄 OTA Update"),
        dbc.Alert([
            html.I(className="fas fa-exclamation-triangle me-2"),
            "Attenzione: l'aggiornamento OTA richiede diversi minuti e il dispositivo sarà offline durante il processo"
        ], color="warning"),
        
        dcc.Upload(
            id="ota-upload",
            children=html.Div([
                html.I(className="fas fa-cloud-upload-alt fa-2x mb-3"),
                html.Br(),
                "Trascina qui un file firmware (.bin) oppure clicca per selezionarlo"
            ]),
            style={
                'width': '100%',
                'height': '120px',
                'lineHeight': '120px',
                'borderWidth': '2px',
                'borderStyle': 'dashed',
                'borderRadius': '10px',
                'textAlign': 'center',
                'margin': '10px 0',
                'cursor': 'pointer'
            },
            multiple=False,
            accept=".bin"
        ),
        
        html.Div(id="ota-upload-feedback"),
        
        dbc.Button(
            [html.I(className="fas fa-rocket me-2"), "Avvia OTA Update"],
            id="start-ota-btn",
            color="danger",
            size="lg",
            disabled=True,
            className="w-100 mt-3"
        ),
        
        html.Hr(),
        
        # Lettura configurazione
        html.H5("📖 Lettura Configurazione"),
        dbc.Row([
            dbc.Col([
                html.Label("Variabile da leggere:", className="fw-bold"),
                dcc.Dropdown(
                    id="get-var-dropdown",
                    options=[
                        {"label": "DEVICE_ID", "value": "DEVICE_ID"},
                        {"label": "SAMP_FREQ", "value": "SAMP_FREQ"},
                        {"label": "BUFFER_SECS", "value": "BUFFER_SECS"},
                        {"label": "CONN_TIMEOUT", "value": "CONN_TIMEOUT"},
                        {"label": "LOG_PERIOD", "value": "LOG_PERIOD"},
                        {"label": "HAMMER_TH", "value": "HAMMER_TH"},
                        {"label": "TCP_IP", "value": "TCP_IP"},
                        {"label": "TCP_PORT", "value": "TCP_PORT"}
                    ],
                    value="DEVICE_ID",
                    className="mb-3"
                )
            ], width=8),
            dbc.Col([
                dbc.Button(
                    [html.I(className="fas fa-eye me-2"), "Leggi Valore"],
                    id="get-value-btn",
                    color="info",
                    className="w-100 mt-4"
                )
            ], width=4)
        ])
    ])

def create_commands_layout():
    """Crea il layout per la pagina comandi"""
    return html.Div([
        # Header
        html.H2([
            html.I(className="fas fa-terminal me-2"),
            "Centro Comandi"
        ], className="mb-4"),
        
        # Selettore dispositivo
        dbc.Card([
            dbc.CardHeader([
                html.I(className="fas fa-target me-2"),
                "Target Comando"
            ]),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.Label("Dispositivo Target:", className="fw-bold"),
                        dcc.Dropdown(
                            id="command-target-dropdown",
                            options=[
                                {"label": "🌐 Tutti i dispositivi (Broadcast)", "value": 0}
                            ],
                            value=0,
                            className="mb-2"
                        )
                    ], width=12)
                ])
            ])
        ], className="mb-3"),
        
        # Area risposte dispositivo
        dbc.Card([
            dbc.CardHeader([
                dbc.Row([
                    dbc.Col([
                        html.I(className="fas fa-comment-dots me-2"),
                        "Risposte Dispositivo"
                    ], width="auto"),
                    dbc.Col([
                        dbc.Button(
                            [html.I(className="fas fa-sync me-1"), "Aggiorna"], 
                            id="refresh-responses-btn",
                            color="secondary",
                            size="sm"
                        )
                    ], width="auto")
                ], justify="between", align="center")
            ]),
            dbc.CardBody([
                html.Div(
                    "In attesa di comandi...",
                    id="command-response-area",
                    style={
                        "height": "120px",
                        "overflow-y": "auto", 
                        "background-color": "#f8f9fa",
                        "padding": "10px",
                        "border-radius": "5px",
                        "font-family": "monospace",
                        "font-size": "0.9em",
                        "white-space": "pre-wrap",
                        "border": "1px solid #dee2e6"
                    }
                )
            ])
        ], className="mb-4"),
        
        # Tutti i contenuti sempre presenti ma inizialmente nascosti
        html.Div(
            id="basic-commands-content", 
            style={"display": "block"},
            children=get_basic_commands_content()
        ),
        html.Div(
            id="configuration-content", 
            style={"display": "none"},
            children=get_configuration_content()
        ),
        html.Div(
            id="advanced-content", 
            style={"display": "none"},
            children=get_advanced_content()
        ),
        
        # Tabs per categorie comandi
        dbc.Tabs([
            dbc.Tab(label="🔧 Comandi Base", tab_id="basic-commands"),
            dbc.Tab(label="⚙️ Configurazione", tab_id="configuration"),
            dbc.Tab(label="📡 Comandi Avanzati", tab_id="advanced-commands")
        ], id="commands-tabs", active_tab="basic-commands"),
        
        # Area feedback comandi
        html.Div(id="command-feedback", className="mt-4"),
        
        # Store per device corrente
        dcc.Store(id="commands-device-store"),
        
        # Rimosso interval automatico - aggiornamento solo manuale
    ])

def register_commands_callbacks(app, tcp_server=None):
    """Registra i callback per la pagina comandi"""
    
    @app.callback(
        [Output("basic-commands-content", "style"),
         Output("configuration-content", "style"),
         Output("advanced-content", "style")],
        [Input("commands-tabs", "active_tab")]
    )
    def update_tab_visibility(active_tab):
        # Mostra solo la tab attiva
        basic_style = {"display": "block"} if active_tab == "basic-commands" else {"display": "none"}
        config_style = {"display": "block"} if active_tab == "configuration" else {"display": "none"}
        advanced_style = {"display": "block"} if active_tab == "advanced-commands" else {"display": "none"}
        
        return basic_style, config_style, advanced_style
    
    # Callback per gestire i comandi base
    @app.callback(
        Output("command-response-area", "children"),
        [Input("srt-cmd-btn", "n_clicks"),
         Input("idl-cmd-btn", "n_clicks"),
         Input("png-cmd-btn", "n_clicks"),
         Input("msr-cmd-btn", "n_clicks"),
         Input("rst-cmd-btn", "n_clicks"),
         Input("snd-on-cmd-btn", "n_clicks"),
         Input("snd-off-cmd-btn", "n_clicks")],
        [State("command-response-area", "children"),
         State("reset-confirm-checkbox", "value"),
         State("command-target-dropdown", "value")],
        prevent_initial_call=True
    )
    def handle_basic_commands(srt_clicks, idl_clicks, png_clicks, msr_clicks, 
                            rst_clicks, snd_on_clicks, snd_off_clicks,
                            current_content, reset_confirmed, target_device):
        """Gestisce i comandi base e aggiorna l'area risposte"""
        ctx = callback_context
        if not ctx.triggered:
            return current_content
            
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Mappa pulsante->comando
        command_map = {
            "srt-cmd-btn": "SRT",
            "idl-cmd-btn": "IDL", 
            "png-cmd-btn": "PNG",
            "msr-cmd-btn": "MSR",
            "rst-cmd-btn": "RST",
            "snd-on-cmd-btn": "SND,1",
            "snd-off-cmd-btn": "SND,0"
        }
        
        # Controllo speciale per reset
        if button_id == "rst-cmd-btn" and not reset_confirmed:
            new_line = f"[{timestamp}] ERRORE: Confermare il reset prima di procedere\\n"
        else:
            command = command_map.get(button_id, "UNKNOWN")
            
            # Invia comando reale tramite TCP server
            if tcp_server:
                # Usa il dispositivo selezionato (0 = broadcast, altro = specifico)
                device_id = target_device or 0
                success = tcp_server.send_command_to_device(device_id, command)
                
                if success:
                    if device_id == 0:
                        new_line = f"[{timestamp}] ✓ Comando {command} inviato a tutti i dispositivi\\n"
                    else:
                        new_line = f"[{timestamp}] ✓ Comando {command} inviato a Device {device_id}\\n"
                else:
                    new_line = f"[{timestamp}] ✗ Errore invio comando {command} a Device {device_id}\\n"
            else:
                new_line = f"[{timestamp}] ⚠ TCP Server non disponibile - Comando {command}\\n"
            
        # Aggiungi la nuova riga al contenuto esistente
        if isinstance(current_content, str):
            updated_content = current_content + new_line
        else:
            updated_content = "In attesa di comandi...\\n" + new_line
            
        # Mantieni solo le ultime 10 righe per evitare overflow
        lines = updated_content.split("\\n")
        if len(lines) > 10:
            updated_content = "\\n".join(lines[-10:])
            
        return updated_content
    
    # Callback per abilitare/disabilitare il pulsante reset
    @app.callback(
        Output("rst-cmd-btn", "disabled"),
        [Input("reset-confirm-checkbox", "value")]
    )
    def toggle_reset_button(confirmed):
        """Abilita il pulsante reset solo se confermato"""
        return not confirmed
    
    # Callback per aggiornare lista dispositivi target
    @app.callback(
        Output("command-target-dropdown", "options"),
        [Input("refresh-responses-btn", "n_clicks")],
        prevent_initial_call=False
    )
    def update_target_devices(refresh_clicks):
        """Aggiorna la lista dei dispositivi disponibili per i comandi"""
        options = [{"label": "🌐 Tutti i dispositivi (Broadcast)", "value": 0}]
        
        if tcp_server:
            try:
                connected_devices = tcp_server.get_connected_devices()
                for device_id in connected_devices:
                    options.append({
                        "label": f"📱 Device {device_id}",
                        "value": device_id
                    })
            except Exception as e:
                print(f"Errore aggiornamento dispositivi target: {e}")
                
        return options
    

    
    @app.callback(
        Output("configuration-content", "children"),
        [Input("commands-tabs", "active_tab")]
    )
    def render_configuration(active_tab):        
        return html.Div([
            html.H4("Modifica i parametri di configurazione del dispositivo"),
            
            # Parametri campionamento
            html.H5("Parametri Campionamento", className="mt-4"),
            dbc.Row([
                dbc.Col([
                    html.Label("Frequenza Campionamento [Hz]:", className="fw-bold"),
                    dcc.Dropdown(
                        id="samp-freq-dropdown",
                        options=[
                            {"label": "800 Hz", "value": 800},
                            {"label": "1600 Hz", "value": 1600}
                        ],
                        value=800,
                        className="mb-3"
                    ),
                    dbc.Button(
                        [html.I(className="fas fa-save me-2"), "Imposta SAMP_FREQ"],
                        id="set-samp-freq-btn",
                        color="primary",
                        className="w-100"
                    )
                ], width=6),
                dbc.Col([
                    html.Label("Buffering [secondi]:", className="fw-bold"),
                    dcc.Slider(
                        id="buffer-secs-slider",
                        min=5,
                        max=30,
                        step=1,
                        value=10,
                        marks={i: str(i) for i in range(5, 31, 5)},
                        className="mb-3"
                    ),
                    dbc.Button(
                        [html.I(className="fas fa-save me-2"), "Imposta BUFFER_SECS"],
                        id="set-buffer-secs-btn",
                        color="primary",
                        className="w-100"
                    )
                ], width=6)
            ], className="mb-4"),
            
            html.Hr(),
            
            # Timeout e logging
            html.H5("Timeout e Logging"),
            dbc.Row([
                dbc.Col([
                    html.Label("Connection Timeout [ms]:", className="fw-bold"),
                    dbc.Input(
                        id="conn-timeout-input",
                        type="number",
                        value=5000,
                        min=1000,
                        max=60000,
                        step=1000,
                        className="mb-3"
                    ),
                    dbc.Button(
                        [html.I(className="fas fa-save me-2"), "Imposta CONN_TIMEOUT"],
                        id="set-timeout-btn",
                        color="primary",
                        className="w-100"
                    )
                ], width=6),
                dbc.Col([
                    html.Label("Log Period [ms]:", className="fw-bold"),
                    dbc.Input(
                        id="log-period-input",
                        type="number",
                        value=1000,
                        min=100,
                        max=10000,
                        step=100,
                        className="mb-3"
                    ),
                    dbc.Button(
                        [html.I(className="fas fa-save me-2"), "Imposta LOG_PERIOD"],
                        id="set-log-period-btn",
                        color="primary",
                        className="w-100"
                    )
                ], width=6)
            ], className="mb-4"),
            
            html.Hr(),
            
            # Soglie rilevamento
            html.H5("Soglie Rilevamento"),
            dbc.Row([
                dbc.Col([
                    html.Label("Hammer Threshold [ADC counts]:", className="fw-bold"),
                    dbc.Input(
                        id="hammer-th-input",
                        type="number",
                        value=500,
                        min=0,
                        max=4095,
                        className="mb-3"
                    ),
                    dbc.Button(
                        [html.I(className="fas fa-save me-2"), "Imposta HAMMER_TH"],
                        id="set-hammer-th-btn",
                        color="primary",
                        className="w-100"
                    )
                ], width=12)
            ], className="mb-4"),
            
            # Soglie per ora del giorno
            html.H6("Soglie Alta/Bassa per Ora del Giorno"),
            dbc.Row([
                dbc.Col([
                    html.Label("Ora:", className="fw-bold"),
                    dcc.Dropdown(
                        id="hour-selector",
                        options=[{"label": f"{i:02d}:00", "value": i} for i in range(24)],
                        value=12,
                        className="mb-3"
                    )
                ], width=4),
                dbc.Col([
                    html.Label("High Threshold [ADC]:", className="fw-bold"),
                    dbc.Input(
                        id="high-th-input",
                        type="number",
                        value=3000,
                        min=0,
                        max=4095,
                        className="mb-3"
                    ),
                    dbc.Button(
                        [html.I(className="fas fa-save me-2"), "Imposta HIGH_TH"],
                        id="set-high-th-btn",
                        color="primary",
                        className="w-100"
                    )
                ], width=4),
                dbc.Col([
                    html.Label("Low Threshold [ADC]:", className="fw-bold"),
                    dbc.Input(
                        id="low-th-input",
                        type="number",
                        value=500,
                        min=0,
                        max=4095,
                        className="mb-3"
                    ),
                    dbc.Button(
                        [html.I(className="fas fa-save me-2"), "Imposta LOW_TH"],
                        id="set-low-th-btn",
                        color="primary",
                        className="w-100"
                    )
                ], width=4)
            ])
        ])
    
    @app.callback(
        Output("advanced-content", "children"),
        [Input("commands-tabs", "active_tab")]
    )
    def render_advanced_commands(active_tab):        
        return html.Div([
            html.H4("Configurazione avanzata e OTA"),
            
            # Connessione TCP
            html.H5("📡 Connessione TCP", className="mt-4"),
            dbc.Row([
                dbc.Col([
                    html.Label("TCP Server IP:", className="fw-bold"),
                    dbc.Input(
                        id="tcp-ip-input",
                        type="text",
                        value="192.168.1.100",
                        className="mb-3"
                    ),
                    dbc.Button(
                        [html.I(className="fas fa-save me-2"), "Imposta TCP_IP"],
                        id="set-tcp-ip-btn",
                        color="primary",
                        className="w-100"
                    )
                ], width=6),
                dbc.Col([
                    html.Label("TCP Server Port:", className="fw-bold"),
                    dbc.Input(
                        id="tcp-port-input",
                        type="text",
                        value="21001",
                        className="mb-3"
                    ),
                    dbc.Button(
                        [html.I(className="fas fa-save me-2"), "Imposta TCP_PORT"],
                        id="set-tcp-port-btn",
                        color="primary",
                        className="w-100"
                    )
                ], width=6)
            ], className="mb-4"),
            
            html.Hr(),
            
            # OTA Update
            html.H5("🔄 OTA Update"),
            dbc.Alert([
                html.I(className="fas fa-exclamation-triangle me-2"),
                "Attenzione: l'aggiornamento OTA richiede diversi minuti e il dispositivo sarà offline durante il processo"
            ], color="warning"),
            
            dcc.Upload(
                id="ota-upload",
                children=html.Div([
                    html.I(className="fas fa-cloud-upload-alt fa-2x mb-3"),
                    html.Br(),
                    "Trascina qui un file firmware (.bin) oppure clicca per selezionarlo"
                ]),
                style={
                    'width': '100%',
                    'height': '120px',
                    'lineHeight': '120px',
                    'borderWidth': '2px',
                    'borderStyle': 'dashed',
                    'borderRadius': '10px',
                    'textAlign': 'center',
                    'margin': '10px 0',
                    'cursor': 'pointer'
                },
                multiple=False,
                accept=".bin"
            ),
            
            html.Div(id="ota-upload-feedback"),
            
            dbc.Button(
                [html.I(className="fas fa-rocket me-2"), "Avvia OTA Update"],
                id="start-ota-btn",
                color="danger",
                size="lg",
                disabled=True,
                className="w-100 mt-3"
            ),
            
            html.Hr(),
            
            # Lettura configurazione
            html.H5("📖 Lettura Configurazione"),
            dbc.Row([
                dbc.Col([
                    html.Label("Variabile da leggere:", className="fw-bold"),
                    dcc.Dropdown(
                        id="get-var-dropdown",
                        options=[
                            {"label": "DEVICE_ID", "value": "DEVICE_ID"},
                            {"label": "SAMP_FREQ", "value": "SAMP_FREQ"},
                            {"label": "BUFFER_SECS", "value": "BUFFER_SECS"},
                            {"label": "CONN_TIMEOUT", "value": "CONN_TIMEOUT"},
                            {"label": "LOG_PERIOD", "value": "LOG_PERIOD"},
                            {"label": "HAMMER_TH", "value": "HAMMER_TH"},
                            {"label": "TCP_IP", "value": "TCP_IP"},
                            {"label": "TCP_PORT", "value": "TCP_PORT"}
                        ],
                        value="DEVICE_ID",
                        className="mb-3"
                    )
                ], width=8),
                dbc.Col([
                    dbc.Button(
                        [html.I(className="fas fa-eye me-2"), "Leggi Valore"],
                        id="get-value-btn",
                        color="info",
                        className="w-100 mt-4"
                    )
                ], width=4)
            ])
        ])
    

    
    # Callback per gestire upload OTA
    @app.callback(
        [Output("ota-upload-feedback", "children"),
         Output("start-ota-btn", "disabled")],
        [Input("ota-upload", "contents")],
        [State("ota-upload", "filename")]
    )
    def handle_ota_upload(contents, filename):
        if not contents:
            return "", True
        
        try:
            # Verifica formato file
            if not filename.endswith('.bin'):
                return dbc.Alert("Formato file non supportato. Solo file .bin sono accettati.", 
                               color="danger"), True
            
            # Decodifica e verifica dimensione
            content_type, content_string = contents.split(',')
            decoded = base64.b64decode(content_string)
            file_size = len(decoded)
            
            if file_size > 1024*1024:  # 1MB max
                return dbc.Alert("File troppo grande. Dimensione massima: 1MB", color="danger"), True
            
            feedback = dbc.Alert([
                html.I(className="fas fa-check-circle me-2"),
                f"File firmware pronto: {filename} ({file_size / 1024:.2f} KB)"
            ], color="success")
            
            return feedback, False
            
        except Exception as e:
            return dbc.Alert(f"Errore nel caricamento: {str(e)}", color="danger"), True
    
    # Callback unificato per tutti i comandi (ora che tutti gli elementi esistono sempre)
    @app.callback(
        Output("command-feedback", "children"),
        [Input("srt-cmd-btn", "n_clicks"),
         Input("idl-cmd-btn", "n_clicks"),
         Input("png-cmd-btn", "n_clicks"),
         Input("msr-cmd-btn", "n_clicks"),
         Input("rst-cmd-btn", "n_clicks"),
         Input("snd-on-cmd-btn", "n_clicks"),
         Input("snd-off-cmd-btn", "n_clicks"),
         Input("set-samp-freq-btn", "n_clicks"),
         Input("set-buffer-secs-btn", "n_clicks"),
         Input("set-timeout-btn", "n_clicks"),
         Input("set-log-period-btn", "n_clicks"),
         Input("set-hammer-th-btn", "n_clicks"),
         Input("set-high-th-btn", "n_clicks"),
         Input("set-low-th-btn", "n_clicks"),
         Input("set-tcp-ip-btn", "n_clicks"),
         Input("set-tcp-port-btn", "n_clicks"),
         Input("start-ota-btn", "n_clicks"),
         Input("get-value-btn", "n_clicks")],
        prevent_initial_call=True
    )
    def handle_all_commands(*args):
        ctx = callback_context
        if not ctx.triggered:
            return ""
        
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        # Mapping tutti i comandi
        command_messages = {
            "srt-cmd-btn": ("SRT", "Comando SRT inviato - Misura avviata", "success"),
            "idl-cmd-btn": ("IDL", "Comando IDL inviato - Dispositivo in idle", "info"),
            "png-cmd-btn": ("PNG", "Comando PNG inviato - Ping dispositivo", "info"),
            "msr-cmd-btn": ("MSR", "Comando MSR inviato - Attendi ricezione misura...", "primary"),
            "rst-cmd-btn": ("RST", "Comando RST inviato - Dispositivo in reset", "warning"),
            "snd-on-cmd-btn": ("SND,1", "Invio log abilitato", "success"),
            "snd-off-cmd-btn": ("SND,0", "Invio log disabilitato", "secondary"),
            "set-samp-freq-btn": ("SET SAMP_FREQ", "Frequenza campionamento impostata", "success"),
            "set-buffer-secs-btn": ("SET BUFFER_SECS", "Buffer secondi impostato", "success"),
            "set-timeout-btn": ("SET CONN_TIMEOUT", "Timeout connessione impostato", "success"),
            "set-log-period-btn": ("SET LOG_PERIOD", "Periodo log impostato", "success"),
            "set-hammer-th-btn": ("SET HAMMER_TH", "Soglia hammer impostata", "success"),
            "set-high-th-btn": ("SET HIGH_TH", "Soglia alta impostata", "success"),
            "set-low-th-btn": ("SET LOW_TH", "Soglia bassa impostata", "success"),
            "set-tcp-ip-btn": ("SET TCP_IP", "IP TCP server impostato", "success"),
            "set-tcp-port-btn": ("SET TCP_PORT", "Porta TCP server impostata", "success"),
            "start-ota-btn": ("OTA", "Aggiornamento OTA avviato", "warning"),
            "get-value-btn": ("GET", "Lettura variabile richiesta", "info")
        }
        
        if button_id in command_messages:
            cmd, message, color = command_messages[button_id]
            return html.Div([
                dbc.Alert([
                    html.I(className="fas fa-terminal me-2"),
                    message
                ], color=color, dismissable=True),
                dbc.Alert([
                    html.I(className="fas fa-info-circle me-2"),
                    "⚠️ Funzionalità in fase di sviluppo - Richiede integrazione con TCP server"
                ], color="warning", dismissable=True, className="mt-2")
            ])
        
        return ""

# Callback separati per le altre tab per evitare errori di elementi non esistenti

def render_info_box():
    """Renderizza box informazioni implementazione"""
    return dbc.Card([
        dbc.CardHeader([
            html.I(className="fas fa-info-circle me-2"),
            "Note Implementazione"
        ]),
        dbc.CardBody([
            html.H6("Stato attuale:", className="fw-bold"),
            html.Ul([
                html.Li("✅ Interfaccia utente completa"),
                html.Li("⚠️ Integrazione con TCP server in fase di sviluppo")
            ]),
            
            html.H6("Prossimi step:", className="fw-bold"),
            html.Ol([
                html.Li("Implementare funzione per recuperare socket client da device_id"),
                html.Li("Collegare pulsanti alle funzioni send_command() del TCP server"),
                html.Li("Gestire risposte asincrone dai dispositivi"),
                html.Li("Implementare callback per aggiornamento UI dopo risposta")
            ]),
            
            html.H6("Come procedere:", className="fw-bold"),
            html.P([
                "Il TCP server è già funzionante e gestisce i comandi. Serve solo collegare questa ",
                "interfaccia web al server esistente tramite import diretto o comunicazione locale."
            ])
        ])
    ], className="mt-4")

    # Callback per aggiornare l'area risposte dal database
    @app.callback(
        Output("command-response-area", "children", allow_duplicate=True),
        [Input("refresh-responses-btn", "n_clicks"),
         Input("srt-cmd-btn", "n_clicks"),
         Input("idl-cmd-btn", "n_clicks"), 
         Input("png-cmd-btn", "n_clicks"),
         Input("msr-cmd-btn", "n_clicks"),
         Input("rst-cmd-btn", "n_clicks")],
        prevent_initial_call=False
    )
    def update_response_area(refresh_clicks, srt_clicks, idl_clicks, png_clicks, msr_clicks, rst_clicks):
        """Aggiorna l'area risposte con i dati dal database (solo risposte R:)"""
        try:
            from db_manager import get_db
            db = get_db()
            
            # Recupera le ultime 20 risposte (solo R:)
            responses = db.get_recent_responses(limit=20)
            
            print(f"🔍 DEBUG: Recuperate {len(responses)} risposte R: dal database")
            for i, resp in enumerate(responses[:3]):  # Stampa prime 3 per debug
                device_id = resp.get('device_id', '?')
                response_data = resp.get('response', 'N/A')[:50]
                print(f"  {i+1}: Device {device_id} -> {response_data}...")
            
            if not responses:
                return "In attesa di risposte dei dispositivi...\n(Invia un comando per vedere le risposte qui)"
            
            # Formatta le risposte 
            formatted_responses = []
            
            for response in responses:
                timestamp = response['timestamp'][:19]  # Rimuove microsecondi 
                device_id = response['device_id'] or '?'
                response_data = response['response']
                
                # Rimuove il prefisso R: per la visualizzazione
                if response_data.startswith('R:'):
                    response_data = response_data[2:]
                
                line = f"[{timestamp}] Device {device_id}: {response_data}"
                formatted_responses.append(line)
            
            # Unisci le linee con separatori
            result = "\n".join(formatted_responses)
            print(f"🔍 DEBUG: Risultato finale: {len(result)} caratteri")
            return result
            
        except Exception as e:
            print(f"❌ DEBUG: Errore in update_response_area: {str(e)}")
            return f"Errore caricamento risposte: {str(e)}"