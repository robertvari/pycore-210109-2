import random, time


def worker1():
    print("Worker 1 started")
    time.sleep(random.randint(1, 10))
    print("Worker 1 finished")


def worker2():
    print("Worker 2 started")
    time.sleep(random.randint(1, 10))
    print("Worker 2 finished")