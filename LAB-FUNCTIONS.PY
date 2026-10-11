def my_function(num):
    """This function prints numbers from num down to 1,
      and each line starts with one number less."""

    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


my_function(10)
print(my_function.__doc__)
