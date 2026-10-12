
def countdown(n: int):
    """Prints a countdown pattern from n to 1."""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


countdown(5)
print(countdown.__doc__)