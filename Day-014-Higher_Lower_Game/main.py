from art import logo, vs
from game_data import data
from random import randint

def start_higher_lower():
    """This function will start the higher lower game"""

    score = 0

    def restart_game():
        """this function will restart the game from beginning."""
        correct_input = True
        while correct_input:
            restart = input("Do you wanna play this game again 'Y' for yes 'N' for No.").lower()

            if restart == 'y':
                start_higher_lower()

            elif restart == 'n':
                print("Good Bye!")
                exit()

            else:
                print("Invalid Input please enter correct input!")

    score = 0
    def compare_a():
        """this function will give us the first compare value details """

        print(logo)
        list_index_a = randint(0, 49)
        print(f"Compare A: {data[list_index_a]["name"]}, {data[list_index_a]["description"]}, from {data[list_index_a]["country"]}")
        followers_of_a = data[list_index_a]["follower_count"]
        print(followers_of_a)
        return followers_of_a

    def compare_b():
        """this function will give us the first compare value details """

        print(vs)
        list_index_b = randint(0, 49)
        print(f"Compare B: {data[list_index_b]["name"]}, {data[list_index_b]["description"]}, from {data[list_index_b]["country"]}")
        followers_of_b = data[list_index_b]["follower_count"]
        print(followers_of_b)
        return followers_of_b, list_index_b

    def shuffle_compare(followers_a, index_number):
        """this function will provide us the functionality of to shift the value from compare A to compare B."""

        print(logo)
        print(f"Compare A: {data[index_number]["name"]}, {data[index_number]["description"]}, from {data[index_number]["country"]}")
        print(followers_a)

        # here we are calling the compare_b function again so we can get the again some random details of another celebrity to compare
        followers_b, indexing_for_b = compare_b()

        # this if statement will solve the problem of both comparision details come out same then it will agian call compare b function
        if followers_a == followers_b:
            followers_b, indexing_for_b = compare_b()

        return followers_a, followers_b, indexing_for_b


# here we will call our compare A and compare B function for the first time so they can give us celebrity details to compare.
    a_followers = compare_a()
    b_followers, index_number_b= compare_b()

    for_correct_guess = True
    while for_correct_guess:

        # this if else statement will check that provided input by user of followers is higher or not
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if guess == "a":

            # if user guess is correct then we will increase his score by one and call the shuffle compare function so now
            # compare B became compare A
            if a_followers > b_followers:
                score += 1
                a_followers, b_followers, random_num = shuffle_compare(b_followers, index_number_b)
                index_number_b = random_num
                print(f"You are right the correct score is {score}")

            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                restart_game()

            # if user guess is correct then we will increase his score by one and call the shuffle compare function so now
            # compare B became compare A
        elif guess == "b":
            if a_followers < b_followers:
                score += 1
                a_followers, b_followers, random_num = shuffle_compare(b_followers, index_number_b)
                index_number_b = random_num

                print(f"You are right the correct score is {score}")

            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                restart_game()

        else:
            print("Invalid Input please enter correct input!")


start_higher_lower()
