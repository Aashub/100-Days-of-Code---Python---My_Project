from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 240


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.shapesize(1.5)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.color("green")

    # this method will move turtle forward
    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    # this method will move turtle backward
    def move_backward(self):
        self.backward(MOVE_DISTANCE)

    # this method will bring turtle to starting position after he crosses finish line.
    def rest_turtle_position(self):
        self.goto(STARTING_POSITION)



