from turtle import Turtle

from data import (
    SCREEN_WIDTH,
    PADDLE_OFFSET_LEFT,
    PADDLE_OFFSET_RIGHT,
    PADDLE_LIMIT_UP,
    PADDLE_LIMIT_DOWN,
    LEFT,
)


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=0.6)
        self.color("white")
        self.setheading(90)

        if position == LEFT:
            self.goto(-SCREEN_WIDTH / 2 + PADDLE_OFFSET_LEFT, 0)
        else:
            self.goto(SCREEN_WIDTH / 2 - PADDLE_OFFSET_RIGHT, 0)

    def up(self):
        # Limit reached. Cannot move the paddle further
        if self.ycor() >= PADDLE_LIMIT_UP:
            return
        distance = min(40, PADDLE_LIMIT_UP - self.ycor())
        self.forward(distance)

    def down(self):
        # Limit reached. Cannot move the paddle further
        if self.ycor() <= PADDLE_LIMIT_DOWN:
            return
        distance = max(-40, PADDLE_LIMIT_DOWN - self.ycor())
        self.forward(distance)
