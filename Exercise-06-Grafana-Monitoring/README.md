# Exercise 06: Grafana Real-Time Monitoring of Quick-Commerce App

## Objective
Build an end-to-end real-time operational monitoring and alerting pipeline for a quick-commerce delivery application ("ZAPPTTO") using Python, Prometheus, Grafana, and Jenkins. The pipeline simulates delivery metrics, exposes them via HTTP, scrapes them into Prometheus, visualizes them with Grafana dashboards, and configures alert rules for high pending deliveries.

---

## Directory Structure and Files
```text
Exercise-06-Grafana-Monitoring/
├── delivery_metrics.py     # Python simulation script exposing Prometheus metrics on port 8000
├── prometheus.yml          # Prometheus scrape configuration targeting Prometheus & delivery app
├── alert_rules.yml         # Prometheus alerting rules (HighPendingDeliveries, HighAverageDeliveryTime)
├── Jenkinsfile             # Pipeline definition automating testing and monitoring deployment
├── dashboard.json          # Grafana dashboard definition (Delivery Monitoring with 4 panels)
├── README.md               # Documentation and test results
└── screenshots/            # Verification screenshots
    ├── 01-metrics-endpoint.png
    ├── 02-prometheus-targets.png
    ├── 03-grafana-prometheus.png
    ├── 04-grafana-dashboard.png
    └── 05-prometheus-alerts.png
```

---

## Architecture & Implementation Details

1. **Metrics Application (`delivery_metrics.py`)**:
   - Exposes operational metrics using the `prometheus-client` library on port `8000`:
     - `total_deliveries`: Gauge representing total volume.
     - `pending_deliveries`: Gauge tracking pending delivery backlog.
     - `on_the_way_deliveries`: Gauge for active in-transit orders.
     - `average_delivery_time`: Summary tracking delivery latency in seconds.
   - Continuously simulates live quick-commerce operations.

2. **Prometheus Configuration (`prometheus.yml` & `alert_rules.yml`)**:
   - Scrapes `localhost:9090` (Prometheus) and `host.docker.internal:8000` (delivery service) every 5 seconds.
   - Evaluates alerting rules:
     - `HighPendingDeliveries`: Triggers warning when `pending_deliveries > 10` for more than 15s.
     - `HighAverageDeliveryTime`: Triggers critical alert when average delivery time exceeds 30s.

3. **Grafana Visualization (`dashboard.json`)**:
   - Connected to Prometheus data source at `http://prometheus:9090`.
   - **Delivery Monitoring Dashboard** with 4 real-time stat panels:
     - Total Deliveries (`total_deliveries`)
     - Pending Deliveries (`pending_deliveries`)
     - On-the-Way Deliveries (`on_the_way_deliveries`)
     - Average Delivery Time (`average_delivery_time_sum / average_delivery_time_count`)

4. **Jenkins Automation (`Jenkinsfile`)**:
   - Adapted pipeline for container orchestration, health pre-checks, metrics simulation, and automated alert validation.

---

## Commands to Run

### 1. Install Requirements and Run Metrics App
```powershell
pip install prometheus-client
python delivery_metrics.py
```
Endpoint verified at `http://localhost:8000/metrics`.

### 2. Run Prometheus in Docker
```powershell
docker run -d --name prometheus --network monitoring -p 9090:9090 `
  -v "${PWD}\prometheus.yml:/etc/prometheus/prometheus.yml" `
  -v "${PWD}\alert_rules.yml:/etc/prometheus/alert_rules.yml" `
  prom/prometheus
```
Target health verified at `http://localhost:9090/targets`.

### 3. Run Grafana in Docker
```powershell
docker run -d --name grafana --network monitoring -p 3000:3000 grafana/grafana
```
Accessible at `http://localhost:3000` (Admin login credentials configured).

---

## Verification & Screenshot Evidence

| Evidence | Screenshot File | Description |
|---|---|---|
| **Metrics Endpoint** | `screenshots/01-metrics-endpoint.png` | Verifies `/metrics` HTTP endpoint exposing raw Prometheus metrics |
| **Prometheus Targets** | `screenshots/02-prometheus-targets.png` | Shows both scrape targets (`prometheus` and `delivery_service`) in `UP` state |
| **Grafana Prometheus Data Source** | `screenshots/03-grafana-prometheus.png` | Confirms successful data source connection to `http://prometheus:9090` |
| **Grafana Dashboard** | `screenshots/04-grafana-dashboard.png` | Displays live "Delivery Monitoring" dashboard with all 4 operational panels |
| **Prometheus Alerts** | `screenshots/05-prometheus-alerts.png` | Confirms `HighPendingDeliveries` alert actively evaluating and firing |

---

## Test Results Summary
- **Metrics App**: Running and successfully publishing live metric streams.
- **Scrape Targets**: Prometheus successfully scrapes the Python app via `host.docker.internal:8000`.
- **Grafana**: Dashboard connected, active, and rendering real-time data panels.
- **Alerting**: Alert rule verified; `HighPendingDeliveries` successfully entered firing state when pending orders exceeded threshold.
