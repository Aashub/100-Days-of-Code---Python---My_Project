from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5

class CarManager:

    def __init__(self):

        self.car_list = []

    def create_car(self, car):
        """this method will create a car. whenever this method is being called."""

        for car_creation in range(car):
            self.car = Turtle("square")
            self.car.shapesize(stretch_wid=1, stretch_len=2)
            self.car.penup()
            self.car.color(random.choice(COLORS))
            self.car.setheading(180)
            x_coordinate = random.randint(360, 420)
            y_coordinate = random.randint(-245, 245)
            self.car.goto(x_coordinate,y_coordinate)

            self.car_list.append(self.car)


    def car_movement(self):
        """this method will move forward each car."""

        for movement in self.car_list:
            movement.forward(STARTING_MOVE_DISTANCE)

    def increase_car_speed(self):
        """this method will increase the car  speed whenever turtle crosses the finish line."""

        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    def collision_with_turtle(self, turtle):
        """this method will check that car has collided with turtle or not and return True if collided."""

        for car_collision in self.car_list:

            if car_collision.distance(turtle) < 33:
                return True
        return None



