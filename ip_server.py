from flask import Flask, jsonify
import socket, requests

app = Flask(__name__)

@app.route('/local-ip')
def local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return jsonify({"local_ip": ip_address})

@app.route('/public-ip')
def public_ip():
    ip = requests.get('https://api.ipify.org').text
    return jsonify({"public_ip": ip})

@app.route('/ping')
def ping():
    return jsonify({"ping": "Server running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
