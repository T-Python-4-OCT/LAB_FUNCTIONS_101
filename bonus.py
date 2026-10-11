# bonus

def count_secret(hidden, input_guess):
    '''
    This function takes a hidden number and an input guess, and counts how many digits are correct in the guess.
    '''
    count = 0
    for i in range(len(hidden)):
        if hidden[i] == input_guess[i]:
            count += 1
    return count


def count_wrong_place(hidden, input_guess):
    '''
    This function takes a hidden number and an input guess, and counts how many digits are correct but in the wrong place.
    '''

    hidden_remaining = []
    input_guess_remaining = []

    for i in range(len(hidden)):
        if hidden[i] != input_guess[i]:
           hidden_remaining.append(hidden[i])
           input_guess_remaining.append(input_guess[i])

    wrong_place = 0
    for digit in input_guess_remaining:
     if digit in hidden_remaining:
        wrong_place += 1
        hidden_remaining.remove(digit)
        return wrong_place



def git_hints(hidden, input_guess):
    '''
    This function takes a hidden number and an input guess.
    '''
    correct_count = count_secret(hidden, input_guess)
    wrong_place_count = count_wrong_place(hidden, input_guess)
    return correct_count, wrong_place_count


def run_functions():

    hidden = "4271"
    max_attempts = 6

    print("Welcome to the guessing game!!")
    print("You have to guess a 4 digit number. You have 6 attempts.")
    print(f"You have {max_attempts} attempts to guess the number.")

    for attempt in range(max_attempts):
        input_guess = input(f"\nAttempt {attempt}/{max_attempts} - Enter your guess: ")

        if len(input_guess) != 4 or not input_guess.isdigit():
            print("Please enter a 4 digit number.")
            continue

        correct_count, wrong_place_count = git_hints(hidden, input_guess)

        print(f"Correct digits in the right place: {correct_count}")
        print(f"Correct digits in the wrong place: {wrong_place_count}")
    

        if correct_count == 4:
            print("Congratulations! You've guessed the number correctly!")
            break

    print(f"The secret number was: {hidden}")


run_functions()

