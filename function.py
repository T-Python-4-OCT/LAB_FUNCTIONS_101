

def reverse(m: int):
 """Prints a descending number"""
 for i in range(m,0,-1):
    for Re in range (i, 0 , -1):
     print (Re , end=" ")
    print()

reverse(5)
print(reverse.__doc__)

    #MohammedAlnsafi