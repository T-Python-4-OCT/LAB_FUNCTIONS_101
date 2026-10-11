# Lab

input

def print_number(input_number:int):
    '''
    This function takes an integer input and prints a pattern of numbers in descending order.
    '''
    for number in range(input_number, 0,-1):
        for x in range(number ,0,-1):
           print(x , end=" ")
        print()
        
print_number(5)
print(print_number.__doc__)