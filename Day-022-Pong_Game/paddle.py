from turtle import Turtle

MOVE_DISTANCE = 30

class Paddle(Turtle):

    def __init__(self):
        super().__init__()

        self.paddle_list = []
        self.create_paddle()
        self.r_paddle = self.paddle_list[0]
        self.l_paddle = self.paddle_list[1]

        self.r_paddle_xcor = self.r_paddle.xcor()
        self.l_paddle_ycor = self.l_paddle.xcor()

    def create_paddle(self):
        """this method will set paddle details and also create a paddle"""

        for each_iterate in range(0,2):

            paddle = Turtle("square")
            paddle.penup()
            paddle.shapesize(stretch_wid=1, stretch_len=4)
            paddle.color("white")
            paddle.setheading(90)
            self.paddle_list.append(paddle)


    def paddle_location(self):
        """this method will help in setting paddle location in left and right side."""

        for paddle in range(len(self.paddle_list)):
            if paddle == 0:
                self.paddle_list[0].goto(430,0)
            elif paddle == 1:
                self.paddle_list[1].goto(-440,0)

    def up_movement_right_paddle(self):
        """method for moving right paddle up"""

        if self.r_paddle.ycor() > 240:
            return

        right_paddle = self.paddle_list[0]
        right_paddle.forward(MOVE_DISTANCE)

    def up_movement_left_paddle(self):
        """method for moving left paddle up"""

        if self.l_paddle.ycor() > 240:
            return

        left_paddle = self.paddle_list[1]
        left_paddle.forward(MOVE_DISTANCE)

    def down_movement_right_paddle(self):
        """method for moving right paddle down"""

        if self.r_paddle.ycor() < -280:
            return

        right_paddle = self.paddle_list[0]
        right_paddle.forward(-MOVE_DISTANCE)

    def down_movement_left_paddle(self):
        """method for moving right paddle down"""

        if self.l_paddle.ycor() < -280:
            return

        left_paddle = self.paddle_list[1]
        left_paddle.forward(-MOVE_DISTANCE)




