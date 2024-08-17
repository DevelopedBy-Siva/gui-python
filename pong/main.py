from turtle import Screen

from paddle import Paddle
from scoreboard import ScoreBoard
from splitscreen import SplitScreen
from data import SCREEN_HEIGHT, SCREEN_WIDTH, LEFT, RIGHT

# Setup screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turn 'OFF' animation

# Initialise left & right paddles
paddle_left = Paddle(LEFT)
paddle_right = Paddle(RIGHT)
# Initialise scoreboard
score = ScoreBoard()
# Split the screen
__ = SplitScreen()

screen.update()
screen.tracer(1)  # turn 'ON' animation

# Listen to events
screen.listen()

# Left paddle events
screen.onkey(key="w", fun=paddle_left.up)
screen.onkey(key="s", fun=paddle_left.down)

# Right paddle events
screen.onkey(key="Up", fun=paddle_right.up)
screen.onkey(key="Down", fun=paddle_right.down)

screen.exitonclick()
