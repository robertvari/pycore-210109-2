import time, logging, getpass
from datetime import datetime


def my_timer(func):

    def wrapper(*args, **kwargs):
        print("my_timer started!")
        start_time = time.time()

        result = func(*args, **kwargs)

        print(f"Runtime: {time.time() - start_time}")

    return wrapper


def my_logger(func):
    logging.basicConfig(filename="my_logger.txt", level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f"{datetime.now()}. {func.__name__} Args: {args, kwargs}. User: {getpass.getuser()}")
        func(*args, **kwargs)

    return wrapper
