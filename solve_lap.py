def pattern(n: int):
    'The function prints a descending pattern starting from the number you give it, decreasing row by row until it reaches the number 1.'
    for i in range(n, 0, -1):        
        for j in range(i, 0, -1):   
            print(j, end=" ")
        print() 

pattern(5)
print(pattern.__doc__)