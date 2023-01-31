import time


def timer(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        total_time = time.time() - start_time
        print('Total time:', total_time)
    return wrapper


@timer
def my_function(idx):
    for i in range(idx):
        pass


def another_function(idx):
    for i in range(idx + 1000):
        pass


my_function(100)
