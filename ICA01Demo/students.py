# This is a sample Python script.
import random
import string

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

text = ""


def find_text():
    text = ""

    while text != "Hello World!":
        char = random.choices(string.ascii_letters+' '+'!')
        if str(char[0]) == str("Hello World!"[len(text)]):
            text += str(char[0])

    return text

def print_hi(name):
    print(*["".join(find_text())])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/