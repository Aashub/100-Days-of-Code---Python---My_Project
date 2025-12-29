from turtle import Turtle


UNTIL_Y_AXIS = -350
VERTICAL_LINE_AXIS = (0,360)
HORIZONTAL_LINE_AXIS = (-460,300)

class Boarder(Turtle):

    def __init__(self):
        super().__init__()
        self.reduce_num = 20

        self.border_list = []
        self.set_boarder_details()

        self.vertical_line = self.border_list[0]
        self.horizontal_line = self.border_list[1]

        self.draw_vertical_line()
        self.draw_horizontal_line()

    def set_boarder_details(self):
        """this method will help in setting borderline details for game"""

        for border in range(2):

            self.line = Turtle("square")
            self.line.shapesize(stretch_wid=0.3, stretch_len=1)
            self.line.hideturtle()
            self.line.penup()
            self.line.color("white")
            self.border_list.append(self.line)

            if border == 0:
                # for vertical line
                self.line.setheading(270)
                self.line.pensize(width=3)
                self.line.goto(VERTICAL_LINE_AXIS)

            elif border == 1:
                # for horizontal line
                self.line.setheading(0)
                self.line.pensize(width=2)
                self.line.goto(HORIZONTAL_LINE_AXIS)

    def draw_vertical_line(self):
        """this method will create vertical line till the end."""

        draw_until = True
        while draw_until:

            if self.vertical_line.ycor() > UNTIL_Y_AXIS:
                self.vertical_line.pendown()
                self.vertical_line.forward(10)
                self.vertical_line.penup()
                self.vertical_line.forward(10)

            elif self.vertical_line.ycor() < UNTIL_Y_AXIS:
                draw_until = False


    def draw_horizontal_line(self):
        """this method will create horizontal line."""

        self.horizontal_line.pendown()
        self.horizontal_line.goto(460, 300)
