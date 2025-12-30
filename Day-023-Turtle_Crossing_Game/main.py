import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=700, height=600)
screen.tracer(0)

turtle_obj = Player()
car_obj = CarManager()
score_obj = Scoreboard()

# key binding for turtle movement.
screen.listen()
screen.onkey(fun=turtle_obj.move_forward, key="Up")
screen.onkey(fun=turtle_obj.move_backward, key="Down")

game_is_on = True
while game_is_on:
    random_chance = random.randint(1, 5)

    time.sleep(0.1)
    screen.update()

    # this if statement will help in create a car at random pace with different coordinates
    if random_chance == 1:
        car_obj.create_car(random_chance)

    # whenever turtle crosses the finish line this statement call below method and increase level, reset turtle position and increase car speed.
    if turtle_obj.ycor() > FINISH_LINE_Y:
        score_obj.increase_level()
        turtle_obj.rest_turtle_position()
        car_obj.increase_car_speed()

    # if this condition return value came out as true than it will call game over over method
    if car_obj.collision_with_turtle(turtle_obj):

        game_is_on = False
        score_obj.game_over()

    car_obj.car_movement()

screen.exitonclick()