from turtle import Screen
import time
from snake import Snake
from food import  Food
from scoreboard import Score

# setting the screen size
screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

# here we are binding the each key so wherever the key is being pressed snake change the direction
screen.listen()
screen.onkey(fun= snake.move_right, key= "Right")
screen.onkey(fun= snake.move_left, key= "Left")
screen.onkey(fun= snake.move_up, key= "Up")
screen.onkey(fun= snake.move_down, key= "Down")

should_continue = True

# game will run until condition doesn't became false
while should_continue:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # this condition will help to increase the snake size and increase score
    if snake.head.distance(food) < 15:
        score.clear()
        snake.extend_snake()
        score.increase_score()
        food.collision_with_food()

    # this condition will check if snake collided with the wall or not
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 279 or snake.head.ycor() < -280:
        should_continue = False
        score.write_game_over()


    for body_collision in snake.segment_list[1:]:

        if snake.head.distance(body_collision) < 10:
            should_continue = False
            score.write_game_over()

screen.exitonclick()