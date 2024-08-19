from turtle import Turtle

from data import SCREEN_HEIGHT

DASH_LENGTH = 20


class Divide(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.setheading(90)
        self.pensize(3)
        self.penup()
        # Set initial position
        self.setpos(0, -SCREEN_HEIGHT // 2 + DASH_LENGTH)

        # Draw dashed lines
        for pos in range(SCREEN_HEIGHT // DASH_LENGTH):
            if pos % 2 == 0:
                self.pendown()
            else:
                self.penup()
            self.forward(DASH_LENGTH)
