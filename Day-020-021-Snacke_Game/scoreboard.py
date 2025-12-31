from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()

        # this will open the data file and read the content stored in it.
        with open(file="data.txt", mode= "r") as file:
            self.high_score = int(file.read())

        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,278)
        self.boarder_line()
        self.update_scoreboard()


    def reset_scoreboard(self):

        if self.score > self.high_score:
            self.high_score = self.score

            # this will update the new highest score in the dat.txt file and when next time someone reads it that will appear as high score.
            with open(file="data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center",
                   font=('Courier', 15, 'normal'))

    def increase_score(self):
        """this method will help to increase the score whenever snake eat the food"""

        self.score += 1
        self.update_scoreboard()


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
