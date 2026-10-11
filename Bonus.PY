def count_exact(secret, guess):
    """Count digits that are correct and in the correct position."""
    exact = 0
    for i in range(4):
        if secret[i] == guess[i]:
            exact = exact + 1
    return exact


def count_misplaced(secret, guess):
    """Count digits that are correct but in the wrong position."""
    secret_left = []
    guess_left = []
    for i in range(4):
        if secret[i] != guess[i]:
            secret_left.append(secret[i])
            guess_left.append(guess[i])

    misplaced = 0
    for digit in guess_left:
        if digit in secret_left:
            misplaced = misplaced + 1
            secret_left.remove(digit)
    return misplaced


def play_game():
    """Run the alien vault game, the player has 6 attempts."""
    secret = "4271"
    attempts = 6

    print("Welcome to the Alien Vault!")
    print("You have 6 attempts to crack the code.")

    for attempt in range(attempts):
        guess = input("Enter your 4-digit guess: ")

        if len(guess) != 4:
            print("Please enter exactly 4 digits!")
            continue

        exact = count_exact(secret, guess)
        misplaced = count_misplaced(secret, guess)
        print("EXACT:", exact, "MISPLACED:", misplaced)

        if exact == 4:
            print("You cracked the vault! You win!")
            return

    print("No more attempts! The vault stays locked. The code was", secret)


play_game()
