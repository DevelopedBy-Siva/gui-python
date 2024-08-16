import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        # Create the food at a random position
        self.relocate()

    def relocate(self):
        """
        Create/Move the food to a new random position
        """
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto((x_cor, y_cor))
