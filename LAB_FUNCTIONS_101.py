def print_pattern(n: int):
    '''
    This function takes an integer 'n' and prints a reverse counting pattern
    from 'n' down to 1 in decreasing rows.
    '''
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

print_pattern(5)

print(print_pattern.__doc__)