from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score

# time module will help us to reduce the loop speed which help us to increase or decrease ball speed.
import  time

# here we are creating objects of our all classes
screen = Screen()
winner = Turtle()
paddle_l = Paddle()
ball = Ball()
score = Score()


# here we are setting the position of our paddle
paddle_l.goto(-390, 0)
paddle_r = Paddle()
paddle_r.goto(380, 0)

# here we are setting the width and height of our gaming screen
screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.tracer(0)

#here we are using onkey function so whenever player gives an valid input paddle will move up and down
screen.listen()
screen.onkey(key= "r", fun= paddle_l.up)
screen.onkey(key= "d", fun= paddle_l.down)
screen.onkey(key= "Up", fun= paddle_r.up)
screen.onkey(key= "Down", fun= paddle_r.down)
speed_up = 0.10

game_is_on = True
while game_is_on:

    ball.movement()

    # whenever ball passes this coordinate in a screen of y axis ball will bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # whenever ball distance with paddle is less than 50px and ball coordinate is greater than 355 than this if statement
    # and ball will bounce back from paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 355 or ball.distance(paddle_l) < 50 and ball.xcor() < -355:
        ball.bounce_x()
        speed_up -= 0.01

    # when r_paddle miss the score points go to l_paddle
    if ball.xcor() > 390:
        score.l_score += 1
        score.update_screen()
        ball.reset_position()
        speed_up = 0.10


    # when l_paddle miss the score points go to r_paddle
    if ball.xcor() < -390:
        score.r_score += 1
        score.update_screen()
        ball.reset_position()
        speed_up = 0.10

    # whichever paddle reaches 10 first will win the game
    if score.l_score == 10 or score.r_score == 10:
        winner.color("white")
        winner.hideturtle()
        winner.penup()
        if score.r_score == 10:
            winner.write(f"right paddle wins!", align="center", font=("Arial", 24, "normal"))
        if score.l_score == 10:
            winner.write(f"left paddle wins!", align="center", font=("Arial", 24, "normal"))

        ball.hideturtle()
        game_is_on = False

    time.sleep(speed_up)
    screen.update()

screen.exitonclick()
