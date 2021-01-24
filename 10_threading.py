import random, time, threading


def worker1(sleep_time):
    print(f"Worker 1 started. {threading.currentThread().name}")
    time.sleep(random.randint(1, sleep_time))
    print("Worker 1 finished")


def worker2(sleep_time):
    print(f"Worker 2 started. {threading.currentThread().name}")
    time.sleep(random.randint(1, sleep_time))
    print("Worker 2 finished")


t1 = threading.Thread(target=worker1, args=[3])
t2 = threading.Thread(target=worker2, args=[10])

t1.start()
t2.start()

print(f"All process finished on {threading.currentThread().name}")