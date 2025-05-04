from turtle import Screen, Turtle
from random import randint

# turtle color list
color_list = ["red", "blue", "green", "yellow", "cyan", "purple"]

def create_turtle(color):
    """in this function we are creating 6 object for each turtle and also assigning each turtle object specific color from the color list."""

    turtle_object_list = []
    for create_objects in color_list:
        timmy = Turtle(shape="turtle")
        timmy.color(create_objects)

        turtle_object_list.append(timmy)

    return turtle_object_list

def starting_line(turtle_race):
    """this function will move each turtle to the starting line"""
    y_axis = -50
    x_axis = 280

    for starting_positing in turtle_race:
        starting_positing.penup()
        starting_positing.goto(x=-x_axis, y = y_axis)
        y_axis += 30

def move_turtle(turtles_, user_color, race_on):
    """this function will move each turtle at random pace and also check that turtle has crossed the finish line or not"""

    # this for loop will run until any turtle don't reach the final line
    for turtle_move in turtles_:
        if turtle_move.xcor() > 250:
            winning_color = turtle_move.pencolor()
            if winning_color == user_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


            race_on = False
            return race_on

        turtle_move.forward(randint(1, 10))


def draw_finish_line(f_line):
    """this function is used to create the finish line."""
    f_line.hideturtle()
    f_line.speed("fastest")
    f_line.penup()
    print(f_line.goto(x=240, y=-140))
    f_line.pendown()
    f_line.setheading(90)
    f_line.forward(300)


screen = Screen()
screen.setup(width=600, height=500)

#function calling
finish_line = Turtle()
draw_finish_line(finish_line)

user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color: ")

#function calling
turtles = create_turtle(color_list)
starting_line(turtles)

is_race_on = False

#here we will check that user has provided the correct color input  or not if yes then only race will start.
for correct_bet in color_list:

    if user_bet == correct_bet:
        is_race_on = True

# this while loop will run until the is_race_on condition doesn't became false
while is_race_on:
    stop_race = move_turtle(turtles, user_bet, is_race_on)
    if stop_race == False:
        is_race_on = False


screen.exitonclick()
