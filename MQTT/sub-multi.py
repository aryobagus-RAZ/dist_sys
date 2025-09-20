#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Subscriber multi-topik
Menerima data suhu & kelembapan
"""

import paho.mqtt.client as mqtt
import sys

broker = "mqtt-broker"
port = 1883
topics = [("sister/temp", 0), ("sister/hum", 0)]  # QoS = 0

# Callback jika koneksi berhasil
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"✅ Subscriber berhasil terhubung ke broker {broker}")
        client.subscribe(topics)
        print(f"📡 Berlangganan topik: {[t[0] for t in topics]}")
    else:
        print(f"❌ Gagal connect, kode error: {rc}")
        sys.exit(1)

# Callback jika pesan masuk
def on_message(client, userdata, message, properties=None):
    print(f"[{message.topic}] {message.payload.decode()}")

# Inisialisasi client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

try:
    print(f"Menghubungkan ke {broker}:{port} ...")
    client.connect(broker, port, keepalive=60)
except Exception as e:
    print(f"❌ Gagal connect: {e}")
    sys.exit(1)

# Loop forever untuk nunggu pesan
try:
    print("Menunggu pesan... (Ctrl+C untuk berhenti)")
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSubscriber dihentikan.")
    client.disconnect()
