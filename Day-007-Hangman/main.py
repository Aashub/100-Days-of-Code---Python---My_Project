#here we are importing all the necessary files which is required to complete this project
import random
from hangman_words import  word_list
from hangman_art import  stages
from hangman_art import logo


print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
placeholder_list = []
chosen_word_list = []

#here we are replacing each letter with space"_"
for space in chosen_word:
    placeholder += "_"

#here we are adding all the space"_" as per the letter in the place holder list
for space in placeholder:
    placeholder_list.append(space)

#here we are adding all the letter as per the chosen word in the chosen word list
for space in chosen_word:
    chosen_word_list.append(space)


print(f"Word to guess: {placeholder}")

Lives = 6
should_continue = True

# loop will continuously run until player's life don't become 0, and he loses a game or until not when he is not guessed all the correct letters
while should_continue:
    display = ""

    #this statement will show the current lives left of player
    print(f"**************************** {Lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # this for loop will check that if guess is in chosen_word_list than it will update the place_holder_list with that letter
    for letter in range(0, len(placeholder_list)):

        # here whenever player guess a letter which is already guessed than this if statement will run
        if guess == placeholder_list[letter]:
            print(f"You've already guessed {guess}")
            pass

        # if guess is present in chosen_word_list than it will update the place_holder_list with that letter
        if guess in chosen_word_list[letter]:
            placeholder_list[letter] = guess

    # here we are concatenating all the correct guesses of placeholder_list in display string
    for correct_guess in placeholder_list:
        display += correct_guess


    print(f"Word to guess: {display}")

    # if guess is not correct, this if statement will execute and decrease 1 lives from overall Lives
    if guess not in chosen_word:
        Lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[Lives])

    # this statement will print each stages of players.
    elif guess in chosen_word:
        print(stages[Lives])

    # if chosen word and all the correct guess string "display" string matches than this if statement will run
    if chosen_word == display:
        print("****************************YOU WIN****************************")
        should_continue = False

    # if player loses all the lives than this if statement will run
    if Lives == 0:
        print(f"*********************** IT WAS {chosen_word}! YOU LOSE **********************")
        should_continue = False




