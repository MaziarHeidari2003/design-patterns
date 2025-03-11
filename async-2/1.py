"Generators that work together are often called coroutines"

import time
from collections import deque
class AsyncScheduler:
    def __init__(self):
        self.ready = deque()

    def call_soon(self, coro):
        self.ready.append(coro)

    def run_until_complete(self):
        while self.ready:
            self.current = self.ready.popleft()        
            try:
                self.current.send(None)
                if self.current:
                    self.call_soon(self.current)
            except StopIteration:
                pass



def sleep(dur):
    until = time.time() + dur
    while time.time() < until:
        yield



def do_tasks(tasks, dur=3):
    for task in tasks:
        print(f'Running {task=}')

        yield from sleep(dur)


asyncio = AsyncScheduler()
asyncio.call_soon(do_tasks(['task1', 'task2', 'task3']))
asyncio.call_soon(do_tasks(['task4', 'task5', 'task6'], dur=1))


asyncio.run_until_complete()