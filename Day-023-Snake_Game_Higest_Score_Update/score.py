from turtle import  Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
class Score(Turtle):
    """the main purpose of this class is to update the score whenever snakes eat a food"""

    def __init__(self):
        super().__init__()
        self.increase_score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.score_card()
        self.reset_score()


    def reset_score(self):
        """this function is reset hte current score value and also update the highest score value."""
        if self.increase_score > self.highest_score:
            self.highest_score = self.increase_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.increase_score = 0

    def score_card(self):
        """this function will align the position of score card in top of the screen."""
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.increase_score}   Highest Score: {self.highest_score}", True, align=ALIGNMENT, font= FONT)

