from turtle import  Turtle


class Score(Turtle):
    """here we are inheriting from turtle class to create our Score class and use its methods and attribute"""

    def __init__(self):
        super().__init__()

        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.update_screen()


    def update_screen(self):
        """this function will align the score points in a specific location"""
        self.clear()
        self.goto(50, 245)
        self.write(self.l_score, move=False, font=("Arial", 40, "normal"))
        self.goto(-50, 245)
        self.write(self.r_score, move=False, font=("Arial", 40, "normal"))

