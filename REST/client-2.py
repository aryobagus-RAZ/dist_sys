#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

BASE = "http://rest-server:5150"

def call(endpoint, a, b):
    try:
        r = requests.get(f"{BASE}/{endpoint}", params={'a': a, 'b': b}, timeout=3)
        if r.status_code == 200:
            data = r.json()
            print(f"{endpoint}({a},{b}) = {data['result']}")
        else:
            print(f"{endpoint} error {r.status_code}: {r.text}")
    except Exception as e:
        print(f"{endpoint} exception: {e}")

def main():
    print("Manual REST Client (ketik 'exit' untuk keluar)")
    while True:
        op = input("Pilih operasi (add/mul): ").strip()
        if op.lower() == "exit":
            break
        a = input("Masukkan angka a: ")
        b = input("Masukkan angka b: ")
        if not a.isdigit() or not b.isdigit():
            print("Input harus angka!")
            continue
        call(op, int(a), int(b))

if __name__ == "__main__":
    main()
