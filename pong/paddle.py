from turtle import Turtle

from data import (
    PADDLE_LIMIT_UP,
    PADDLE_LIMIT_DOWN,
    DISTANCE_TO_COVER,
)


class Paddle(Turtle):

    def __init__(self, pos_x):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=0.6)
        self.color("white")
        self.setheading(90)
        self.goto(pos_x, 0)

    def up(self):
        # Limit reached. Cannot move the paddle further
        if self.ycor() >= PADDLE_LIMIT_UP:
            return
        distance = min(DISTANCE_TO_COVER, PADDLE_LIMIT_UP - self.ycor())
        self.forward(distance)

    def down(self):
        # Limit reached. Cannot move the paddle further
        if self.ycor() <= PADDLE_LIMIT_DOWN:
            return
        distance = max(-DISTANCE_TO_COVER, PADDLE_LIMIT_DOWN - self.ycor())
        self.forward(distance)
