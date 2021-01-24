import time, random
from my_modules.decorators import my_timer, my_logger


@my_timer
@my_logger
def worker1(name, age):
    time.sleep(random.randint(1, 10))
    print(f"Hello {name}. You are {age} old")


worker1("Robert", 32)