import random

from art import logo


def start_number_guessing():
    """this function will start the game first time."""

    def game_restart():
        """as per the user input this function will restart the game again by calling start_number_guessing() function again."""

        #this while loop runs until the user don't provide the correct input
        until_correct_input = True
        while until_correct_input:
            restart_game = input("Do you wanna play this game again? type 'y' for yes & 'n' for exit").lower()

            if restart_game == 'y':
                print("\n" * 20)
                start_number_guessing()

            elif restart_game == 'n':
                print("Good bye!")
                exit()

            else:
                print("Invalid Input, Please provide correct input!")


    def check_correct_guess(remaining_guess):
        """this function will check, the guessed number by user is correct or not."""

        #this while loop check weather the guess was correct or not and as per that decide user has won the game or not
        to_get_correct_guess = True
        while to_get_correct_guess:

            print(f"You have {remaining_guess} attempts remaining to guess the number.")

            number_guessed = int(input("Make a guess: "))

            #if guessed number is  high then this if statement will run
            if number_guessed > random_number:
                print("Too high.\nTry again.")
                remaining_guess -= 1

            # if guessed number is low then this elif statement will run
            elif number_guessed < random_number:
                print("Too low.\nTry again.")
                remaining_guess -= 1

            # if guess was correct then this one
            elif number_guessed == random_number:
                print(f"You got it!, The answer was {random_number}.\n")
                game_restart()

            # if user is exhaust all his chances to guess the number then this if statement
            if remaining_guess == 0:
                print("You've run out of guesses.")
                game_restart()

    print(logo)

    #random.randint() will give us the random number between 1 and 100
    random_number = random.randint(1,100)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
    difficulty_level = input(f"Choose a difficulty. Type 'easy', 'medium' or 'hard': ").lower()

    def select_difficulty_level(level):
        """this function will check that, on which difficulty level user wants to play this game."""

        if level == "easy":
            number_of_guess = 10
            check_correct_guess(number_of_guess)

        elif level == "medium":
            number_of_guess = 7
            check_correct_guess(number_of_guess)

        elif level == "hard":
            number_of_guess = 5
            check_correct_guess(number_of_guess)

        # if user provide invalid input as difficulty level then this elif statement will run and due to recursion it
        # will trigger the function select_difficulty_level again so it can ask the user to select difficulty level as per provided options.
        elif level != "hard" or "medium" or "easy":
            print("Invalid Input!, Please provide correct Input!")
            difficultyy_level = input(f"Choose a difficulty. Type 'easy', 'medium' or 'hard': ").lower()
            select_difficulty_level(difficultyy_level)


    select_difficulty_level(difficulty_level)

start_number_guessing()
