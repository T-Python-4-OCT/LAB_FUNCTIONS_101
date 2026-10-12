
def count_exact(secret, guess):
    exact = 0

    for i in range(4):
        if secret[i] == guess[i]:
            exact += 1

    return exact


def count_misplaced(secret, guess):
    remaining_secret = []
    remaining_guess = []

    for i in range(4):
        if secret[i] != guess[i]:
            remaining_secret.append(secret[i])
            remaining_guess.append(guess[i])

    misplaced = 0

    for digit in remaining_guess:
        if digit in remaining_secret:
            misplaced += 1
            remaining_secret.remove(digit)

    return misplaced


def play_game():
    secret_code = "4271"
    attempts = 6

    print("Welcome to the Alien Vault!")
    print("You have 6 attempts to crack the code.")

    for attempt in range(1, attempts + 1):
        guess = input(
            f"Attempt {attempt}/{attempts} - Enter your guess: "
        )

        if len(guess) != 4 or not guess.isdigit():
            print("Enter exactly 4 digits!")
            continue

        exact = count_exact(secret_code, guess)
        misplaced = count_misplaced(secret_code, guess)

        print("EXACT:", exact)
        print("MISPLACED:", misplaced)

        if exact == 4:
            print("Congratulations! You cracked the vault!")
            return

    print("Game over! You ran out of attempts.")
    print("The secret code was:", secret_code)


play_game()