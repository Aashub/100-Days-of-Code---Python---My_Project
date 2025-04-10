import art
from random import  choice
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def black_jack():
    """this function will start the Game """

    #this is the Dictionary which will store the player & dealer card value and their overall score
    Cards = {
        "player_card": [],
        "computer_card": [],

        "player_score": 0,
        "computer_score": 0
    }

    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

    if user_input == "y":
        print("\n" * 17)
        print(art.logo)


        def final_result():
            """this function will print out the final result of the game"""

            print(f"Your final hand: {Cards["player_card"]} , final score: {Cards["player_score"]}")
            print(f"Computer's final hand: {Cards["computer_card"]}, final score: {Cards["computer_score"]}")


        def player_cards(num):
            """this function will give the random cards to player and also give its card total score
                   and store player card value and total score in dictionary"""

            for pl_cards in range(0, num):
                if num == 2:
                    Cards["player_card"].append(choice(cards))
                    Cards["player_score"] += Cards["player_card"][pl_cards]

                #when player want to get another card this if statement will run and will give
                # him a random another card
                if num == 1:
                    Cards["player_card"].append(choice(cards))
                    Cards["player_score"] += Cards["player_card"][len(Cards["player_card"])-1]

                    if Cards["player_score"] > 21:
                        final_result()
                        print("You went over. You lose 😭")
                        black_jack()


        def computer_cards(num):
            """this function will give the random cards to dealer and also give its card total score
                            and store dealer card value and total score in dictionary"""

            for com_cards in range(0, num):
                if num == 2:
                    Cards["computer_card"].append(choice(cards))
                    Cards["computer_score"] += Cards["computer_card"][com_cards]

                #if dealer score is less than 17 than this if statement will run and it will add another
                #card and it will add cards until dealer score don't go beyond 17
                elif num == 1:
                    Cards["computer_card"].append(choice(cards))
                    Cards["computer_score"] += Cards["computer_card"][len(Cards["computer_card"])-1]

                    if Cards["computer_score"] < 17:
                        num = 1
                        computer_cards(num)

                    elif Cards["computer_score"] >= 17:

                        if Cards["computer_score"] <= 21:
                            return

                        elif Cards["computer_score"] > 21:
                            final_result()
                            print("Opponent went over. You win 😁")
                            black_jack()

            return Cards["computer_card"][0]


        pl_num = 2
        com_num = 2

        #here the first time player and dealer card value is being assigned
        player_cards(pl_num)
        computer_first_card = computer_cards(com_num)

        should_continue = True

        # this loop will help to run the game until the player decide now he don't want anymore cards
        while should_continue:
            print(f"Your cards: {Cards["player_card"]}, current score: {Cards["player_score"]}")
            print(f"Computer's first card: {Cards["computer_card"][0]}")

            new_card = input("Type 'y' to get another card, type 'n' to pass:").lower()

            if new_card == "y":
                pl_num = 1
                player_cards(pl_num)
                print(f"Computer's first card: {computer_first_card}")

            elif new_card == "n":

                if Cards["computer_score"] < 17:
                    num = 1
                    computer_cards(num)

                if Cards["computer_score"] == Cards["player_score"]:
                    final_result()
                    print("Draw 🙃")

                elif Cards["computer_score"] < Cards["player_score"]:

                    final_result()
                    print("You win 😃")

                elif Cards["computer_score"] > Cards["player_score"]:
                    final_result()
                    print("You lose 😤")

                black_jack()

    else:
        print("Good bye")
        exit()
black_jack()













