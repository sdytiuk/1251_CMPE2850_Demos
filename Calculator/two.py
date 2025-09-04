from main import *
from calculator import *
import random

if __name__ == '__main__':
    for x in range(-50, 0, 2):
        print('*', x, end='')
    print()
    print('x'*10)

    x,y = 200,1300
    match(x,y):
        case(100, 300):
            print(1)
        case (100 | 300 | 500, 200):
            print(2)
        case (_, 333):
            print(3)
        case _:
            print('Match all')

    #RANDOM
    val = random.randint(1,10) #B IS INCLUSIVE
    a = [3, 6, 33, 88]
    b = random.choice(a) #picks one from a
    random.shuffle(a)
    print(a)
