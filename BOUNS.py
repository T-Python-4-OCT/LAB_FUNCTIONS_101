


secret_code = "4271"

def count_clues(secret_code, PlaNum):
    EXACT = 0
    misplaced = 0

    for ind in range(len(PlaNum)):
        if secret_code[ind] == PlaNum[ind]:
            EXACT += 1

    remaining_numbers = list(secret_code)
    remaining_guess = list(PlaNum)

    for ind in range(len(PlaNum)):
        if secret_code[ind] == PlaNum[ind]:
            remaining_numbers[ind] = None
            remaining_guess[ind] = None

    for ind in range(len(PlaNum)):
        if remaining_guess[ind] is not None:
            if remaining_guess[ind] in remaining_numbers:
                misplaced += 1
                remaining_numbers.remove(remaining_guess[ind])

    return EXACT, misplaced




def check_guess(secret_code, PlaNum):
    if PlaNum == secret_code:
        return True
    else:
        return False



def run_game():
    attempts = 6

    for i in range(attempts):
        PlaNum = input("Enter the secret_code: ")

        if len(PlaNum) != 4 or not PlaNum.isdigit():
            print("Enter exactly 4 digits!")
            continue

        EXACT, misplaced = count_clues(secret_code, PlaNum)
        
        print("Player guess\tEXACT\tMISPLACED")
        print(f"{PlaNum}\t\t{EXACT}\t{misplaced}")



        if check_guess(secret_code, PlaNum):
            print("Victory! the secret_code: is true!")
            return
        else:
            print("the secret_code is false. Try again!")

    print("I failed, all attempts are over")

run_game()