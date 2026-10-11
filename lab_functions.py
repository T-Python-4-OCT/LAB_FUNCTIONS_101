def print_pattern(number: int):
    """Print a descending number pattern."""
    for row_number in range(number, 0, -1):
        for current_number in range(row_number, 0, -1):
            print(current_number , end=" ")
        print()

user_number = int(input("Enter a number: "))
print_pattern(user_number)