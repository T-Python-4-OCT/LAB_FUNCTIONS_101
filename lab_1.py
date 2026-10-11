
def number_pattern(max_num: int):
    """Print a descending number pattern.
    **Example Output for `5`**
    5 4 3 2 1   
    4 3 2 1   
    3 2 1   
    2 1   
    1   
    """
    
    for current_row in range(max_num, 0, -1):
        for current_num in range(current_row, 0, -1):
            print(current_num, end=" ")
        print()


number_pattern(max_num=int(input(" Enter a number : ")))

