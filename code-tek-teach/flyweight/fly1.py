import string
import random



class User:
    def __init__(self, name):
        self.name = name


def random_string():
    chars = string.ascii_lowercase
    return ''.join(
        [random.choice(chars) for x in range(8)]
    )



class User2:
    strings = []
    

if __name__ == "__main__":
    users = []
    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]
    for first in first_names:
        for last in last_names:
            users.append(User(f'{first} {last}'))
