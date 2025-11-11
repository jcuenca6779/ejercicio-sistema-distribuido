# scripts/load_test.py
import requests
import time
from threading import Thread

# URL del balanceador de carga 
URL = "http://localhost:80/status"
NUM_REQUESTS = 20
NUM_THREADS = 5

print(f"Iniciando prueba de carga en {URL}...")

results = {
    "servidores_contactados": set(),
    "exitos": 0,
    "errores": 0
}

def make_request():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            results["exitos"] += 1
            # Guardamos el nombre del servidor de app que respondió
            server = response.json().get("servidor_app", "unknown")
            results["servidores_contactados"].add(server)
        else:
            results["errores"] += 1
    except requests.exceptions.ConnectionError:
        results["errores"] += 1

start_time = time.time()
threads = []

for _ in range(NUM_REQUESTS):
    t = Thread(target=make_request)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()

print(f"\n--- Resultados de la Prueba de Carga ---")
print(f"Tiempo total: {end_time - start_time:.2f} segundos")
print(f"Peticiones exitosas: {results['exitos']}")
print(f"Peticiones fallidas: {results['errores']}")
print("\n--- Demostración de Balanceo de Carga ---")
print(f"Servidores de aplicación contactados (deberías ver varios):")
for server in results["servidores_contactados"]:
    print(f"  -> {server}")