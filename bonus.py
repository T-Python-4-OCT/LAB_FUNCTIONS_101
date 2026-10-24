def count_exact(secret, guess):
    exact = 0
    for i in range(4):
        if secret[i] == guess[i]:
            exact += 1
    return exact


def count_misplaced(secret, guess):
    matches = 0
    for digit in "0123456789":
        matches += min(secret.count(digit), guess.count(digit))
    return matches - count_exact(secret, guess)


def run_game():
    secret = "4271"
    attempts = 0

    while attempts < 6:
        guess = input("Enter a 4-digit code: ")

        if len(guess) != 4 or not guess.isdecimal():
            print("Please enter exactly 4 digits.")
            continue

        attempts += 1
        exact = count_exact(secret, guess)
        misplaced = count_misplaced(secret, guess)

        print(f"EXACT: {exact}, MISPLACED: {misplaced}")

        if exact == 4:
            print("You unlocked the vault!")
            return

        print(f"Attempts left: {6 - attempts}")

    print(f"You failed! The code was {secret}.")


run_game()