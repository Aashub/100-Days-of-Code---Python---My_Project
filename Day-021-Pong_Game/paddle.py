from turtle import Turtle


class Paddle(Turtle):
    """here we are inheriting from turtle class so we can use its method and attribute to create our modified methods and attributes"""

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        """this function will help us to move our paddle up"""
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)

    def down(self):
        """this function will help us to move our paddle up"""
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)











