# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

varGlobal = 'GLOBAL'

def fncA():
    print('fncA', varGlobal)

def fncB():
    #global varGlobal IF you want to access the global!!
    #print('fncB (Try 1)', varGlobal) TRIPPY!
    varGlobal = 'LOCAL'
    print('fncB', varGlobal)
    #fncB_Nested() DNW
    def fncB_Nested():
        varGlobal = 'Nested'
        print('fncB_Nested', varGlobal)
    fncB_Nested()

def fncC():
    print('fncC', varGlobal)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fncA()
    fncB()
    fncC()
    print_hi('PyCharm')
    decimal_number = 12345.678
    octal_number = 0o12
    hexadecimal_number = 0xae0
    binary_number = 0b10110001

    print(decimal_number, octal_number, hexadecimal_number, binary_number, type(binary_number))

    x, y, z = 1, 2, 3

    z, y = y, z

    '''
    As a note, with explicit tuple syntax, this works in c# as well.
    
    int x = 3;
    int y = 4;
    ( y, x ) = ( x, y ); // not too bad, more brackets.
    '''
    t = 1,2,3
    print(t, type(t))
    print(x, y, z, type(x))

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
