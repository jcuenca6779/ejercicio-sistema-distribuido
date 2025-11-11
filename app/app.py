# app/app.py
from flask import Flask, jsonify
from pymongo import MongoClient
import os # Importado para obtener el nombre del host

app = Flask(__name__) # Corregido de _name_

# Obtenemos el nombre del contenedor para saber qué réplica nos responde
HOSTNAME = os.environ.get('HOSTNAME', 'unknown')

def get_db_connection():
    # Esta es la cadena de conexión para el REPLICA SET 
    client = MongoClient('mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0')
    return client.test_database

@app.route('/')
def hello():
    return f"Aplicación servida por: {HOSTNAME}"

@app.route('/status')
def status():
    try:
        db = get_db_connection()
        db.command('ping')
        return jsonify({
            "status": "Conectado a MongoDB", 
            "servidor_app": HOSTNAME, 
            "db_primary": db.client.primary
        })
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e), "servidor_app": HOSTNAME})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)