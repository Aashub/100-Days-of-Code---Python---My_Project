from turtle import Turtle

class Ball(Turtle):
    """here we are inheriting from turtle class to modify our ball class"""

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 8
        self.y_move = 8

    def movement(self):
        """this function will move our ball """

        ycor = self.ycor() + self.y_move
        xcor = self.xcor() + self.x_move
        self.goto(xcor, ycor)

    def bounce_y(self):
        """this function will help us to change the y coordinate so whenever ball hits upper and lower wall then it changes
        the y_move value into positive or negative which will help us to change direction after hitting wall"""
        self.y_move  *=  -1

    def bounce_x(self):
        """this function will help us to change the x coordinate so whenever ball hits left and right paddle then it changes
        the x_move value into positive or negative which will help us to change direction after hitting paddle"""
        self.x_move *= -1

    def reset_position(self):
        """this function will reset the position whenever players misses the ball so the game starts again from starting
        coordinates"""
        self.goto(0,0)




