print('''
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
print("You have found a map in your new home basement now you have decided\n"
      "to find that Treasure.")
print("Your mission is to find the treasure.")


road = input("You have come to road decide which way you wanna"
             " Go type 'left' and 'right'\n").lower()


if road == "left":
    forest = input("You have come to a forest where you have found two ways"
          " to go 'left' and 'right'\n").lower()

    if forest == "left":
        print("You have fall into a swamp, Game Over!")

    elif forest == "right":
        lake = input("You have reached out to a lake decide which way "
                     "you wanna go, cross the lake, 'Swim' or 'boat'\n").lower()

        if lake == "swim":
            print("crocodile was present in a lake, they have eaten you, Game Over!")

        elif lake == "boat":
            hill = input("you have safely crossed the lake and reached out to a hill"
                         " Do you wanna climb the hill or go from a cave select from "
                         "'climb' or 'cave'\n").lower()

            if hill == "cave":
                print("you have safely gone inside the cave")
                direction = input("inside the cave you have found three ways to go "
                                  "'left', 'Right' and 'Center'\n")

                if direction == "left":
                    print("Hurray You Found the Treasure, Game Over")

                elif direction == "center":
                    print("You Fall down in a ditch Game Over")

                elif direction == "right":
                    print("Yeti attacked You, Game Over")

            elif hill == "climb":

                print("Due to heavy rain landslide happened and you died, Game Over")

elif road == "right":
    print("You have struck by Truck, you die, Game Over!")
