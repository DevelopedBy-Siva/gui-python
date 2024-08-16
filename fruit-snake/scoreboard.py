from turtle import Turtle

STYLE = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        """
        Initialize the scoreboard
        """
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(0, 270)
        self.refresh_score()

    def add_point(self):
        """
        Increases the score by one point and updates the scoreboard
        """
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        """
        Clear and update the scoreboard
        """
        self.clear()
        self.write(f"Score: {self.score}", False, font=STYLE, align="center")

    def game_over(self):
        """
        Clear and display 'Game Over'
        """
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", False, font=STYLE, align="center")
