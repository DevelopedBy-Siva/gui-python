import random
from turtle import Turtle

from data import BALL_COVERS


class Ball(Turtle):

    def __init__(self, p_left, p_right):
        super().__init__()
        self.paddles = (p_left, p_right)
        self.penup()
        self.shape("circle")
        self.color("white")
        self.__initialize_bounce_direction()

    def move(self):
        result = (0, 0)

        x, y = self.position()

        # Check top and bottom collisions
        if abs(y) > 280:
            self.setheading(-self.heading())

        # Check collisions with the paddles
        if abs(x) > 350:
            if (
                self.distance(self.paddles[0]) < 50
                or self.distance(self.paddles[1]) < 50
            ):
                self.setheading(180 - self.heading())
            # Paddle Left gained a point
            elif x > 400:
                result = (1, 0)
            # Paddle Right gained a point
            elif x < -410:
                result = (0, 1)

        # Move the ball
        self.forward(BALL_COVERS)
        return result

    def reset(self):
        # Override turtle reset
        self.home()
        self.__initialize_bounce_direction()

    def __initialize_bounce_direction(self):
        # Randomize initial bounce direction
        initial_angle = random.randint(30, 60)
        self.setheading(initial_angle)
