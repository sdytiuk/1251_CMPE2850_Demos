import math
import random

rad_to_deg = lambda r: 360*r/(2*math.pi)

max = 10000

rand_int = lambda: random.randint(0,max)

def ri():
    max = 500 + 1
    return random.randint(0,max)

print('Call #1: lambda rand_int() call returned: ', rand_int())
print('Call #2: lambda rand_int() call returned: ', ri())

ans = rad_to_deg(max)
print(ans)

list_of_tuples = [(1,2.0,'Zelda'),(4,6.0,'Melda'),(3,1.0,'Alda'),
                  (1,2.0,'Welda'),(1,2.0,'Pupil')]
list_of_tuples.sort(key = lambda item: (item[1],item[2]),reverse = True)

print(list_of_tuples)

#deque
from collections import deque
q = deque(range(5))
print(q)
for i in range(20,25):
    q.append(i)
print(q)

while (len(q) > 0):
    print(q.pop())

def make_sequence(num):
    """
    Showing off doctest
    :param num:
    :return:
    """
    return list(range(num))

print(make_sequence(5))

import sys
print(sys.argv)
print(len(sys.argv))
if len(sys.argv) > 2:
    print(sys.argv[1], 'says hi to ', sys.argv[2])