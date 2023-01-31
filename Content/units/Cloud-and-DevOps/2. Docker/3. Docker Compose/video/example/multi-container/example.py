import random
import psycopg2
from time import sleep

if __name__ == "__main__":

    conn = psycopg2.connect(
        host="database",
        database="postgres",
        user="postgres",
        password="example")

    while True:
        sleep(1)
        print("I'm still connected")
