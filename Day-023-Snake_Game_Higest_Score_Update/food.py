from turtle import Turtle
import random

class Food(Turtle):
    """this class main purpose is to create a food for snake and move it into random direction whenever
    snake eats the food."""

    def __init__(self):
        """by using super().__init__() we are inheriting all the properties of turtle module which we have used to create
        snake food."""
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """this function will refresh the food location in a random location in a screen"""
        x_axis = random.randint(-270, 270)
        y_axis = random.randint(-270, 270)
        self.goto(x_axis,y_axis)

