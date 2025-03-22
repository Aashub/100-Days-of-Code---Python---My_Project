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

#rock pare scissors variable list.
RPS_list = [rock,paper,scissors]

#here player will decide what he wants to choose
pl_choice =   int(input("What do you choose? Type 0 for Rock, 1 for Paper & 2 for Scissors\n"))

#if user choose more than 2 and less than 0 then it will print this msg.
if pl_choice > 2 or pl_choice < 0:
    print("You typed an Invalid Number, You Lose!")
    exit()
player = RPS_list[pl_choice]
computer = random.choice(RPS_list)

print("Player Chose:")
print(player)
print("Computer Chose:")
print(computer)

# here all the logics work out and print whoever is winner
if player == rock and computer == scissors:
    print("You Win")

if player == paper and computer == rock:
    print("You Win")

if player == scissors and computer == paper:
    print("You Win")

if player == rock and computer == paper:
    print("Computer Win")

if player == scissors and computer == rock:
    print("Computer Win")

if player == paper and computer == scissors:
    print("Computer Win")

elif player == computer:
    print("Draw!")

