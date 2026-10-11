SECRET_CODE = "4271"

def count_exact(secret: str, guess: str) -> int:
    """Count digits that are correct AND in the correct position."""
    exact = 0
    for s, g in zip(secret, guess):
        if s == g:
            exact += 1
    return exact


def count_misplaced(secret: str, guess: str) -> int:
    """Count digits that are correct but in the wrong position."""
    temp = list(secret)

    
    for i in range(4):
        if guess[i] == secret[i]:
            temp[i] = None

    misplaced = 0

    for i in range(4):
        if guess[i] != secret[i]:  # 
            if guess[i] in temp:
                misplaced += 1
                temp[temp.index(guess[i])] = None  

    return misplaced


def play_game():
    print("Alien Vault Cracker — Python Edition")
    print("Try to crack the 4-digit alien code!")
    print("You have 6 attempts.\n")

    attempts = 6

    while attempts > 0:
        guess = input("Enter your 4-digit guess: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter exactly 4 digits.\n")
            continue

        exact = count_exact(SECRET_CODE, guess)
        misplaced = count_misplaced(SECRET_CODE, guess)

        print(f"EXACT: {exact}")
        print(f"MISPLACED: {misplaced}\n")

        if exact == 4:
            print(" You cracked the alien vault! Technology unlocked!")
            return

        attempts -= 1
        print(f"Attempts left: {attempts}\n")

    print(" You failed to crack the vault. The alien tech remains locked.")



play_game()
