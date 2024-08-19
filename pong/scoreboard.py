from turtle import Turtle

from data import SCREEN_HEIGHT, WINNING_POINT


class ScoreBoard(Turtle):
    def __init__(self):
        # Initialise Scoreboard
        super().__init__()
        self.score_paddle_left = 0
        self.score_paddle_right = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, SCREEN_HEIGHT / 2.7)
        # Show the score
        self.refresh_score()

    def refresh_score(self):
        # Clear and update the scoreboard
        self.clear()
        self.__display_txt(
            f"{self.score_paddle_left}      {self.score_paddle_right}", 60
        )

    def add_score(self, result_l, result_r):
        # Increment Score
        self.score_paddle_left += result_l
        self.score_paddle_right += result_r
        self.refresh_score()

    def game_over(self):
        # Check game is over or not
        return (
            self.score_paddle_left == WINNING_POINT
            or self.score_paddle_right == WINNING_POINT
        )

    def display_game_over(self):
        # Display GAME OVER message
        self.home()  # Adjust pos to middle
        self.__display_txt()  # Display GAME OVER by default

        # Check which player won and display
        result = "Player 2 won the game"
        if self.score_paddle_left > self.score_paddle_right:
            result = "Player 1 won the game"
        self.goto(0, -30)
        self.__display_txt(f"{result}", 15, "normal")

    def __display_txt(self, result="GAME OVER", font_size=42, font_weight="bold"):
        self.write(result, font=("Verdana", font_size, font_weight), align="center")
