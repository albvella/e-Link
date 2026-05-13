"""
Database Manager per e-Link Web Interface
Gestisce telemetria con buffer circolare di 1 ora per device
"""

import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
import threading
import atexit
import time

class TelemetryDB:
    def __init__(self, db_path: str = "../data/elink.db"):
        """
        Inizializza database SQLite con buffer circolare 1h per device.
        
        Args:
            db_path: Path al file database SQLite
        """
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.lock = threading.Lock()
        self._connection_cache = {}
        self._last_cleanup = time.time()
        
        # Registra cleanup automatico all'uscita
        atexit.register(self.cleanup_connections)
        
        self._init_db()
    
    def _init_db(self):
        """Crea schema database se non esiste"""
        with sqlite3.connect(str(self.db_path)) as conn:
            cursor = conn.cursor()
            
            # Tabella telemetria con timestamp server-side
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS telemetry (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    device_id INTEGER NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    pressure REAL,
                    flow REAL,
                    ax REAL,
                    ay REAL,
                    az REAL,
                    vbatt REAL,
                    v1 REAL,
                    v2 REAL,
                    v3 REAL,
                    i1 REAL,
                    i2 REAL,
                    i3 REAL,
                    temperature REAL
                )
            """)
            
            # Indice per query veloci per device e timestamp
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_device_timestamp 
                ON telemetry(device_id, timestamp DESC)
            """)
            
            # Tabella dispositivi connessi
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS devices (
                    device_id INTEGER PRIMARY KEY,
                    last_seen DATETIME,
                    status TEXT,
                    ip_address TEXT
                )
            """)
            
            # Tabella comandi in coda per invio ai dispositivi
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS command_queue (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    device_id INTEGER NOT NULL,
                    command TEXT NOT NULL,
                    parameters TEXT,
                    status TEXT DEFAULT 'pending',
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    sent_at DATETIME,
                    response TEXT,
                    source TEXT DEFAULT 'web_interface'
                )
            """)
            
            # Tabella risposte dispositivi (formattate come in eLink_Client_Control)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS device_responses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    device_id INTEGER,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    response_type TEXT,
                    raw_data TEXT,
                    parsed_data TEXT,
                    firmware_version REAL,
                    uptime TEXT,
                    vbatt REAL,
                    sampling_freq INTEGER,
                    buffering INTEGER,
                    v1 REAL,
                    v2 REAL,
                    v3 REAL,
                    i1 REAL,
                    i2 REAL,
                    i3 REAL,
                    temperature REAL
                )
            """)
            
            # Indice per query veloci sui comandi pending
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_command_status 
                ON command_queue(status, device_id, created_at)
            """)
            
            # Indice per risposte per device e timestamp
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_responses_device_timestamp 
                ON device_responses(device_id, timestamp DESC)
            """)
            
            conn.commit()
    
    def get_connection(self):
        """
        Ottiene connessione database thread-safe con timeout.
        """
        # Cleanup connessioni vecchie ogni 5 minuti
        current_time = time.time()
        if current_time - self._last_cleanup > 300:  # 5 minuti
            self.cleanup_old_connections()
            self._last_cleanup = current_time
            
        conn = sqlite3.connect(
            str(self.db_path),
            timeout=30.0,  # Timeout di 30 secondi
            check_same_thread=False
        )
        # Abilita WAL mode per migliori prestazioni concurrent
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA busy_timeout=30000")  # 30 secondi busy timeout
        return conn
    
    def cleanup_old_connections(self):
        """Pulisce connessioni cache vecchie"""
        thread_id = threading.get_ident()
        if thread_id in self._connection_cache:
            try:
                self._connection_cache[thread_id].close()
            except:
                pass
            del self._connection_cache[thread_id]
    
    def cleanup_connections(self):
        """Pulisce tutte le connessioni cache all'uscita"""
        with self.lock:
            for conn in self._connection_cache.values():
                try:
                    conn.close()
                except:
                    pass
            self._connection_cache.clear()
    
    def insert_telemetry(self, device_id: int, data: dict):
        """
        Inserisce nuovo record telemetria e rimuove dati più vecchi di 1h.
        
        Args:
            device_id: ID dispositivo
            data: dict con chiavi: pressure, flow, ax, ay, az, vbatt, v1, v2, v3, i1, i2, i3, temperature
        """
        with self.lock:
            conn = self.get_connection()
            try:
                cursor = conn.cursor()
                
                # Inserisci nuovo record
                cursor.execute("""
                    INSERT INTO telemetry 
                    (device_id, pressure, flow, ax, ay, az, vbatt, v1, v2, v3, i1, i2, i3, temperature)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    device_id,
                    data.get('pressure'),
                    data.get('flow'),
                    data.get('ax'),
                    data.get('ay'),
                    data.get('az'),
                    data.get('vbatt'),
                    data.get('v1'),
                    data.get('v2'),
                    data.get('v3'),
                    data.get('i1'),
                    data.get('i2'),
                    data.get('i3'),
                    data.get('temperature')
                ))
                
                # Rimuovi dati più vecchi di 1 ora (buffer circolare)
                one_hour_ago = datetime.now() - timedelta(hours=1)
                cursor.execute("""
                    DELETE FROM telemetry 
                    WHERE device_id = ? AND timestamp < ?
                """, (device_id, one_hour_ago))
                
                conn.commit()
            finally:
                conn.close()
    
    def get_telemetry(self, device_id: int, minutes: int = 60):
        """
        Recupera telemetria degli ultimi N minuti per un device.
        
        Args:
            device_id: ID dispositivo
            minutes: Numero di minuti da recuperare (default 60 = 1h)
            
        Returns:
            list[dict]: Lista di record telemetria
        """
        with sqlite3.connect(str(self.db_path)) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            time_ago = datetime.now() - timedelta(minutes=minutes)
            
            cursor.execute("""
                SELECT 
                    timestamp,
                    pressure,
                    flow,
                    ax, ay, az,
                    vbatt, v1, v2, v3,
                    i1, i2, i3,
                    temperature
                FROM telemetry
                WHERE device_id = ? AND timestamp >= ?
                ORDER BY timestamp ASC
            """, (device_id, time_ago))
            
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
    
    def get_latest_telemetry(self, device_id: int):
        """
        Recupera l'ultimo record telemetria per un device.
        
        Args:
            device_id: ID dispositivo
            
        Returns:
            dict | None: Ultimo record o None se non esistente
        """
        with sqlite3.connect(str(self.db_path)) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT 
                    timestamp,
                    pressure,
                    flow,
                    ax, ay, az,
                    vbatt, v1, v2, v3,
                    i1, i2, i3,
                    temperature
                FROM telemetry
                WHERE device_id = ?
                ORDER BY timestamp DESC
                LIMIT 1
            """, (device_id,))
            
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def update_device_status(self, device_id: int, status: str, ip_address: str = None):
        """
        Aggiorna stato dispositivo (connesso/disconnesso).
        
        Args:
            device_id: ID dispositivo
            status: Stato ("connected", "disconnected")
            ip_address: Indirizzo IP del dispositivo
        """
        with self.lock:
            with sqlite3.connect(str(self.db_path)) as conn:
                cursor = conn.cursor()
                
                # Prima prova a fare UPDATE
                cursor.execute("""
                    UPDATE devices 
                    SET last_seen = CURRENT_TIMESTAMP, status = ?, ip_address = ?
                    WHERE device_id = ?
                """, (status, ip_address, device_id))
                
                # Se non ha aggiornato nessuna riga, fai INSERT
                if cursor.rowcount == 0:
                    cursor.execute("""
                        INSERT INTO devices (device_id, last_seen, status, ip_address)
                        VALUES (?, CURRENT_TIMESTAMP, ?, ?)
                    """, (device_id, status, ip_address))
                
                conn.commit()
    
    def get_connected_devices(self):
        """
        Recupera lista dispositivi connessi (visti negli ultimi 5 minuti).
        
        Returns:
            list[dict]: Lista dispositivi con device_id, last_seen, status, ip_address
        """
        with sqlite3.connect(str(self.db_path)) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            five_min_ago = datetime.now() - timedelta(minutes=5)
            
            cursor.execute("""
                SELECT device_id, last_seen, status, ip_address
                FROM devices
                WHERE last_seen >= ? AND status = 'connected'
                ORDER BY device_id ASC
            """, (five_min_ago,))
            
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
    
    def cleanup_old_data(self):
        """
        Pulizia manuale di tutti i dati più vecchi di 1h.
        Viene chiamata automaticamente ad ogni inserimento, ma può essere utile per manutenzione.
        """
        with self.lock:
            with sqlite3.connect(str(self.db_path)) as conn:
                cursor = conn.cursor()
                
                one_hour_ago = datetime.now() - timedelta(hours=1)
                
                cursor.execute("""
                    DELETE FROM telemetry WHERE timestamp < ?
                """, (one_hour_ago,))
                
                deleted = cursor.rowcount
                conn.commit()
                
                return deleted
    
    def get_db_stats(self):
        """
        Statistiche database per monitoring.
        
        Returns:
            dict: Statistiche (total_records, devices_count, oldest_record, newest_record)
        """
        with sqlite3.connect(str(self.db_path)) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Conteggio totale record
            cursor.execute("SELECT COUNT(*) as total FROM telemetry")
            total_records = cursor.fetchone()['total']
            
            # Numero dispositivi unici
            cursor.execute("SELECT COUNT(DISTINCT device_id) as count FROM telemetry")
            devices_count = cursor.fetchone()['count']
            
            # Record più vecchio e più recente
            cursor.execute("SELECT MIN(timestamp) as oldest, MAX(timestamp) as newest FROM telemetry")
            times = cursor.fetchone()
            
            return {
                'total_records': total_records,
                'devices_count': devices_count,
                'oldest_record': times['oldest'],
                'newest_record': times['newest']
            }
    
    # =================== GESTIONE CODA COMANDI ===================
    
    def queue_command(self, device_id: int, command: str, parameters: str = None, source: str = 'web_interface') -> int:
        """
        Aggiunge comando alla coda per invio al dispositivo.
        
        Args:
            device_id: ID dispositivo target (0 per broadcast)
            command: Comando da inviare (es: "SRT", "IDL", "PNG")  
            parameters: Parametri aggiuntivi (es: per SET/GET)
            source: Sorgente comando (web_interface, api, etc)
            
        Returns:
            ID del comando inserito
        """
        with self.lock:
            with sqlite3.connect(str(self.db_path)) as conn:
                cursor = conn.cursor()
                
                cursor.execute("""
                    INSERT INTO command_queue (device_id, command, parameters, source)
                    VALUES (?, ?, ?, ?)
                """, (device_id, command, parameters, source))
                
                command_id = cursor.lastrowid
                conn.commit()
                
                print(f"📝 Comando accodato: {command} → Device {device_id} (ID: {command_id})")
                return command_id
    
    def get_pending_commands(self, device_id: int = None) -> list:
        """
        Ottiene comandi in attesa di invio.
        
        Args:
            device_id: Se specificato, filtra per dispositivo
            
        Returns:
            Lista di dict con comando details
        """
        with self.lock:
            with sqlite3.connect(str(self.db_path)) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                if device_id is not None:
                    cursor.execute("""
                        SELECT * FROM command_queue 
                        WHERE status = 'pending' AND (device_id = ? OR device_id = 0)
                        ORDER BY created_at ASC
                    """, (device_id,))
                else:
                    cursor.execute("""
                        SELECT * FROM command_queue 
                        WHERE status = 'pending'
                        ORDER BY created_at ASC
                    """)
                
                return [dict(row) for row in cursor.fetchall()]
    
    def mark_command_sent(self, command_id: int, response: str = None):
        """
        Marca comando come inviato con eventuale risposta.
        
        Args:
            command_id: ID del comando
            response: Risposta ricevuta dal dispositivo
        """
        with self.lock:
            with sqlite3.connect(str(self.db_path)) as conn:
                cursor = conn.cursor()
                
                cursor.execute("""
                    UPDATE command_queue 
                    SET status = 'sent', sent_at = CURRENT_TIMESTAMP, response = ?
                    WHERE id = ?
                """, (response, command_id))
                
                conn.commit()
    
    def mark_command_failed(self, command_id: int, error: str = None):
        """
        Marca comando come fallito.
        
        Args:
            command_id: ID del comando
            error: Messaggio di errore
        """
        with self.lock:
            with sqlite3.connect(str(self.db_path)) as conn:
                cursor = conn.cursor()
                
                cursor.execute("""
                    UPDATE command_queue 
                    SET status = 'failed', sent_at = CURRENT_TIMESTAMP, response = ?
                    WHERE id = ?
                """, (error, command_id))
                
                conn.commit()
    
    def get_command_history(self, device_id: int = None, limit: int = 50) -> list:
        """
        Ottiene storico comandi inviati.
        
        Args:
            device_id: Se specificato, filtra per dispositivo
            limit: Numero massimo risultati
            
        Returns:
            Lista comandi ordinata per timestamp desc
        """
        with self.lock:
            with sqlite3.connect(str(self.db_path)) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                if device_id is not None:
                    cursor.execute("""
                        SELECT * FROM command_queue 
                        WHERE device_id = ? OR device_id = 0
                        ORDER BY created_at DESC
                        LIMIT ?
                    """, (device_id, limit))
                else:
                    cursor.execute("""
                        SELECT * FROM command_queue 
                        ORDER BY created_at DESC
                        LIMIT ?
                    """, (limit,))
                
                return [dict(row) for row in cursor.fetchall()]

    def insert_device_response(self, device_id: int, raw_data: str):
        """
        Inserisce risposta dispositivo parsata come in eLink_Client_Control.
        
        Args:
            device_id: ID dispositivo (può essere None per risposte senza ID)
            raw_data: Dati grezzi della risposta
        """
        import json
        
        with self.lock:
            with sqlite3.connect(str(self.db_path)) as conn:
                cursor = conn.cursor()
                
                # Parsing come in eLink_Client_Control rx_handler
                parsed_data = None
                response_type = "simple"
                
                try:
                    if raw_data.startswith('R:'):
                        data_str = raw_data[2:].strip()
                        parts = data_str.split(",")
                        
                        # Check if this looks like a full info response (many comma-separated values)
                        if len(parts) >= 17:
                            try:
                                from datetime import datetime
                                parsed_info = {
                                    "ID": int(parts[0]),
                                    "Firmware Version": round(float("{}.{}".format(int(parts[1]) >> 8, int(parts[1]) & 0xFF)), 4),
                                    "Uptime": str(datetime(year=int(parts[2]) + 2000, month=int(parts[3]), day=int(parts[4]), hour=int(parts[5]), minute=int(parts[6]), second=int(parts[7]))),
                                    "Vbatt [V]": f"{int(parts[8]) * 0.001:.4f}",
                                    "Sampling Freq [Hz]": int(parts[9]),
                                    "Buffering [s]": int(parts[10]),
                                    "V1 [V]": f"{int(parts[11]) * 0.001:.4f}",
                                    "V2 [V]": f"{int(parts[12]) * 0.001:.4f}",
                                    "V3 [V]": f"{int(parts[13]) * 0.001:.4f}",
                                    "I1 [A]": f"{((((int(parts[14]) >> 3) if int(parts[14]) < 0x8000 else (int(parts[14]) - 0x10000) >> 3) * 0.00004 / 0.08)):.4f}",
                                    "I2 [A]": f"{((((int(parts[15]) >> 3) if int(parts[15]) < 0x8000 else (int(parts[15]) - 0x10000) >> 3) * 0.00004 / 0.08)):.4f}",
                                    "I3 [A]": f"{((((int(parts[16]) >> 3) if int(parts[16]) < 0x8000 else (int(parts[16]) - 0x10000) >> 3) * 0.00004 / 0.08)):.4f}",
                                    "Temp [°C]": f"{(int(parts[17]) * 0.0625 if int(parts[17]) < 0x8000 else (int(parts[17]) - 0x10000) * 0.0625):.4f}"
                                }
                                
                                response_type = "full_info"
                                parsed_data = json.dumps(parsed_info)
                                device_id = parsed_info["ID"]
                                
                                cursor.execute("""
                                    INSERT INTO device_responses 
                                    (device_id, response_type, raw_data, parsed_data, 
                                     firmware_version, uptime, vbatt, sampling_freq, buffering,
                                     v1, v2, v3, i1, i2, i3, temperature)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                """, (
                                    device_id, response_type, raw_data, parsed_data,
                                    parsed_info["Firmware Version"], parsed_info["Uptime"], 
                                    float(parsed_info["Vbatt [V]"]), parsed_info["Sampling Freq [Hz]"], 
                                    parsed_info["Buffering [s]"], float(parsed_info["V1 [V]"]),
                                    float(parsed_info["V2 [V]"]), float(parsed_info["V3 [V]"]),
                                    float(parsed_info["I1 [A]"]), float(parsed_info["I2 [A]"]),
                                    float(parsed_info["I3 [A]"]), float(parsed_info["Temp [°C]"])
                                ))
                                
                            except Exception as e:
                                # Fall back to simple response
                                response_type = "simple"
                                parsed_data = data_str
                                cursor.execute("""
                                    INSERT INTO device_responses 
                                    (device_id, response_type, raw_data, parsed_data)
                                    VALUES (?, ?, ?, ?)
                                """, (device_id, response_type, raw_data, parsed_data))
                        else:
                            # Simple response (like ping response)  
                            response_type = "simple"
                            parsed_data = data_str
                            cursor.execute("""
                                INSERT INTO device_responses 
                                (device_id, response_type, raw_data, parsed_data)
                                VALUES (?, ?, ?, ?)
                            """, (device_id, response_type, raw_data, parsed_data))
                    else:
                        # Altri tipi di risposta
                        cursor.execute("""
                            INSERT INTO device_responses 
                            (device_id, response_type, raw_data, parsed_data)
                            VALUES (?, ?, ?, ?)
                        """, (device_id, "unknown", raw_data, raw_data))
                        
                except Exception as e:
                    print(f"❌ Errore parsing risposta: {e}")
                    cursor.execute("""
                        INSERT INTO device_responses 
                        (device_id, response_type, raw_data, parsed_data)
                        VALUES (?, ?, ?, ?)
                    """, (device_id, "error", raw_data, str(e)))
                
                conn.commit()

    def get_recent_responses(self, device_id: int = None, limit: int = 10):
        """
        Recupera risposte recenti dei dispositivi (solo risposte R:, esclude L: e H:).
        
        Args:
            device_id: Filtra per device specifico (None = tutti)
            limit: Numero massimo risposte da restituire
            
        Returns:
            list: Lista risposte formattate
        """
        with sqlite3.connect(str(self.db_path)) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            if device_id is not None:
                cursor.execute("""
                    SELECT * FROM device_responses 
                    WHERE device_id = ? AND response LIKE 'R:%'
                    ORDER BY timestamp DESC
                    LIMIT ?
                """, (device_id, limit))
            else:
                cursor.execute("""
                    SELECT * FROM device_responses 
                    WHERE response LIKE 'R:%'
                    ORDER BY timestamp DESC
                    LIMIT ?
                """, (limit,))
            
            return [dict(row) for row in cursor.fetchall()]

    def cleanup_devices_on_startup(self):
        """
        Marca tutti i dispositivi come disconnessi all'avvio del server.
        Utile per pulire stati inconsistenti dopo riavvio.
        """
        with self.lock:
            with sqlite3.connect(str(self.db_path)) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE devices 
                    SET status = 'disconnected'
                    WHERE status = 'connected'
                """)
                disconnected_count = cursor.rowcount
                conn.commit()
                return disconnected_count


# Istanza singleton globale
_db_instance = None

def get_db() -> TelemetryDB:
    """Ottieni istanza singleton del database"""
    global _db_instance
    if _db_instance is None:
        # Crea percorso relativo alla directory corrente del progetto
        current_dir = Path(__file__).parent
        db_path = current_dir.parent / "data" / "elink.db"
        _db_instance = TelemetryDB(str(db_path))
    return _db_instance
