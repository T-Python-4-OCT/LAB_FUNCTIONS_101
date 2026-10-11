 
def print_number(num):
    '''Printing the numbers in descending order , removing the lst number each line . 
    
    '''
    
    for x in range(num, 0,-1):
        for y in range(x, 0, -1):
            print(y, end=' ')
        print()
        


print_number(5)
print(print_number.__doc__)


# The output is :
# this function show me the number like this : 
# 5 4 3 2 1   
# 4 3 2 1   
# 3 2 1   
# 2 1   
# 1   
        