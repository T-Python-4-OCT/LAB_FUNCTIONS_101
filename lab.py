def print_descending_sequence(number):
    """Print descending rows of numbers from number to 1."""
    for i in range(number, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


print_descending_sequence(5)

print(print_descending_sequence.__doc__)