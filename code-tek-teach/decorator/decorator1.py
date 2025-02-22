import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'the {func.__name__} took {end-start} sec')
        return result
    return wrapper

@time_it
def some_op():
    print('starting')
    time.sleep(1)
    print('ending')
    return 123


some_op()