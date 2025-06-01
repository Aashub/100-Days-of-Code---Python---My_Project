from turtle import  Turtle

class Level(Turtle):
    """here we are creating level for our turtle crossing game"""
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-330, 220)
        self.score = 0

    def write_score(self):
        """this method will display the level of player."""
        self.clear()
        self.write(arg=f"Level:{self.score}",move=False,font=("Arial",15,"normal"))

    def game_over(self):
        """this function will execute whenever turtle hits the game and game over happens to show game is over."""
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-50, 0)
        self.write(arg=f"Game Over", move=False, font=("Arial", 15, "normal"))







