from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        # creating a ball
        self.ball = Turtle("circle")
        self.ball.penup()
        self.ball.color("white")
        self.speed("slowest")

        self.ball_speed = 0.2
        self.ball_hit = False

    def ball_movement(self, ball_direction):
        """this method will set ball heading & make sure ball move forward at certain speed and give x y cord of ball"""

        self.ball.setheading(ball_direction)
        self.ball.forward(self.ball_speed)

        x_cor = round(self.ball.xcor(), 2) + 20
        y_cor = round(self.ball.ycor(), 2)


        return x_cor, y_cor

    def collision_with_wall(self, ball_direction):
        """this method will help in change direction after hitting the wall."""

        new_heading = 360 - ball_direction
        return new_heading

    def collision_with_paddle(self, ball_direction):
        """this method will help is change the ball direction after hitting paddle"""

        random_num = random.randint(0, 14)

        # here are also increasing ball speed.
        if not self.ball_hit:
            self.ball_speed += 0.05
            self.ball_hit = True

        print(self.ball_speed)

        new_heading = (180 - ball_direction) + random_num
        return new_heading


