import random


def create_code():
    """Function that creates the 4 digit code, using random digits from 1 to 8"""

    code = [0, 0, 0, 0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    return code

def show_instructions():
    """Shows instructions to the user"""

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def show_results(correct_digits_and_position,correct_digits_only):
    """Show the results from one turn"""

    print('Number of correct digits in correct place:     '
           +str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' 
           +str(correct_digits_only))

def compare(code,answer):
    """Function Compares Answer to The generated code
       ==============================================

        local variable
        --------------
        correct_digits_and_position : type -> int : Defaultvalue -> 0
        correct_digits_only : type -> int : Defaultvalue -> 0


       1. Compares each character from code and answer
       -----------------------------------------------
            - If the digit in the answer is in the code and at the same position as it is in
            code then increment the number of correct digits
            - If the digit in the answer is in the code but not same index as in the code
            then increment number of correct digits only
       2. Return
       ---------
        - The variable - correct_digits_and_position
        - The variable - correct_digits_only
       """
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    return correct_digits_and_position,correct_digits_only


def get_answer_input():
    """Asks for an input:
       ==================
        1 check if the answer is valid
        -------------------------------
            - does the input have a length of 4
            - does input only contain digits onyl
        
        2 If the answer is no on one of the validation questions above
        -------------------------------------------------------------

          - then prompt the user to input again

        3  When the input is finally correct then return it
        ---------------------------------------------------
         """


    answer = input("Input 4 digit code: ")
    while len(answer) < 4 or len(answer) > 4 or not answer.isdigit():
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    return answer


def take_turn(code):
    """Handle the logic of taking a turn, which includes:
       * get answer from user
       * check if answer is valid
       * check correctness of answer
    """

    answer = get_answer_input()
    
    correct_digits_and_position,correct_digits_only = compare(code,answer)

    
    return (correct_digits_and_position,correct_digits_only)


def show_code(code):
    """Show Code that was created to user"""

    print('The code was: '+str(code))


def check_correctness(turns,correct_digits_and_position):
    """Checks correctness of answer and show output to user"""

    
    if correct_digits_and_position == 4:
        print('Congratulations! You are a codebreaker!')
        return True
    else:
        print('Turns left: ' + str(12 - turns))
        return False


def run_game():
    """Main function for running the game"""

    
    correct = False

    code = create_code()
    show_instructions()

    turns = 0
    while not correct and turns < 12:
        correct_dig_tuple = take_turn(code)
        turns += 1
        show_results(correct_dig_tuple[0],correct_dig_tuple[1])
        correct = check_correctness(turns,correct_dig_tuple[0])

    show_code(code)


if __name__ == "__main__":
    run_game()
