#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = a + b
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/mul', methods=['GET'])
def mul_numbers():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = a * b
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    # Bind ke semua interface agar bisa diakses dari container
    app.run(debug=True, host='0.0.0.0', port=5150)
