FROM prom/prometheus

# prometheus.yml is the default path from which Prometheus will take the config
COPY prometheus-nodes.yml /etc/prometheus/prometheus.yml

# outline which ports should be mapped
EXPOSE 9090
