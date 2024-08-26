from turtle import Turtle


class Marker(Turtle):
    def __init__(self, X, Y, name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(x=X, y=Y)
        self.write(f"{name.title()}")
