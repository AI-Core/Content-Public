from prometheus_client import Summary, start_http_server, Counter

counter = Counter("my_metric", "A fantastic metric")

if __name__ == "__main__":
    start_http_server(9090)
    while True:
        counter.inc(1)
