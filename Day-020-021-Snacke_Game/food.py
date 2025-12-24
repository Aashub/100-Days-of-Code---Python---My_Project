from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.collision_with_food()

    def collision_with_food(self):
        """this method will check relocate the food in the random direction in a screen"""
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 275)
        self.goto(x_axis, y_axis)