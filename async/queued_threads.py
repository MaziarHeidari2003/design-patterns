import time 
import random
import queue
from threading import Thread


counter = 0
job_queue = queue.Queue()
counter_queue = queue.Queue()


def increment_manager():
    global counter
    while True:
        increment = counter_queue.get()
        time.sleep(random.random())
        old_counter = counter
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put((f'New counter value is {counter}', '------'))
        counter_queue.task_done()


Thread(target=increment_manager, daemon=True).start()


def printer_manager():
    while True:
        for line in job_queue.get():
            time.sleep(random.random())
            print(line)
        job_queue.task_done()

Thread(target=printer_manager, daemon=True).start()


def increment_counter():
    counter_queue.put(1)


worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join()


counter_queue.join()
job_queue.join()

