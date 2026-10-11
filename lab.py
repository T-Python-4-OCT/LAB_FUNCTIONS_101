def print_pattern(n: int):
    """
    This function prints a descending number pattern
    starting from n down to 1.
    """
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

print_pattern(10)

print(print_pattern.__doc__)