from turtle import  Turtle, Screen
import  random


# here we are setting screen size and other required
screen =  Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a turtle color: ")


color_list = ["red", "orange", "Gray", "green", "blue", "purple"]
turtle_list = []
X_AXIS = -230
Y_AXIS = -100

# This for loop will assign each turtle a specific starting position in the screen
for turtles_position in range(len(color_list)):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(color_list[turtles_position])
    turtle.goto(x=X_AXIS, y=Y_AXIS)
    turtle_list.append(turtle)

    Y_AXIS += 40

# this finish line object is used to create for a finish line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.speed("fastest")
finish_line.goto(210, 200)
finish_line.left(360)
finish_line.pendown()
finish_line.goto(210, -200)
finish_line_coord = 214

# this display_winner object is created for showing the winner on screen.
display_winner = Turtle()
display_winner.hideturtle()
display_winner.penup()
display_winner.speed("fastest")

if user_choice:
    is_game_on = True

while is_game_on:

    # this for loop will help to move turtle forward at random pace and also help to decide a winner
    for turtles_movement in turtle_list:
        turtle_coord = int(turtles_movement.xcor())

        # if any turtle coordinate became greater than finish line coordinate than this statement will implement
        if turtle_coord >= finish_line_coord:

            winner_turtle = turtles_movement.pencolor()
            is_game_on = False

            if user_choice == winner_turtle:
                display_winner.color(winner_turtle)
                display_winner.write(arg = f"You've have Won!, The {winner_turtle} turtle is the winner!", align= "center")

            else:
                display_winner.color(winner_turtle)
                display_winner.write(arg = f"You've have Lost!, The {winner_turtle} turtle is the winner!", align= "center")

        # if each turtle coordinate don't match or become greater than finish_Line coord than this statment will implement and
        elif turtle_coord != finish_line_coord:

            # below statement will help to move forward each turtle at random pace
            random_distance = random.randint(0,10)
            turtles_movement.forward(random_distance)

screen.exitonclick()