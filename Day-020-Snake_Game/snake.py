from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """this class main functionality is that it creates snake and increases snake size whenever it eats food"""
    def __init__(self):
        self.snake_list = []
        self.x_axis = 0
        self.y_axis = 0

    def snake_object(self):
        """this function create objects for snake body and also add them in a list."""
        for body_part in range(3):
            snake = Turtle("square")
            snake.color("white")
            self.snake_list.append(snake)

    def snake_body(self):
        """this function align the snake body in a certain location so they snake actually looks like a snake."""
        for snake_body in self.snake_list:
            snake_body.penup()
            snake_body.goto(self.x_axis, self.y_axis)
            self.x_axis -= 20

    def extend(self):
        """this function will increase the snake size by creating a new object of snake and appending it into a list
        and adding them into a end of body."""
        snake_extend = Turtle("square")
        snake_extend.color("white")
        snake_extend.penup()
        snake_extend.goto(self.x_axis, self.y_axis)
        self.snake_list.append(snake_extend)

    def snake_movement(self):
        """this function will help the snake to move in any direction without losing its body, so whenever snake head
        make any turn other snake body also take turns"""
        for set_num in range(len(self.snake_list)-1, 0, -1):
            new_x = self.snake_list[set_num - 1].xcor()
            new_y = self.snake_list[set_num - 1].ycor()
            self.snake_list[set_num].goto(new_x, new_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    # below four function will help us to move snake into all four direction with also preventing the condition of
    # not coming back word because snake can move only forward.

    def up(self):
        if self.snake_list[0].heading() != DOWN:
            self.snake_list[0].setheading(UP)

    def down(self):
        if self.snake_list[0].heading() != UP:
            self.snake_list[0].setheading(DOWN)

    def left(self):
        if self.snake_list[0].heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)

    def right(self):
        if self.snake_list[0].heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)

