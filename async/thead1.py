from threading import Thread
import time

def ask_user():
    start = time.time()
    user_input = input('enter: ')
    print(user_input)
    print(time.time()- start)


def complex_cal():
    start = time.time()
    for x in range(2000000):
        x**2
    print(time.time()- start)



thread1 = Thread(target=complex_cal)
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()


print(time.time() - start)
