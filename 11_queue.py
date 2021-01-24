import time, queue, threading, random
from my_modules.file_utilities import find_all_files

file_list = []
find_all_files(r"D:\_PythonSuli\pycore-210109-2", file_list)

job_list = queue.Queue()
for f in file_list:
    job_list.put(f)


def file_worker():
    while not job_list.empty():
        next_file = job_list.get()
        print(f"{threading.currentThread().name} working on {next_file}")
        time.sleep(random.randint(1, 10))


for _ in range(1):
    t = threading.Thread(target=file_worker)
    t.start()