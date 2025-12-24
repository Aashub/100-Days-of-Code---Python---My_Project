from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,278)
        self.increase_score()
        self.boarder_line()

    def write_game_over(self):
        """this method will write game over in the screen."""

        self.goto(0, 0)
        self.write(arg=f"Game Over!", align="center", font=('Courier', 15, 'normal'))

    def increase_score(self):
        """this method will help to increase the score whenever snake eat the food"""
        self.write(arg=f"Score: {self.score}", align="center", font=('Courier', 15, 'normal'))
        self.score += 1


    def boarder_line(self):
        """ this finish line object is used to create for a finish line"""
        line = Turtle()
        line.hideturtle()
        line.color("white")
        line.penup()
        line.speed("fastest")
        line.goto(-310, 280)
        line.left(360)
        line.pendown()
        line.goto(300, 280)
