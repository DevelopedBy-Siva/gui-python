from turtle import Turtle

from data import SCREEN_HEIGHT

DISTANCE_TO_MOVE = 15


class SplitScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.setheading(90)
        self.pensize(3)
        self.penup()
        # Set initial position
        self.setpos(0, -SCREEN_HEIGHT // 2 + 20)

        # Draw dashed lines
        for pos in range(SCREEN_HEIGHT // DISTANCE_TO_MOVE):
            if pos % 2 == 0:
                self.pendown()
            else:
                self.penup()
            self.forward(DISTANCE_TO_MOVE)
