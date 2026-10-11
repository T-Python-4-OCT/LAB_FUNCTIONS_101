
def numberRefer(number):
    ''' A function to print numbers in reverse and repeat them.'''
    for num in range(number,0,-1):
        for i in range(num,0,-1):
            print(i,end=" ")
        print()

        
      
        
Number1=int(input("Enter a number "))  
numberRefer(Number1)
print(numberRefer.__doc__)

    
