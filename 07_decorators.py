import time, random


def my_timer(func):

    def wrapper(*args, **kwargs):
        print("my_timer started!")
        start_time = time.time()

        result = func(*args, **kwargs)

        print(f"Runtime: {time.time() - start_time}")

    return wrapper


@my_timer
def worker1(name, age):
    time.sleep(random.randint(1, 10))
    print(f"Hello {name}. You are {age} old")


worker1("Robert", 32)