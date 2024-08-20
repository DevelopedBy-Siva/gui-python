from turtle import Turtle

STYLE = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        """
        Initialize the scoreboard
        """
        super().__init__()
        self.score = 0
        self.high_score = self.__read_high_score()
        self.exit = False
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(0, 270)
        self.__refresh_score()

    def add_point(self):
        """
        Increases the score by one point and updates the scoreboard
        """
        self.score += 1
        self.__refresh_score()

    def reset_score(self):
        """
        Clear and display 'Game Over'
        """
        if self.score > self.high_score:
            self.high_score = self.score
            self.__save_high_score()

        self.score = 0
        self.__refresh_score()

    def __refresh_score(self):
        """
        Clear and update the scoreboard
        """
        self.clear()
        self.write(
            f"Score: {self.score}   High Score: {self.high_score}",
            False,
            font=STYLE,
            align="center",
        )

    def game_over(self):
        """
        Stop the game
        """
        self.exit = True

    def __read_high_score(self):
        with open("high_score.txt") as file:
            content = file.read()
        return int(content)

    def __save_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))
