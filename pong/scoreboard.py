from turtle import Turtle

from data import SCREEN_HEIGHT

STYLE = ("Arial", 70, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        # Initialise Scoreboard
        super().__init__()
        self.score_paddle_left = 0
        self.score_paddle_right = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, SCREEN_HEIGHT / 2.6)
        # Show the score
        self.refresh_score()

    def refresh_score(self):
        # Clear and update the scoreboard
        self.clear()
        self.write(
            f"{self.score_paddle_left}      {self.score_paddle_right}",
            False,
            font=STYLE,
            align="center",
        )
