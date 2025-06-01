import random
from turtle import Turtle
from random import randint

EASY = ["red", "blue", "green", "yellow", "orange"]
MODERATE = ["red", "blue", "green", "yellow", "orange", "purple", "black"]
HARD =  ["red", "blue", "green", "yellow", "orange", "purple", "black", "black", "cyan", "magenta"]

class Cars:
    """this class main purpose is to create cars and move them"""

    def __init__(self):

        self.car_list = []
        self.score = 0
        self.increase_speed = 10
        self.slow_creation = 0


    def create_cars(self):
        """this function is being used to create cars for the game."""

        #this if else statement is used to reduce the creation of cars.
        if self.slow_creation % 2 == 0:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(random.randint(360, 500), random.randint(-200, 250))
            car.color(random.choice(HARD))
            self.car_list.append(car)



    def car_movement(self):
        """this function objective is to move cars """

        for moving_car in self.car_list:
            xcor = moving_car.xcor() - self.increase_speed
            moving_car.goto(xcor, moving_car.ycor())

        self.create_cars()





















































