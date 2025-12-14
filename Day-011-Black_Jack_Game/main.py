import random
from art import  logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start_blackjack():
    """this function will start the game."""

    player_card = []
    computer_card = []

    def fetch_player_card():
        """this function will distribute first two cards to player """
        for dealer_dealt in range(0, 2):
            player_card.append(random.choice(cards))

        return sum(player_card)

    def fetch_computer_card():
        """this function will distribute first two cards to computer """
        for dealer_dealt in range(0, 2):
            computer_card.append(random.choice(cards))
        card_total = sum(computer_card)

        return card_total

    def decide_winner(pl_total, com_total, pl_card, com_card):
        """this function will decide is who wins the game."""

        if pl_total == com_total:
            print("Draw 🙃")

        elif pl_total == 21 and com_total < 21:
            print("You win with a Blackjack 😎")
        elif com_total == 21 and pl_total < 21:
            print("You loss, opponent has a 😭")
        elif pl_total > 21:
            print("You went over. You lose 😧")
        elif com_total > 21:
            print("Opponent went over. You win 😁")
        elif com_total > pl_total:
            print("You lose 😤")
        elif pl_total > com_total:
            print("You win 😃")

        print(f"Your final hand: {pl_card}, final score: {player_card_total}")
        print(f"Computer's final hand: {com_card}, final score: {computer_card_total}")

        start_blackjack()

    # this input will ask the user that do he want to play a game again or not.
    game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    print("\n" * 3)

    if game_start == "y":
        print(logo)

        # here we are calling the function so that first two cards of blackjack can be drawn.
        player_card_total = fetch_player_card()
        computer_card_total = fetch_computer_card()

        should_continue = True
        while should_continue:

            print(f"Your cards: {player_card}, current score: {player_card_total}")
            print(f"Computer's first card: {computer_card[0]}")

            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            # this condition will help user to draw cards again and again
            if another_card == "y":
                player_card.append(random.choice(cards))
                player_card_total = sum(player_card)

                # this condition will implement if player cards overall total become over 21
                if player_card_total > 21:

                    decide_winner(pl_total=player_card_total, com_total=computer_card_total, pl_card=player_card,
                                  com_card=computer_card)

            # this condition will run if player doesn't want to withdraw anymore card.
            elif another_card == "n":

                if computer_card_total < 17:

                    is_true = True
                    # this while loop will help to withdraw cards of computer again & again until computer cards doesn't pass the cards total 17
                    while is_true:
                        computer_card.append(random.choice(cards))
                        computer_card_total = sum(computer_card)

                        if computer_card_total > 17:
                            is_true = False

                # if computer card is above 17 than this condition will run and decide who is the winner of a game.
                if computer_card_total > 17:
                    decide_winner(pl_total=player_card_total, com_total=computer_card_total, pl_card=player_card,
                                  com_card=computer_card)
                    should_continue = False

    elif game_start == "n":
        print("Good Bye!")
        exit()

start_blackjack()


