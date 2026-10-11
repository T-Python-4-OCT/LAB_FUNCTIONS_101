SECERET_CODE = "4271"


def count_exact (secrt,guess):
    exact = 0

    for i in range(4):
        if secrt[i] == guess[i]:
            exact += 1

    return exact


def count_misplaced(secrt,guess):
    secrt_left =[]
    guess_left =[]

    for i in range(4):
        if secrt[i] != guess[i]:
            secrt_left.append(secrt[i])
            guess_left.append(guess[i])
    
    
    misplaced = 0    

    for digit in guess_left:
        if digit in secrt_left:
            misplaced += 1
            secrt_left.remove(digit)   


    return misplaced


def run_game():
    attempts = 12

    while attempts > 0:
        guess = input("Enter your 4-digit guess:")

        if len(guess) != 4 or not guess.isalnum():
            print("Invalid input. Please enter a 4-digit number.")

            continue

        exact = count_exact(SECERET_CODE, guess)
        misplaced = count_misplaced(SECERET_CODE, guess)

        print(f"Exact matches: {exact}, Misplaced matches: {misplaced}")

        if exact == 4:
            print("You cracked the code! Congratulations!")
            return

        attempts -= 1
        print(f"Attempts remaining: {attempts}")

    print("You failed to crack the code.")
    print(f"Wrong guesses: {6 - attempts}")

if __name__ == "__main__":
    run_game()

