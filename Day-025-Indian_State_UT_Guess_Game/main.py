import pandas
from turtle import Screen, Turtle
from tkinter import messagebox


def write_state_name(state_d, map, guessed_state):
    """this function will write the guessed state on the screen."""

    state = state_d[state_d.Name == guessed_state]
    x_cor = state.Center_X.item()
    y_cor = state.Center_Y.item()

    map.penup()
    map.color("red")
    map.goto(x_cor, y_cor)
    map.write(arg=guess, align= "center", font=("Courier",9, "normal"))


def unanswered_state_list(correct_guesses, all_states):

    unanswered_state = []
    for state in all_states:
        if state in correct_guesses:
            pass
        else:
            unanswered_state.append(state)
            new_data = pandas.DataFrame(unanswered_state)
            new_data.to_csv("states_to_learn.csv")


screen = Screen()
map_obj = Turtle()
map_obj.hideturtle()

screen.bgpic("India_blank_state_map_img.gif")
state_data = pandas.read_csv("india_states_ut_centers.csv")

screen.tracer(0)

state_name = state_data.Name
total_state = len(state_name)
correct_guess = 0

correct_guess_list = []
game_is_on = True

# this while loop will run until user don't guess all the correct guesses.
while game_is_on:
    screen.update()
    guess = screen.textinput(title=f"{correct_guess}/{total_state} States Correct", prompt="What's another state name? type exit for exiting game.").title()

    if guess == "Exit":
        unanswered_state_list(correct_guess_list, state_name)
        break

    # this for loop will check that use has guessed the correct guess or not.
    for state in state_name:
        if state == guess:

            # this if condition prevent from if user guesses the same guess which he has done previously than it will not increase the correct guess number.
            if guess not in correct_guess_list:
                correct_guess += 1
                correct_guess_list.append(guess)
                write_state_name(state_data, map_obj, guess)

        if correct_guess == total_state:
            messagebox.showinfo("congratulations.", "you guessed all 28 Indian states & 8 Union Territory.")
            screen.exitonclick()