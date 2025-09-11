import statistics
import os
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def analyze_data(list_numbers):
    '''
    Take in a list of numbers
    analyse and return the sum, avg, and max
    :param list_numbers: numbers to analyze
    :return: tuple of sum, avg, max
    '''
    return sum(list_numbers), statistics.mean(list_numbers), max(list_numbers)
    #autopacks into tuple


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    student_info = ('John Smith', 'Comp Eng Tech', 2025, 3.45)
    print(*student_info)
    print(student_info[0])
    print(*[x*2 for x in student_info])
    #print([a,b,c,d for a,b,c,d in student_info ]) NOPE

    #ex 2: combining tuples
    colors_rgb = (255, 0, 0) #red
    colors_cmyk = (0,100,100,0) #red

    # colors_rgb[0] = 0 TUPLE IS IMMUTABLE so NO.
    colors_rgb = (0,255,0) #this is allowed
    new_tuple = colors_rgb + colors_cmyk
    print(new_tuple)

    print(analyze_data([2,4,6,8]))

    #tuple inside of a list
    book_collection = [('The Hitchhiker\'s Guide to the Galaxy', 'Douglas Adams',
                       1979), ('Dune', 'Frank Herbert', 1965),
                       ('1984', 'George Orwell', 1949)]
    book_collection += [('Lord of the Rings', 'JRR Tolkien', 1941)]
    book_collection.remove(('Dune', 'Frank Herbert', 1965))
    print(book_collection)
    newList = []
    for x in book_collection:
        for y in x:
            newList.append(y)
    print(newList)
    '''
    #USER INPUT
    default_value = 'Nobody'
    user_input = input(f'Please enter a value [{default_value}]:') or default_value
    print(user_input)

    while True:
        default_num = "3"
        user_input = input(f'Please enter a value [{default_num}]:') or default_num
        if user_input.isnumeric():
            break

    print(user_input)

    #we want input that only contains a,b,c
    foundInvalid = True
    while foundInvalid:
        foundInvalid = False
        uinput = input("Give me a string of characters A-C:")
        for char in uinput:
            if char.upper() not in "ABC":
                foundInvalid = True
    '''
    #time for list comprehensions
    #1 square some numbers
    numbers = [1,2,3,4,5]
    squares = [x**2 for x in numbers]
    print(squares)

    #filtering!!
    numbers = [1,2,3,4,5,6,7,8,9,10]
    even_numbers = [x for x in numbers if x%2 == 0]
    print(even_numbers)

    #nested loops
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(transposed_matrix)

    #String manipulation
    word = "hello"
    uppercase_word = [char.upper() for char in word]
    print(",".join(uppercase_word))

    #conditional expression
    numbers = [1,-2,3,-4,5]
    positive_nums = [x for x in numbers if x>0]
    other_way = [x if x>0 else None for x in numbers]
    print(positive_nums)
    print(other_way)

    #flattening a list of lists
    nested_list = [[1,2,3],[4,5,6],[7,8,9]]
    flattened_list = [item for sublist in nested_list for item in sublist]
    print(flattened_list)

    #dictionaries
    keys = ('a', 'b', 'c')
    values = (1, 2, 3)
    my_dict = {keys[i]: values[i] for i in range(len(keys))}

    print(my_dict)

    #cartesian product
    list1 = [1,2,3,4,5]
    list2 = [6,7,8,9]

    cartesian_product = [(x,y) for x in list1 for y in list2]
    print(cartesian_product)

    file_names = [f for f in os.listdir('.')]
    print(file_names)

    #set of unique elements
    numbers = [1,2,2,2,2,3,3,4,5,5,5]
    print(set(numbers))
    unique_numbers = list(set([x for x in numbers])) #dept of redundancy dept
    print(unique_numbers)



