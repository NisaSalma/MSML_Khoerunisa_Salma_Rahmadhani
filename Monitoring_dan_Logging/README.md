Monitoring dan Model Serving

1. Model Serving
Model disajikan menggunakan FastAPI dengan endpoint /predict.
Uvicorn berjalan di port 8000.

2. Monitoring Prometheus
Metrics yang dimonitor:
- request_count_total
- request_processing_seconds
- error_count_total

3. Monitoring Grafana
Grafana digunakan untuk visualisasi metrics request count, latency, dan error.

4. Alerting
Alert dibuat ketika error_count_total > 0 dan status alert berhasil firing.
