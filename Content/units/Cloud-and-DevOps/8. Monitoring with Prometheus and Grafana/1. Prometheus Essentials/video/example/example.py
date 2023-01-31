import random
from time import sleep
from prometheus_client import start_http_server, Counter


counter = Counter("my_metric", "A fantastic metric")

if __name__ == "__main__":

    start_http_server(9100)
    while True:
        sleep(1)
        counter.inc(random.randint(0, 10))
