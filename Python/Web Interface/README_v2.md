# e-Link Web Interface v2.0

Interfaccia web per visualizzazione telemetria real-time e controllo dispositivi e-Link.

## 🔄 Aggiornamenti v2.0

- ✅ **Schema Database Corretto**: Correnti (I1, I2, I3) e tensioni (Vbatt, V1, V2, V3) salvate **separatamente**
- ✅ **Integrazione DB Corretta**: Spostata in `eLink_Client_Control.py` (script principale)
- ✅ **Dashboard Aggiornata**: Visualizzazione di tutte le tensioni e correnti separate
- ✅ **Telemetry Plots**: Aggiunta visualizzazione dettagliata per tutte le misure elettriche

## 📋 Caratteristiche

- **Dashboard Real-Time**: Visualizzazione stato dispositivi connessi con metriche live
- **Telemetria**: Plot interattivi di pressione, flusso, accelerazioni, tensioni e correnti
- **Misure Complete**: Visualizzazione e analisi file binari con decompressione ADPCM
- **Comandi**: Interfaccia per inviare comandi e configurare parametri
- **Buffer Circolare**: Mantiene automaticamente solo ultimi 60 minuti di dati
- **Multi-Device**: Gestione simultanea di più dispositivi connessi

## 🗄️ Schema Database

### Tabella `telemetry`
```sql
CREATE TABLE telemetry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    pressure REAL,      -- Pressione [bar]
    flow REAL,          -- Flusso [L/s]
    ax REAL,            -- Accelerazione X [mg]
    ay REAL,            -- Accelerazione Y [mg]
    az REAL,            -- Accelerazione Z [mg]
    vbatt REAL,         -- Tensione batteria [V]
    v1 REAL,            -- Tensione canale 1 [V]
    v2 REAL,            -- Tensione canale 2 [V]
    v3 REAL,            -- Tensione canale 3 [V]
    i1 REAL,            -- Corrente canale 1 [A]
    i2 REAL,            -- Corrente canale 2 [A]
    i3 REAL,            -- Corrente canale 3 [A]
    temperature REAL    -- Temperatura [°C]
)
```

**⚠️ IMPORTANTE**: Le correnti e tensioni sono salvate **separatamente** (non aggregate).

### Tabella `devices`
```sql
CREATE TABLE devices (
    device_id INTEGER PRIMARY KEY,
    last_seen DATETIME,
    status TEXT,        -- "connected" / "disconnected"
    ip_address TEXT
)
```

## 🚀 Setup e Avvio

### 1. Installazione Dipendenze

```bash
pip install streamlit plotly pandas numpy
```

### 2. Avvio TCP Server

**IMPORTANTE**: Utilizzare **`eLink_Client_Control.py`** come script principale:

```bash
cd Python
python eLink_Client_Control.py
```

Il server:
- ✅ Avvia TCP server sulla porta configurata
- ✅ Salva automaticamente i log nel database SQLite
- ✅ Parsing completo con **tutte le correnti e tensioni separate**
- ✅ Aggiorna stato dispositivi (connesso/disconnesso)
- ✅ Gestisce buffer circolare (elimina dati > 1h automaticamente)

### 3. Avvio Web Interface

In un **secondo terminale**:

```bash
cd "Python/Web Interface"
streamlit run streamlit_app.py
```

Streamlit aprirà automaticamente il browser su `http://localhost:8501`.

## 📊 Utilizzo

### Selezione Dispositivo
1. Connetti un dispositivo e-Link al TCP server
2. Nella sidebar della web interface, seleziona il dispositivo dall'elenco
3. La dashboard mostrerà le ultime metriche ricevute

### Pagine Disponibili

#### 🏠 Home (Dashboard)
- Stato dispositivi connessi
- Metriche real-time:
  - **4 tensioni separate**: Vbatt, V1, V2, V3
  - **3 correnti separate**: I1, I2, I3
  - Temperatura e pressione correnti
- Link rapidi alle altre sezioni

#### 📊 Telemetry
- Plot interattivi con Plotly (zoom, pan, hover)
- Selezione intervallo: **1 minuto / 10 minuti / 1 ora**
- Auto-refresh ogni 1 secondo (opzionale)
- Statistiche aggregate (media, max, min)
- Visualizzazione separata di:
  - Pressione
  - Flusso
  - Accelerazioni (3 assi)
  - Tutte le tensioni (4 canali)
  - Tutte le correnti (3 canali)

#### 📁 Measures
- Caricamento file `.bin` da server o upload
- Decompressione automatica (ADPCM + parsing binario)
- Plot sincronizzati di tutte le misure
- Export CSV dei dati decodificati

#### ⚙️ Commands
- Interfaccia comandi: SRT, IDL, PNG, MSR, RST
- Configurazione parametri: SAMP_FREQ, BUFFER_SECS, LOG_PERIOD
- OTA firmware update interface
- **Nota**: Integrazione TCP in fase di sviluppo

## 🔧 Architettura

```
eLink_Client_Control.py  (Script Principale con DB Integration)
    ↓ usa
eLink_TCP_Interface.py   (Classe TCP Server Base)
    ↓ riceve log
eLink_Client_Control.py::rx_handler()
    ↓ parsing: L:ID,press,flow,ax,ay,az,vbatt,i1,i2,i3,v1,v2,v3,temp
    ↓ salvataggio DB
db_manager.py (SQLite Database)
    ↓ buffer circolare 1h
    ↓ 4 tensioni + 3 correnti separate
streamlit_app.py + pages/  (Web Interface)
    ↓ query database
    ↓ visualizzazione Plotly
```

### Formato Log Telemetria
```
L:ID,press,flow,ax,ay,az,vbatt,i1,i2,i3,v1,v2,v3,temp
```

**14 campi totali**:
- `ID`: Device ID (int)
- `press`: Pressione raw (ADC 12-bit)
- `flow`: Flusso raw (conteggio timer)
- `ax, ay, az`: Accelerazioni raw (signed 16-bit)
- `vbatt`: Tensione batteria raw (ADC)
- `i1, i2, i3`: Correnti raw (INA3221, signed 16-bit)
- `v1, v2, v3`: Tensioni canali raw (ADC)
- `temp`: Temperatura raw (DS18B20, signed 16-bit)

**Tutte le conversioni** (ADC → unità fisiche) sono fatte in `rx_handler()`.

## 📁 Struttura File

```
Python/
├── eLink_Client_Control.py  ← SCRIPT PRINCIPALE (con DB integration)
├── eLink_TCP_Interface.py   ← Classe base TCP server (NO DB)
├── eLink_Decompress_Measure.py
└── Web Interface/
    ├── streamlit_app.py     ← Dashboard principale
    ├── db_manager.py        ← Gestione database SQLite
    ├── README.md
    ├── README_v2.md         ← Questo file
    ├── pages/
    │   ├── 1_Telemetry.py   ← Plot real-time telemetria
    │   ├── 2_Measures.py    ← Visualizzazione misure .bin
    │   └── 3_Commands.py    ← Interfaccia comandi
    └── data/                ← (auto-creata)
        ├── elink.db         ← Database SQLite
        └── measures/        ← File .bin misure
```

## ⚠️ Note Importanti

### 1. Script Principale
**Utilizzare sempre `eLink_Client_Control.py`** come script principale:
- ✅ Include integrazione database
- ✅ Parsing completo con tutti i campi separati
- ✅ Gestione connessioni/disconnessioni
- ❌ **NON usare** `eLink_TCP_Interface.py` direttamente (è solo una classe base)

### 2. Database SQLite
- **Path**: `Python/Web Interface/data/elink.db`
- **Schema**: Creato automaticamente al primo avvio
- **Locale**: Stesso PC del server TCP (Shared State architecture)
- **Buffer Circolare**: Dati > 1 ora eliminati automaticamente

### 3. Correnti e Tensioni Separate
- ✅ **I1, I2, I3**: Salvate individualmente (NO somma)
- ✅ **Vbatt, V1, V2, V3**: Salvate individualmente
- Dashboard mostra:
  - Valori individuali
  - Totale correnti (I1+I2+I3) calcolato al volo

### 4. Buffer Circolare
- **Limite**: 1 ora per device (non globale)
- **Trigger**: Ogni nuovo log elimina dati vecchi
- **Personalizzabile**: Modifica `timedelta(hours=1)` in `db_manager.py`

### 5. Multi-Device Support
- Database gestisce più dispositivi simultaneamente
- Ogni device ha il proprio buffer circolare indipendente

## 🐛 Troubleshooting

### Web Interface non mostra dispositivi
```bash
# 1. Verifica TCP server attivo
ps aux | grep eLink_Client_Control.py  # Linux/Mac
tasklist | findstr python                # Windows

# 2. Verifica connessione dispositivo
# Output atteso: "Device ID X connected!"

# 3. Verifica database
ls -la "Python/Web Interface/data/elink.db"
```

### Errore import `db_manager`
- Verifica che la cartella `Web Interface` esista
- Controlla path in `sys.path.append()` in `eLink_Client_Control.py`

### Plot vuoti in Telemetry
1. Attendi ricezione primo log dal dispositivo
2. Controlla intervallo temporale selezionato (prova "1 ora")
3. Verifica dati nel database:
   ```bash
   sqlite3 "Python/Web Interface/data/elink.db"
   SELECT COUNT(*) FROM telemetry WHERE device_id = 1;
   SELECT * FROM telemetry ORDER BY timestamp DESC LIMIT 5;
   ```

### Database non si aggiorna
- Controlla output `eLink_Client_Control.py` per errori "Database error"
- Verifica permessi scrittura su `Python/Web Interface/data/`
- Controlla che `DB_AVAILABLE = True` (import db_manager riuscito)

### Dati vecchi non vengono eliminati
- Buffer circolare trigger: ogni `insert_telemetry()`
- Verifica query DELETE in `db_manager.py::insert_telemetry()`
- Test manuale:
  ```python
  from db_manager import get_db
  db = get_db()
  deleted = db.cleanup_old_data()
  print(f"Deleted {deleted} records")
  ```

## 🔍 Debug e Testing

### Test Database Schema
```python
# Python/Web Interface/
python

from db_manager import get_db
db = get_db()

# Inserisci test record
db.insert_telemetry(999, {
    'pressure': 12.5,
    'flow': 0.8,
    'ax': 10, 'ay': -5, 'az': 980,
    'vbatt': 3.7, 'v1': 5.0, 'v2': 3.3, 'v3': 12.0,
    'i1': 0.5, 'i2': 0.3, 'i3': 0.1,
    'temperature': 25.5
})

# Verifica
latest = db.get_latest_telemetry(999)
print(latest)
# Output atteso: dict con tutti i campi separati
```

### Test TCP Server + Database
```bash
# Terminal 1: Avvia server
cd Python
python eLink_Client_Control.py

# Terminal 2: Simula log da dispositivo
python
import socket
sock = socket.socket()
sock.connect(('localhost', 8000))  # Porta configurata
sock.send(b'L:1,2048,5000,100,-50,16000,3700,400,200,100,5000,3300,12000,400\n')
sock.close()

# Terminal 1: Verifica output
# Atteso: "Data parse error" o salvataggio corretto
```

### Verifica Integrazione Completa
1. Avvia `eLink_Client_Control.py`
2. Connetti dispositivo reale o simulato
3. Invia log telemetria
4. Avvia Streamlit
5. Verifica dashboard aggiornata
6. Verifica plot in pagina Telemetry
7. Controlla metriche correnti/tensioni separate

## 📝 TODO Future

- [ ] Collegare pulsanti comandi UI alle funzioni TCP server
- [ ] Gestire risposte asincrone dispositivi in pagina Commands
- [ ] Aggiungere plot tensioni/correnti nella pagina Telemetry (subplot dedicato)
- [ ] Export CSV anche per telemetria (non solo misure)
- [ ] Notifiche push per eventi critici (disconnessione, errori)
- [ ] Autenticazione utenti per accesso web
- [ ] Logging eventi in database (oltre a telemetria)
- [ ] API REST per accesso programmatico ai dati

## 🔄 Migration da v1.0

Se hai già il database v1.0 con schema vecchio (voltage, current):

```bash
# Backup database vecchio
cp "Python/Web Interface/data/elink.db" "Python/Web Interface/data/elink_v1_backup.db"

# Elimina database vecchio
rm "Python/Web Interface/data/elink.db"

# Riavvia server (creerà nuovo schema)
python eLink_Client_Control.py
```

**Nota**: Dati vecchi non sono compatibili (schema diverso).

## 📜 License

Developed for Smart_Joint Project - STM32 + SIM7000 e-Link System

---

**Version**: 2.0  
**Last Update**: Corretti schema database (tensioni/correnti separate) e integrazione in script corretto  
**Author**: Smart_Joint Development Team
