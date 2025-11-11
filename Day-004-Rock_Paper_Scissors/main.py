import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))

print(user_choice)

signs = [rock, paper, scissors]

computer_choice = random.choice(signs)

# if both player choose the same thing then this condition make it draw
if signs[user_choice] == computer_choice:
    print(f"You Chose:\n{signs[user_choice]}\nComputer chose:\n{computer_choice}\nIt's a draw")

# if player choose rock and computer chose paper this condition make me lose.
elif signs[user_choice] == rock and computer_choice == paper:
    print(f"You Chose:\n{signs[user_choice]}\nComputer chose:\n{computer_choice}\nYou Lose!")

# if player choose rock and computer chose scissors this condition make me win.
elif signs[user_choice] == rock and computer_choice == scissors:
    print(f"You Chose:\n{signs[user_choice]}\nComputer chose:\n{computer_choice}\nYou Win!")

# if player choose paper and computer chose rock this condition make me win.
elif signs[user_choice] == paper and computer_choice == rock:
    print(f"You Chose:\n{signs[user_choice]}\nComputer chose:\n{computer_choice}\nYou Win!")

# if player choose paper and computer chose scissors this condition make me lose.
elif signs[user_choice] == paper and computer_choice == scissors:
    print(f"You Chose:\n{signs[user_choice]}\nComputer chose:\n{computer_choice}\nYou Lose!")

# if player choose scissors and computer chose rock this condition make me lose.
elif signs[user_choice] == scissors and computer_choice == rock:
    print(f"You Chose:\n{signs[user_choice]}\nComputer chose:\n{computer_choice}\nYou Lose!")

# if player choose scissors and computer chose paper this condition make me Win.
elif signs[user_choice] == scissors and computer_choice == paper:
    print(f"You Chose:\n{signs[user_choice]}\nComputer chose:\n{computer_choice}\nYou Win!")
















