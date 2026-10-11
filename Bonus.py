# Bonus Part

CODE_NUMBER = "4271"


def count_right_number(code, guess):  #function 1
   
    count = 0
    for i in range(4):
        if code[i] == guess[i]:
            count += 1
    return count


def count_wrong_number(code, guess):  #function 2
   
    same_digits = 0
    for digit in "0123456789":
       
        same_digits += min(code.count(digit), guess.count(digit))   # i use min function because we don't want to count the same digit twice

    return same_digits - count_right_number(code, guess)


def player_vault(code, max_tries):   #function 3
    tries_used = 0

    while tries_used < max_tries:
        my_guess = input("Enter 4-digit guess: ")
        if len(my_guess) != 4 or not my_guess.isdigit():
            print("Please enter exactly 4 digits.")
            continue
        tries_used += 1
        right = count_right_number(code, my_guess)
        wrong = count_wrong_number(code, my_guess)
        print("EXACT:", right, "| MISPLACED:", wrong)



        if right == 4:
            print("Your Vault unlocked! You win in", tries_used, "tries.")
            return True
        print("Attempts left:", max_tries - tries_used)
    print("Your Vault locked forever. The code was", code)
    return False



player_vault(CODE_NUMBER, 6)