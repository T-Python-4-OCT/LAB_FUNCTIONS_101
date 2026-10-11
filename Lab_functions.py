def countdown_pattren(number: int ):

    """
     Prints a countdown pattern starting from the given number.
    """

    for i in range(number,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()


countdown_pattren(9)

print(countdown_pattren.__doc__)