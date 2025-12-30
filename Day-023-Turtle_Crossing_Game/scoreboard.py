from turtle import  Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.current_score = 0
        self.draw_horizontal_line()
        self.write_level()


    def write_level(self):
        # turtle created for writing on a screen
        self.hideturtle()
        self.penup()
        self.goto(-270, 260)
        self.write(arg=f"LEVEL:{self.current_score}", align="center", font=FONT)


    def increase_level(self):
        """this method will increase and update the level of game."""

        self.current_score += 1
        if self.current_score != 0:
            self.clear()

        self.write_level()

    def draw_horizontal_line(self):
        """this method will draw a horizontal finish line for the game."""

        line = Turtle()
        line.hideturtle()
        line.penup()
        line.goto(-350, 260)
        line.setheading(0)
        line.pendown()
        line.goto(350, 260)

    def game_over(self):
        """this method will display game over if turtle collides with car."""

        text = Turtle()
        text.hideturtle()
        text.penup()
        text.goto(0, 0)
        text.write(arg=f"GAME OVER!", align="center", font=FONT)



