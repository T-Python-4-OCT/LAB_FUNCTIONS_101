
def print_number(n):
    """
    This function gets a number n and prints numbers going down.
   
    """

    for i in range(n, 0, -1):
        
        for j in range(i, 0, -1):
            print(j, end=" ")
            
        print()



print(print_number.__doc__)

print("\n--- Output only when I put any number ---")

print_number(7)