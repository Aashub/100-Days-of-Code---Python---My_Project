print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


print("You have found the Treasure Map in your Father Old stuff.\nBut this Treasure Map comes with curse.\nIf you try to find treasure you will face obstacle and you can get Die!\n")

decide_route = input("You came outside the home. Two ways to reach the treasure — S for shortcut, L for long route: ").lower()



if decide_route == "l":
    print("\nYou chooses a right route now in front of you their is a jungle.")

    choose_route = input("inside the jungle you found three routes choose between S for straight, R for Right and L for Left: ").lower()


    if choose_route == "l":
        print("\nYou came across with lion he eats, you died, Game Over!")

    elif choose_route == "r":
        print("\nYou fall into a swamp, you died, Game Over!")
        exit()

    elif choose_route == "s":
        print("\nYou decided the correct route you came across the river and across that river their is a cave.")


        boat_or_swim = input("There’s a boat nearby, but it might break. Decide how you’ll cross, Swim (S) or Boat (B): ").lower()

        if boat_or_swim == "s":
            print("\nTheir are piranha fish into the river you got eaten, Game Over!")
            exit()

        elif boat_or_swim == "b":
            print("\nYou have safely crossed the river now you have gone inside the cave.")

        print("After walking some distance you found three ways to go but map doesn't describe to go which way to find the treasure.")

        L_S_R = input("decide between left(L), Straight(S), Right(R) to find the Treasure?").lower()

        if L_S_R == "l":
            print("\nYou found the Treasure! Hurray now you are really rich person.")

        elif L_S_R == "s":
            print("\nYou fall into the abyss you died, Game Over!")
            exit()

        elif L_S_R == "r":
            print("\nYou chooses the wrong route, you attacked by the bats and they eaten you alive, Game Over!")

elif decide_route == "s":
    print("the car hits you and died, Game Over!")