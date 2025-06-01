from turtle import Screen
from TURTLE import Turtle
from cars import Cars
from level import Level
import time


screen = Screen()
cars = Cars()

screen.tracer(0.1)

timmy = Turtle()

# here we are setting up the screen size
screen.setup(width=700, height= 500)
screen.title("Turtle Crossing Game")

# this function listen the key and as per that input turtle moves up and down,
screen.listen()
screen.onkey(fun=timmy.turtle_up, key="Up")
screen.onkey(fun=timmy.turtle_down, key="Down")

score_lvl = Level()
score_lvl.write_score()

cars.create_cars()
game_is_on = True

#while loop will run until the turtle don't hit the car and game don't become "game over"
while game_is_on:

    #here when each car distance will become less than 35 then game stops and game over happens
    for car in cars.car_list:
        if car.distance(timmy) < 35:
            score_lvl.game_over()
            game_is_on = False

    # here cars will move forward until the turtle coordinates are less than 260 in y axis
    if timmy.ycor() < 250:
        cars.car_movement()
        cars.slow_creation += 1

    # if turtle crosses y axis above 260 then here we can increaes its speed in next level and as per that we are writing
    # its current level.
    elif timmy.ycor() > 260:
        timmy.goto(0,-230)
        cars.increase_speed *= 1.5
        score_lvl.score += 1
        score_lvl.write_score()


    time.sleep(0.5)
    screen.update()

screen.exitonclick()
