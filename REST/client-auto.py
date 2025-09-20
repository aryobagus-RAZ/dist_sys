#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time

BASE = "http://rest-server:5150"

def call(endpoint, a, b):
    try:
        r = requests.get(f"{BASE}/{endpoint}", params={'a': a, 'b': b}, timeout=3)
        if r.status_code == 200:
            data = r.json()
            print(f"[AUTO] {endpoint}({a},{b}) = {data['result']}")
        else:
            print(f"[AUTO] {endpoint} error {r.status_code}: {r.text}")
    except Exception as e:
        print(f"[AUTO] {endpoint} exception: {e}")

def run_auto():
    # Coba beberapa operasi otomatis
    test_cases = [
        ("add", 3, 5),
        ("mul", 7, 6),
        ("add", 10, 20),
        ("mul", 4, 9),
    ]

    for op, a, b in test_cases:
        call(op, a, b)
        time.sleep(1)  # jeda biar lebih jelas

if __name__ == "__main__":
    run_auto()
