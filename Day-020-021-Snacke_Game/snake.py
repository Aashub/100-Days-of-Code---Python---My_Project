from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

body_tuple = [(0,0),(0,-20),(0,-40)]

class Snake:

    def __init__(self):
        self.x_cord = 20
        self.segment_list = []

        self.create_snake()
        self.head = self.segment_list[0]


    def create_snake(self):
        for body in body_tuple:
            self.add_segment(body)

    def add_segment(self, body):
        """this method will create a snake body."""

        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.goto(body)
        snake_segment.color("white")
        self.segment_list.append(snake_segment)

        self.x_cord -= 20

    def reset_snake(self):

        for off_screen in self.segment_list:
            off_screen.goto(500,500)

        self.segment_list.clear()
        self.create_snake()
        self.head = self.segment_list[0]

    def extend_snake(self):
        """this method will help in extend the snake body """
        self.add_segment(self.segment_list[-1].position())


    def move(self):
        """this method will help to move forward"""

        # this for loop will help to keep all the snake segment attach with each other so when snake change direction it the other part also follow that direction
        for movement in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[movement - 1].xcor()
            new_y = self.segment_list[movement - 1].ycor()
            self.segment_list[movement].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def move_right(self):
        """help to move right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        """help to move left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_up(self):
        """help to move up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        """help to move down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
