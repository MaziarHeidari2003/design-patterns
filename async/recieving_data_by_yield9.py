def greet():
    friend = yield 
    print(f'Hello {friend}')


g = greet()
g.send(None)
g.send('Adam')