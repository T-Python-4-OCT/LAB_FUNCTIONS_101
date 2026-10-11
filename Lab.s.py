def number_pattern(n):
    '''a function to print the number pattern'''
    for i in range(n, 0, -1):
        for number in range(i, 0, -1):
            print(number, end = " ")  
        print() 


num = int(input("Enter a number: "))
number_pattern(num)
help(number_pattern)
