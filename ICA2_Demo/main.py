import random
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def backwards(seq):
    for index in range(1, len(seq) + 1):
        yield seq[-index]

def print_hi(timeofday : str, weekday : str, *name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'It is {timeofday} on {weekday}! Hi, {', '.join(name)}')  # Press Ctrl+F8 to toggle the breakpoint.

def kwarg_hi(**kwargs):
    print(kwargs)
    print(kwargs['firstname'])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    names = ['Monday', 'Tuesday', 'Wednesday']
    print(*names)
    print_hi(2,'Wednesday',*names)
    kwarg_hi(firstname='Eric', lastname='Hajay', middlename='PyCharm')

    s = 'ABCDEFGHIJK'
    for letter in backwards(s):
        print(letter, end=' ')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
