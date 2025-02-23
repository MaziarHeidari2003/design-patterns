from threading import Thread
import time
from concurrent.futures import ThreadPoolExecutor

def ask_user():
    start = time.time()
    user_input = input('enter: ')
    print(user_input)
    print(time.time()- start)


def complex_cal():
    start = time.time()
    for x in range(20000000):
        x**2
    print(time.time()- start)



start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_cal)
    pool.submit(ask_user)


print(time.time() - start)
