import random

from art import  logo,vs
from game_data import data

# original variable help us track over current score & game_end_score variable help program to end it
original_score = 0
game_end_score = -1
compare_A = random.choice(data)
compare_B = random.choice(data)

if compare_A == compare_B:
    compare_B = random.choice

def increase_score(follow_a, follow_b):
    """this function will increase the score whenever do the correct guess and if guess is wrong it will return the value which will help for existing the game."""

    global original_score
    most_followers = input(f"Who has more followers? Type 'A' or 'B':").lower()

    if follow_a > follow_b:
        if most_followers == "a":
            original_score += 1

        elif most_followers == "b":
            return game_end_score

    elif follow_b > follow_a:
        if most_followers == "b":
            original_score += 1

        elif most_followers == "a":
            return game_end_score

    return  original_score

def assigning_data_a(comp_a):
    """this function will assign compare A data"""

    name = comp_a["name"]
    description = comp_a["description"]
    country = comp_a["country"]
    follower_count_a = comp_a["follower_count"]

    return f"{name}, {description}, from {country}.",  follower_count_a

def assigning_data_b(comp_b):
    """this function will assign compare B data"""

    name = comp_b["name"]
    description = comp_b["description"]
    country = comp_b["country"]
    follower_count_a = comp_b["follower_count"]

    return f"{name}, {description}, from {country}.", follower_count_a

def declare_current_score(A, B):
    """this function will give output of current score and return compare B"""

    print("\n" * 20)
    print(f"{logo}\nYou're right! Current score: {original_score}.\nCompare A: {A}{vs}Against B: {B}")

    return B

restart_game = True
while restart_game:

    compare_A_details, followers_A=  assigning_data_a(comp_a = compare_A)
    compare_B_details, followers_B =  assigning_data_b(comp_b = compare_B)

    print(f"{logo}\nCompare A: {compare_A_details}{vs}Against B: {compare_B_details}")

    until_not_wrong = True
    while until_not_wrong:
        compare_B = random.choice(data)

        score = increase_score(follow_a=followers_A, follow_b=followers_B)

        # this below statement will help us to assign compare_b data to compare_a and compare_b data get assigned with new data
        compare_A_details = compare_B_details
        followers_A = followers_B
        compare_B_details, followers_B = assigning_data_b(comp_b=compare_B)

        declare_current_score(A = compare_A_details, B = compare_B_details)

        # this if statement will run when user make wrong guess 'score' value became -1 which will lead this if statement to implement
        if original_score != score:
            print("\n" * 15)
            print(f"{logo}\nSorry, that's wrong. Final score: {original_score}")
            until_not_wrong = False

            decide = input("Do you want to play higher lower game again Type 'Y' for yes and 'N' for no :").lower()

            if decide == "y":
                original_score = 0
                print("\n" * 25)
                continue

            elif decide == "n":
                print("Good Bye!")
                restart_game = False
















