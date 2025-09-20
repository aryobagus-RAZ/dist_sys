#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UDP Client Oneway
Mengirim pesan ke server tanpa menunggu balasan
"""

import socket
import time

# Buat socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Alamat server → gunakan nama service di docker-compose
server_address = ('udp-server', 12345)

print(" UDP client siap mengirim pesan ke server...")

# Kirim beberapa pesan
for i in range(9):
    message = f"Pesan UDP ke-{i}"
    client_socket.sendto(message.encode('utf-8'), server_address)
    print(f"[SENT] {message}")
    time.sleep(1)

# Tutup socket
client_socket.close()
print(" Semua pesan sudah dikirim (oneway).")
