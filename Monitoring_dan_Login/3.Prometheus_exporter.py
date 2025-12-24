import random
import time
from prometheus_client import Counter, Summary, start_http_server

# Jumlah request
REQUEST_COUNT = Counter('request_count', 'Total number of requests')
REQUEST_LATENCY = Summary('request_processing_seconds', 'Request latency in seconds')
ERROR_COUNT = Counter('error_count', 'Total number of errors')

# Fungsi simulasi prediksi
def process_request():
    REQUEST_COUNT.inc()
    if random.random() < 0.1:
        ERROR_COUNT.inc()
    with REQUEST_LATENCY.time():
        time.sleep(random.random())

if __name__ == '__main__':
    # Jalankan exporter di port 8001
    start_http_server(8001)
    print("Prometheus exporter running on port 8001")
    while True:
        process_request()