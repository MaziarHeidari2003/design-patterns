def countdown(n):
    while n > 0:
        yield n
        n -= 1

# using generators for multi tasking instead of threads!

tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task Finished')    