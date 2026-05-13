#!/usr/bin/env python3
"""
Test script per verificare il sistema di risposte dispositivi
"""

from db_manager import get_db

# Testa inserimento risposte
db = get_db()

print("🧪 Testing device response system...")

# Simula alcune risposte come quelle che arriverebbero dal dispositivo
test_responses = [
    "R:PNG_REPLY",  # Risposta semplice a ping
    "R:1,768,24,11,7,14,30,45,3276,100,5,3280,3290,3300,8192,8100,8050,1024",  # Info completa device 1
    "R:0,512,24,11,7,15,10,30,3200,50,3,3250,3260,3270,7900,7800,7700,950"   # Info completa device 0
]

for response in test_responses:
    print(f"💾 Inserting response: {response[:50]}...")
    db.insert_device_response(None, response)

print("✅ Test responses inserted successfully!")

# Verifica le risposte inserite
print("\n📋 Recent responses:")
responses = db.get_recent_responses(limit=5)

for i, resp in enumerate(responses, 1):
    print(f"\n{i}. Response ID: {resp['id']}")
    print(f"   Device: {resp['device_id']}")
    print(f"   Type: {resp['response_type']}")
    print(f"   Timestamp: {resp['timestamp']}")
    if resp['parsed_data']:
        print(f"   Data: {resp['parsed_data'][:100]}...")

print(f"\n🔢 Total responses in database: {len(responses)}")
print("🌐 Now check the web interface!")