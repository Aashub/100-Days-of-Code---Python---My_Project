from turtle import Turtle

TURTLE_COD = (0, -230)

class Turtle(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.goto(TURTLE_COD)
        self.shape("turtle")
        self.color("green")
        self.shapesize(1.5)
        self.setheading(90)


    def turtle_up(self):
        """this function will move the turtle in up direction"""

        ycor = self.ycor() + 5
        self.goto(self.xcor(), ycor)

    def turtle_down(self):
        """this function will move the turtle in down direction"""

        ycor = self.ycor() - 10
        self.goto(self.xcor(), ycor)



