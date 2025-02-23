from threading import Thread
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import process

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
print(time.time() - start)
