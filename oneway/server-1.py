#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UDP Server Oneway
Menerima pesan dari client, hanya print ke layar
"""

import socket

# Buat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind ke semua IP (0.0.0.0) dan port 12345
server_socket.bind(('0.0.0.0', 12345))

print(" UDP server (oneway) listening on port 12345")

while True:
    # Terima data dari client
    data, client_address = server_socket.recvfrom(1024)
    print(f"[RECEIVED] dari {client_address} : {data.decode('utf-8')}")
