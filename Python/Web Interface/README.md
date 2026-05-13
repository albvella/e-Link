# e-Link Web Interface

Interfaccia web per monitoraggio e controllo dispositivi e-Link.

## Caratteristiche

- 📊 **Telemetria Real-Time**: Visualizzazione pressione, flusso e accelerazioni con plot interattivi
- 📁 **Visualizzazione Misure**: Decompressione e analisi misure complete da file `.bin`
- ⚙️ **Centro Comandi**: Invio comandi e configurazione parametri dispositivi
- 💾 **Buffer Circolare**: Dati telemetria mantenuti per 1 ora (configurabile)
- 🔄 **Auto-Refresh**: Aggiornamento automatico dati real-time

## Architettura

```
[STM32 Devices] ←TCP→ [Python TCP Server] ←→ [SQLite DB] ←→ [Streamlit Web UI]
```

- **TCP Server**: `eLink_TCP_Interface.py` (gestisce connessioni dispositivi)
- **Database**: SQLite con buffer circolare automatico
- **Web UI**: Streamlit con Plotly per grafici interattivi

## Installazione

### 1. Installa dipendenze Python

```bash
cd "Web Interface"
pip install -r requirements.txt
```

### 2. Verifica struttura cartelle

```
Python/
├── eLink_TCP_Interface.py
├── eLink_Decompress_Measure.py
├── Web Interface/
│   ├── streamlit_app.py
│   ├── db_manager.py
│   ├── requirements.txt
│   └── pages/
│       ├── 1_Telemetry.py
│       ├── 2_Measures.py
│       └── 3_Commands.py
└── data/
    ├── elink.db (creato automaticamente)
    └── measures/ (misure .bin salvate qui)
```

## Utilizzo

### Avvio Server TCP + Web Interface

**Terminale 1** - Avvia server TCP:
```bash
cd Python
python eLink_TCP_Interface.py
```

**Terminale 2** - Avvia web interface:
```bash
cd "Python/Web Interface"
streamlit run streamlit_app.py
```

La web interface sarà disponibile su: `http://localhost:8501`

### Workflow

1. **Avvia server TCP** - Accetta connessioni dai dispositivi e-Link
2. **Connetti dispositivo** - Il dispositivo si registra automaticamente
3. **Apri web interface** - Naviga su `http://localhost:8501`
4. **Seleziona dispositivo** - Dalla sidebar, scegli il device da monitorare
5. **Naviga tra le sezioni**:
   - **Home**: Dashboard con metriche principali
   - **Telemetry**: Plot real-time con selezione intervallo (1min, 10min, 1h)
   - **Measures**: Visualizza e analizza misure complete salvate
   - **Commands**: Invia comandi e configura parametri

## Funzionalità Database

### Buffer Circolare Automatico

- **Capacità**: 1 ora di dati per dispositivo
- **Pulizia automatica**: Dati più vecchi di 1h vengono eliminati automaticamente
- **Timestamp**: Basato su orario arrivo log (server-side)
- **Periodo logging**: Configurabile dal dispositivo (default 1s)

### Query Ottimizzate

- Indici su `device_id` e `timestamp` per query veloci
- Supporto multi-device con isolamento dati
- Tracking stato connessione dispositivi

## Configurazione

### Parametri Dispositivo

Configurabili tramite web interface (pagina Commands):

- `SAMP_FREQ`: Frequenza campionamento (800 o 1600 Hz)
- `BUFFER_SECS`: Durata buffer circolare (5-30s)
- `LOG_PERIOD`: Periodo invio log telemetria (100-10000ms)
- `CONN_TIMEOUT`: Timeout connessione TCP (1000-60000ms)
- `HAMMER_TH`: Soglia rilevamento colpo d'ariete
- `HIGH_TH` / `LOW_TH`: Soglie pressione per ora (24 valori)
- `TCP_IP` / `TCP_PORT`: Parametri connessione server

### Intervalli Visualizzazione

Selezionabili nella pagina Telemetry:

- **1 minuto**: Visualizzazione dettagliata breve periodo
- **10 minuti**: Monitoraggio medio termine (default)
- **1 ora**: Overview completo buffer

## Struttura Database

### Tabella `telemetry`

```sql
CREATE TABLE telemetry (
    id INTEGER PRIMARY KEY,
    device_id INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    pressure REAL,
    flow REAL,
    ax REAL, ay REAL, az REAL,
    voltage REAL,
    current REAL,
    temperature REAL
);
```

### Tabella `devices`

```sql
CREATE TABLE devices (
    device_id INTEGER PRIMARY KEY,
    last_seen DATETIME,
    status TEXT,
    ip_address TEXT
);
```

## Formato Dati

### Log Telemetria (TCP)

```
L:<device_id>,<press>,<flow>,<ax>,<ay>,<az>,<vbatt>,<i1>,<i2>,<i3>,<v1>,<v2>,<v3>,<temp>
```

### Misure Complete (`.bin`)

- **Compressione**: ADPCM (12-bit per pressione, 16-bit per accelerazioni)
- **RLE**: Run-Length Encoding per flusso
- **Metadata**: 6 byte header (pressure_size, flow_size, accel_size)
- **Rapporto compressione**: Tipicamente 5-10x

## Troubleshooting

### Web interface non si connette

- Verifica che il server TCP sia avviato
- Controlla che non ci siano conflitti di porta (8501)
- Verifica path moduli in `sys.path.append()`

### Nessun dispositivo visualizzato

- Controlla che il dispositivo sia connesso al server TCP
- Verifica che il device_id sia stato associato correttamente
- Controlla log server TCP per messaggi di errore

### Database non si aggiorna

- Verifica che `DB_AVAILABLE = True` in `eLink_TCP_Interface.py`
- Controlla permessi scrittura su `data/elink.db`
- Verifica che i log arrivino correttamente al server

### Plot vuoti

- Controlla che il dispositivo stia inviando log
- Verifica periodo logging configurato sul device
- Controlla che i dati siano nel range temporale selezionato

## Note Implementazione

### Stato Attuale

- ✅ Database con buffer circolare funzionante
- ✅ Salvataggio automatico telemetria da TCP server
- ✅ Plot real-time con Plotly (interattivi)
- ✅ Visualizzazione misure complete
- ✅ Interfaccia comandi completa
- ⚠️ Integrazione invio comandi in fase di sviluppo

### Prossimi Step

1. Implementare funzione per recuperare socket client da device_id
2. Collegare pulsanti comandi alle funzioni TCP server
3. Gestire risposte asincrone dispositivi
4. Implementare callback per aggiornamento UI dopo risposta

## Sviluppo

### Struttura Codice

```python
# db_manager.py
- TelemetryDB: Gestione database SQLite
  - insert_telemetry(): Inserisce + pulisce vecchi dati
  - get_telemetry(): Query con filtro temporale
  - update_device_status(): Tracking connessioni

# streamlit_app.py
- Home dashboard con selezione device
- Metriche real-time principali
- Link rapidi alle sezioni

# pages/1_Telemetry.py
- Plot real-time pressione/flusso/accelerazioni
- Selezione intervallo temporale
- Auto-refresh ogni 1s
- Statistiche aggregate

# pages/2_Measures.py
- Caricamento file .bin (salvati o upload)
- Decompressione con eLink_Decompress_Measure
- Plot interattivi Plotly
- Export CSV dati decodificati

# pages/3_Commands.py
- Pulsanti per comandi base (SRT, IDL, PNG, MSR, RST, SND)
- Form configurazione parametri
- OTA update interface
- Lettura configurazione corrente
```

### Contribuire

Per aggiungere nuove funzionalità:

1. Modifica schema database in `db_manager.py` se necessario
2. Aggiungi funzioni salvataggio dati in `eLink_TCP_Interface.py`
3. Crea nuova pagina in `pages/` se serve nuova sezione
4. Aggiorna questo README

## Licenza

Parte del progetto Smart_Joint - e-Link System

## Autore

Sviluppato per il progetto Smart_Joint
Versione 1.0 - Novembre 2025
