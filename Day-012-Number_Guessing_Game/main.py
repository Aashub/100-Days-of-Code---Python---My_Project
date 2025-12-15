import random
from art import  logo

# here are my global constant variable which i don't need to modify later in my program
game_level = {
    "EASY": 10,
    "MODERATE": 7,
    "HARD": 5,
}


def start_number_guessing_game():
    """this function will start the number guessing game"""

    correct_guess_num = 0
    def guessing_the_number(number_to_guess, attempts_left):
        """this function will decide that user has guessed the correct number or not"""

        number_guessed_correctly = True

        # this while loop will run until user don't guess the correct number or until he lost all his chances
        while number_guessed_correctly:

            print(f"You have {attempts_left} attempts remaining to guess the number.")
            guessed_number = int(input("Make a guess: "))

            if attempts_left == 1:
                return 0

            elif guessed_number > number_to_guess:
                print("Too high.\nGuess again.")
                attempts_left -= 1

            elif guessed_number < number_to_guess:
                print("Too low.\nGuess again.")
                attempts_left -= 1

            elif guessed_number == number_to_guess:
                return guessed_number
        return None

    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")
    random_number = int(random.randint(1, 101))

    for_correct_input = True

    # this while loop prevent the user to enter wrong output by asking him again & again to enter correct input.
    while for_correct_input:
        decide_game_level = input("Choose a difficulty. Type 'easy', 'moderate' or 'hard':").upper()

        # below if and for loop will help us to decide on which level user wants to play a game and as per that it will calling the function.
        if decide_game_level == "EASY" or decide_game_level == "MODERATE" or decide_game_level ==  "HARD":

            for level in game_level:
                if level == decide_game_level:
                    number_of_attempts = game_level[level]
                    correct_guess_num = guessing_the_number(number_to_guess = random_number, attempts_left = number_of_attempts)
                    for_correct_input = False

        else:
            print("Please provide the correct input!")

    if correct_guess_num:
        print(f"You got it! The answer was {correct_guess_num}.\n")

    elif correct_guess_num == 0:
        print("You've run out of guesses. restart to play again.\n")

start_number_guessing_game()

should_continue = True

# this while loop ask the user that he wants to play a game again or not and also prevents him to enter wrong input.
while should_continue:
    restart_game = input("Do you want to play number_guessing_game again? type 'Y' for yes & 'N' for no: ").lower()

    if restart_game == "y":
        print("\n" * 20)
        start_number_guessing_game()
    elif restart_game == "n":
        print("Good Bye!")
        should_continue = False
    else:
        print("Please provide the correct input!")

