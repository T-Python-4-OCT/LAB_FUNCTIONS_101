key = "4271"


def count_exact(secret, guess):
    exact = 0

    for i in range(4):
        if secret[i] == guess[i]:
            exact = exact + 1

    return exact


def count_misplaced(secret, guess):
    misplaced = 0

    for i in range(4):
        if secret[i] != guess[i]:
            if guess[i] in secret:

                count_in_secret = secret.count(guess[i])
                count_before = guess[:i].count(guess[i])

                if count_before < count_in_secret:
                    misplaced = misplaced + 1

    return misplaced


def run_game():
    attempts = 6

    while attempts > 0:
        guess = input("Enter a 4-digit code: ")

        exact = count_exact(key, guess)
        misplaced = count_misplaced(key, guess)

        print("EXACT:", exact)
        print("MISPLACED:", misplaced)

        if exact == 4:
            print("You unlocked the vault!")
            break

        attempts = attempts - 1
        print("Attempts left:", attempts)

    else:
        print("You failed to unlock the vault.")


run_game()