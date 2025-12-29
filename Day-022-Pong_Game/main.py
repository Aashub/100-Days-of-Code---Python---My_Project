
# all required classes
from turtle import Screen
from paddle import Paddle
from scoreboard import Score
from boarder import Boarder
from ball import Ball
import  random

def random_direction():
    """this function willl help for seating initial heading direction of pong ball"""
    DIRECTION_LIST = [(30, 70), (130, 160), (200, 230), (320, 330)]

    DIRECTION_TUPLE = random.choice(DIRECTION_LIST)
    BALL_HEADING = random.randint(DIRECTION_TUPLE[0], DIRECTION_TUPLE[1])

    return BALL_HEADING

# all objet
screen_object = Screen()
screen_object.tracer(0)
paddle_object = Paddle()
score_object = Score()
boarder_object = Boarder()
ball_object = Ball()

screen_object.bgcolor("black")
screen_object.setup(width=900, height=700)

paddle_object.paddle_location()
score_object.create_scorebboard()

screen_object.listen()

# all required key binding for paddle movement
screen_object.onkey(fun=paddle_object.up_movement_right_paddle, key="Up")
screen_object.onkey(fun=paddle_object.down_movement_right_paddle, key="Down")
screen_object.onkey(fun=paddle_object.up_movement_left_paddle, key="w")
screen_object.onkey(fun=paddle_object.down_movement_left_paddle, key="s")

BALL_HEADING = random_direction()

game_is_one = True
while game_is_one:
    """game will run until game is on condition doesn't became false"""

    ball_x_cor, y_cor = ball_object.ball_movement(BALL_HEADING)


    if y_cor > 290 or y_cor < -325:
        # if y cor is greater than those value than this method will get called and give us new heading after calling upper and lower wall.

        new_heading = ball_object.collision_with_wall(BALL_HEADING)
        BALL_HEADING = new_heading

    if ball_x_cor >= paddle_object.r_paddle.xcor() and ball_object.ball.distance(paddle_object.r_paddle) < 40 and not ball_object.ball_hit:
        # if ball x_xcor is greater than paddle x_cor and ball & paddle distance is less than 40 and ball not hit than this method will give us new direction

        new_heading = ball_object.collision_with_paddle(BALL_HEADING)
        BALL_HEADING = new_heading
        ball_object.ball_hit = True


    elif ball_x_cor >= paddle_object.l_paddle.xcor() and ball_object.ball.distance(paddle_object.l_paddle) < 25 and not ball_object.ball_hit:
        # if ball x_xcor is greater than paddle x_cor and ball & paddle distance is less than 25 and ball not hit than this method will give us new direction

        new_heading = ball_object.collision_with_paddle(BALL_HEADING)
        BALL_HEADING = new_heading
        ball_object.ball_hit = True

    # reset hit lock after ball leaves paddles
    if (
            ball_object.ball.distance(paddle_object.r_paddle) > 60 and
            ball_object.ball.distance(paddle_object.l_paddle) > 60
    ):
        ball_object.ball_hit = False

    if ball_object.ball.xcor() > 440:
        # bal xcor is greater than 440 than new left paddle score get increased and new ball at random direction will go

        score_object.left_score += 1
        score_object.increase_left_paddle_score()
        ball_object.ball.goto(0, 500)
        ball_object = Ball()

        BALL_HEADING = random_direction()

    elif ball_object.ball.xcor() < -440:
        # bal xcor is greater than -440 than new right paddle score get increased and new ball at random direction will go

        score_object.right_score += 1
        score_object.increase_right_paddle_score()
        ball_object.ball.goto(0, 500)
        ball_object = Ball()

        BALL_HEADING = random_direction()

    if score_object.right_score == 5 or score_object.left_score == 5:
        # if any side got the score equal to 5 than winner will be displayed

        if score_object.right_score == 5:
            winner = f"RIGHT SIDE WON!"
            score_object.display_winner(winner)
            ball_object.ball_hit = False

        elif score_object.left_score == 5:
            winner = f"LEFT SIDE WON!"
            score_object.display_winner(winner)
            ball_object.ball_hit = False

        game_is_one = False


    screen_object.update()

screen_object.exitonclick()