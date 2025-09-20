

"""
Publisher multi-topik
Mengirim data suhu & kelembapan secara acak
"""

import paho.mqtt.client as mqtt
import time
import random
import sys

broker = "mqtt-broker"   # nama service broker di docker-compose
port = 1883

# Callback jika berhasil konek
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"✅ Publisher berhasil terhubung ke broker {broker}")
    else:
        print(f"❌ Gagal connect, kode error: {rc}")
        sys.exit(1)

# Inisialisasi client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

try:
    print(f"Menghubungkan ke {broker}:{port} ...")
    client.connect(broker, port, keepalive=60)
except Exception as e:
    print(f"❌ Gagal connect: {e}")
    sys.exit(1)

# Loop publish data acak
try:
    while True:
        suhu = random.randint(25, 35)
        hum = random.randint(40, 70)

        client.publish("sister/temp", f"Suhu: {suhu}°C")
        client.publish("sister/hum", f"Kelembapan: {hum}%")

        print(f"Published → Temp: {suhu}°C | Hum: {hum}%")
        time.sleep(2)

except KeyboardInterrupt:
    print("\nPublisher dihentikan.")
    client.disconnect()
