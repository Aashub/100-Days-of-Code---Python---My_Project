from turtle import Screen
from snake import Snake
from food import  Food
from score import Score

import  time
screen = Screen()

#here we have mentioned basic details of our snake games like screen width and screen color.
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# here we have created object from all the classes that we are going to use to call the methods so our game can
#perform all the functionality
snake = Snake()
snake_food = Food()
score = Score()

snake.snake_object()
snake.snake_body()

# here we are binding keys so whenever the user press the key our snake can move into specific direction.
screen.listen()
screen.onkey(key="Up", fun= snake.up)
screen.onkey(key="Down", fun= snake.down)
screen.onkey(key="Left", fun= snake.left)
screen.onkey(key="Right", fun= snake.right)

# here loop will run until the condition doesn't became false
game_is_on = True
while game_is_on:
    screen.update()

    time.sleep(0.1)
    # here we are checking that if snake head distance with food is less than 15 than we will refresh the food
    # so it can go to different location and snake body size also increases and score also increases
    if snake.snake_list[0].distance(snake_food) < 15:
        snake_food.refresh()
        snake.extend()

        #whenever this if statement will executed then score.increase_score will increase the score by one in score class method
        score.increase_score += 1
        score.clear()
        score.score_card()

    #detect collision with wall
    if snake.snake_list[0].xcor() > 270 or snake.snake_list[0].xcor() < -270 or snake.snake_list[0].ycor() > 255 or snake.snake_list[0].ycor() < -270:
        score.reset_score()
        score.score_card()
        snake.reset_snake_body()

    #detect collision with tail
    #if head collides with own body then trigger game over
    for body_part in snake.snake_list[1:]:
        if snake.snake_list[0].distance(body_part) < 10:
            score.reset_score()
            score.score_card()
            snake.reset_snake_body()

    snake.snake_movement()

screen.exitonclick()
