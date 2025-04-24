
from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/simulador')
def simulador():
    return render_template('simulador.html')

@app.route('/data/<path:filename>')
def serve_data(filename):
    return send_from_directory('data', filename)

if __name__ == '__main__':
    app.run(debug=True)
