import random
import time

def dummy():
    n = random.random() / 100
    time.sleep(n)

if __name__ == '__main__':
    for _ in range(1000):
        dummy()