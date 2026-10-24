def print_pattern(n):
    """ Prints a pattern of numbers in descending order."""
    for row in range(n, 0, -1):
        for number in range(row, 0, -1):
            print(number, end=" ")
        print()


print_pattern(5)
print(print_pattern.__doc__)