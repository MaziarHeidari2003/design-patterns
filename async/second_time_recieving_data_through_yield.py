from collections import deque
friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)

    # yeild from g    
# used to extract values from an iterator
# used for two way communications , reciving data and forward data

# a type of generator which recives data is a coroutine
# coroutines can take data and be suspended

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello!')
greeter.send('Hello!')
greeter.send('Hello!')
greeter.send('Hello!')

