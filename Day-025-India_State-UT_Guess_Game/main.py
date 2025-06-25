import turtle
import pandas
from pandas.core.missing import mask_missing

screen = turtle.Screen()

cord = turtle.Turtle()
msg = turtle.Turtle()
cord.hideturtle()

# here we are giving the name to a title
screen.title("India State Game")


image = "./india_map.gif"
screen.addshape(image)
turtle.shape(image)


def player_click(x_cor, y_cor, state_name):
    """this function will take 3 argument to relocate the state name to its desired location"""
    cord.penup()
    cord.goto(int(x_cor), int(y_cor))

    cord.write(f"{state_name}", align="center", font=("Georgia", 8, "normal"))

# here we are reading the csv file so we can use its data.
data = pandas.read_csv("./indian_states_coordinates_turtle.csv")

correct_guees = []

should_continue = True

# while loop will run until the player don't guess all the state names
while should_continue:

    # here we are allowing user to guess the correct state
    answer_state = screen.textinput(title=f"{len(correct_guees)}/{len(data)} States/UT Correct", prompt="what's another state name?").title()

    if answer_state == "Exit":
        should_continue = False

    for matching in data["State"]:
        #this for loop checks if any matched state from the csv data is matching with player guess then it will pass its
        #coordinate to the player check function so state name shows in its correct location

        if matching == answer_state:

            correct_guees.append(answer_state)

            state_coordinate = data[data["State"] == answer_state]
            x_coordinate = state_coordinate["X"]
            y_coordinate = state_coordinate["Y"]

            player_click(x_coordinate,y_coordinate,answer_state)
            break

    # this statement will implement when player will able to guess all the states and UT of India
    if len(correct_guees) == 36:
        msg.hideturtle()
        msg.write(f"Congratulations You Guessed All the States!", align="center", font=("Georgia", 18, "normal"))
        msg.color("red")
        should_continue = False


all_state_list = data["State"].to_list()

# this for loop will give us the all the states which user has missed out to guess so he can check which state UT he has missed
for missing_state in all_state_list:

    if missing_state in correct_guees:
        all_state_list.pop(all_state_list.index(missing_state))

missed_state = pandas.DataFrame(all_state_list)

missed_state.to_csv("states_to_learn.csv")




