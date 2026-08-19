from turtle import  Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0

        self.scorboard_list = []
        self.create_scorebboard()

        self.right_score_ob = self.scorboard_list[0]
        self.left_score_ob = self.scorboard_list[1]

        self.increase_right_paddle_score()
        self.increase_left_paddle_score()


    def create_scorebboard(self):
        """this method will create left and right side score and store them in a list"""

        for sc in range(2):
            self.score = Turtle()
            self.score.penup()
            self.score.hideturtle()
            self.score.color("white")
            self.scorboard_list.append(self.score)


    def increase_right_paddle_score(self):
        """thiis method will help in icrease  right side of score"""

        if self.right_score > 0:
            self.right_score_ob.clear()

        self.right_score_ob.goto(225, 295)
        self.right_score_ob.write(arg=f"{self.right_score}", align="center", font=('Courier', 40, 'normal'))

    def increase_left_paddle_score(self):
        """thiis method will help in icrease left side of score"""

        if self.left_score > 0:
            self.left_score_ob.clear()

        self.left_score_ob.goto(-225, 295)
        self.left_score_ob.write(arg=f"{self.left_score}", align="center", font=('Courier', 40, 'normal'))


    def display_winner(self, winner):
        """this method will display winner whoever scored the 5 points first."""

        self.winner = Turtle()
        self.winner.penup()
        self.winner.hideturtle()
        self.winner.color("white")
        self.winner.goto(0, 0)
        self.winner.write(arg=f"{winner}", align="center", font=('Courier', 45, 'normal'))

