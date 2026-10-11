def print_pattern(n):
    """Print a descending number triangle for a given integer n.

    The function prints rows that start from n down to 1, and each
    next row decreases by one number.
    """
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
print_pattern(int(input("Enter a number: ")))
print(print_pattern.__doc__)