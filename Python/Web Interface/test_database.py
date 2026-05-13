"""
Test script per verificare il database e creare dati di test se necessario
"""

import sys
from pathlib import Path

# Aggiungi path per import moduli
sys.path.append(str(Path(__file__).parent))

from db_manager import get_db

def test_database():
    """Testa il database e crea dati di test se necessario"""
    print("🔧 Test database e-Link...")
    
    try:
        db = get_db()
        print("✅ Database inizializzato correttamente")
        
        # Test get_connected_devices
        try:
            devices = db.get_connected_devices()
            print(f"📱 Dispositivi connessi: {len(devices)}")
            for device in devices:
                print(f"   - Device {device['device_id']}: {device['ip_address']}")
        except Exception as e:
            print(f"❌ Errore get_connected_devices: {e}")
        
        # Test get_db_stats
        try:
            stats = db.get_db_stats()
            print(f"📊 Statistiche database: {stats}")
        except Exception as e:
            print(f"❌ Errore get_db_stats: {e}")
        
        # Se non ci sono dispositivi, crea dati di test
        if len(devices) == 0:
            print("🧪 Creando dati di test...")
            create_test_data(db)
            
    except Exception as e:
        print(f"❌ Errore generale database: {e}")

def create_test_data(db):
    """Crea dati di test per il database"""
    try:
        # Aggiungi dispositivo di test
        db.update_device_status(1, "192.168.1.100", "connected")
        
        # Aggiungi telemetria di test
        import time
        test_data = {
            'device_id': 1,
            'pressure': 2.5,
            'flow': 1.2,
            'ax': 100.0,
            'ay': -50.0,
            'az': 980.0,
            'vbatt': 3.7,
            'v1': 3.3,
            'v2': 5.0,
            'v3': 12.0,
            'i1': 0.150,
            'i2': 0.280,
            'i3': 0.050,
            'temperature': 25.4
        }
        
        db.add_telemetry(**test_data)
        print("✅ Dati di test creati")
        
    except Exception as e:
        print(f"❌ Errore creazione dati di test: {e}")

if __name__ == "__main__":
    test_database()