from turtle import  Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
class Score(Turtle):
    """the main purpose of this class is to update the score whenever snakes eat a food"""

    def __init__(self):
        super().__init__()
        self.num = 0
        self.score_card()

    def game_over(self):
        """this function will show the game over prompt whenever snake hits the wall or collide with his own body"""
        self.goto(x=0, y=0)
        self.write(f"Game Over!", True, align=ALIGNMENT, font=FONT)


    def score_card(self):
        """this function will align the position of score card in top of the screen."""
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.num}", True, align=ALIGNMENT, font= FONT)

