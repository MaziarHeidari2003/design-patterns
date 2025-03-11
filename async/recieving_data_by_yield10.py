from collections import deque
from types import coroutine


friends = deque(('ralphe', 'jose', 'charlie', 'jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('starting...')
    await g
    print('end...')
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)


greeter = greet(friend_upper())            
greeter.send(None)
greeter.send('Hi')