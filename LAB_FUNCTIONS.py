def countdown (n):
    for start in range (n,0,-1):
        for num in range (start,0,-1):
            print (num, end=" ")
        print()

countdown(5)

#print documentation 
print(countdown.__doc__)