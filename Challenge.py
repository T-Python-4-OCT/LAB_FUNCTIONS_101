
secret_code = "4271"


def count_exact(secret, guess):
    """Count digits in the right position."""
    count = 0

    for i in range(4):
        if secret[i] == guess[i]:
            count += 1

    return count


def count_misplaced(secret, guess):
    """Count digits in the wrong position."""
    secret_digits = []
    guess_digits = []

    for i in range(4):
        if secret[i] != guess[i]:
            secret_digits.append(secret[i])
            guess_digits.append(guess[i])

    count = 0

    for digit in guess_digits:
        if digit in secret_digits:
            count += 1
            secret_digits.remove(digit)

    return count



def run_game(secret):
    """Play the game with six valid attempts."""
    print("Welcome to the Alien Vault!")
    print("Guess the 4-digit code in 6 attempts.")

    attempt = 0

    while attempt < 6:
        print("Attempt", attempt + 1, "of 6")
        guess = input("Enter your guess: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Please enter exactly 4 digits.")
            continue

        attempt += 1

        exact = count_exact(secret, guess)
        misplaced = count_misplaced(secret, guess)

        print("EXACT:", exact)
        print("MISPLACED:", misplaced)

        if exact == 4:
            print("Correct! You opened the vault!")
            return True

    print("Game over. The code was", secret)
    return False


run_game(secret_code)



print("Testing")

test_guesses = ["4172", "2471", "4421", "1122", "0000", "4271"]

for guess in test_guesses:
    exact = count_exact(secret_code, guess)
    misplaced = count_misplaced(secret_code, guess)

    print(guess, ": EXACT =", exact, ", MISPLACED =", misplaced)



print("Function documentation")
print(count_exact.__doc__)
print(count_misplaced.__doc__)
print(run_game.__doc__)

#MohammedAlnsafi