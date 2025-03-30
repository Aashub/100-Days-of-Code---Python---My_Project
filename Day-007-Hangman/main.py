import random
from hangman_art import logo, stages
from hangman_words import  word_list


print(logo)
life = 6

# here we can get the random word from word_list
word = random.choice(word_list)


char_list = []
dash_list = []

# here we will add the "_" & word character in a list
for char in word:
    char_list.append(char)
    dash_list.append("_")

# here we will convert the list into again strings
for string in range(0,len(word)):
    word_str = "".join(map(str,char_list))
    dash_str = "".join(map(str, dash_list))

print(word_str)
print(f"Word to guess: {dash_str}")

should_continue = True

#here the loop will run until its condition didn't become False
while should_continue:

    print(f"****************************{life}/6 LIVES LEFT****************************")
    Guess = input("Guess the Word: ").lower()

    # if Guess character is present in word_str then condition become True
    if Guess in word_str:

        # in every correct guess the guessed value is replaced with _ character
        # and again converted into string
        for correct_guess in range(0,len(word_str)):
            if word_str[correct_guess] == Guess:
                dash_list[correct_guess] = Guess
                dash_str = "".join(map(str, dash_list))


        print(f"Word to guess: {dash_str}")
        print(stages[life])

        if dash_str == word:
            print("****************************YOU WIN****************************")
            should_continue = False

    # if Guess character is not present in word_str then condition will run
    elif Guess not in word_str:
        life -= 1
        print(f"Word to guess: {dash_str}")
        print(f"You guessed {Guess}, that's not in the word. You lose a life.")
        print(stages[life])

        if life == 0:
            print(f"***********************IT WAS {word}! YOU LOSE**********************")
            should_continue = False





