
def Pattern(number: int):
    """
    
    The function prints the argument as a descending number pattern.
    Example: when the argument is 4, the output will be:

    4321
    321
    21
    1

    """
    while number > 0:
        N = number
        while N > 0:
            print(N, end="")
            N -= 1

        print()
        number -= 1


Pattern(7)

print(Pattern.__doc__)
