#!/usr/bin/env python3
"""
Script di pulizia database e-Link
Risolve problemi di lock e connessioni orfane
"""

import os
import subprocess
import sys
from pathlib import Path

def find_db_locks():
    """Trova processi che hanno lock sul database"""
    db_path = Path(__file__).parent / "../data/elink.db"
    
    try:
        result = subprocess.run(['lsof', str(db_path)], 
                              capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            print("🔒 Database locks trovati:")
            print(result.stdout)
            return True
        else:
            print("✅ Nessun lock sul database")
            return False
    except FileNotFoundError:
        print("⚠️ Comando lsof non disponibile")
        return False

def cleanup_database():
    """Pulisce connessioni database orfane"""
    db_path = Path(__file__).parent / "../data/elink.db"
    
    if find_db_locks():
        print("\n🧹 Pulizia database in corso...")
        
        try:
            # Forza chiusura connessioni
            subprocess.run(['fuser', '-k', str(db_path)], 
                         capture_output=True)
            print("✅ Connessioni database chiuse")
        except FileNotFoundError:
            print("⚠️ Comando fuser non disponibile")
            
        # Verifica pulizia
        if not find_db_locks():
            print("🎉 Database pulito con successo!")
        else:
            print("❌ Alcuni lock potrebbero persistere")

def kill_elink_processes():
    """Termina tutti i processi eLink attivi"""
    print("🔄 Controllo processi eLink...")
    
    try:
        result = subprocess.run(['pgrep', '-f', 'eLink'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            pids = result.stdout.strip().split('\n')
            print(f"🛑 Terminando {len(pids)} processi eLink...")
            
            for pid in pids:
                subprocess.run(['kill', '-TERM', pid], 
                             capture_output=True)
            
            print("✅ Processi eLink terminati")
        else:
            print("✅ Nessun processo eLink attivo")
    except FileNotFoundError:
        print("⚠️ Comando pgrep non disponibile")

def main():
    """Main cleanup routine"""
    print("🚀 e-Link Database Cleanup Tool")
    print("=" * 40)
    
    kill_elink_processes()
    cleanup_database()
    
    print("\n🎯 Pulizia completata!")
    print("Ora puoi avviare eLink_Client_Control o il daemon")

if __name__ == "__main__":
    if os.name != 'posix':
        print("❌ Questo script funziona solo su Linux/Unix")
        sys.exit(1)
    
    main()