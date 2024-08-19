import time
from turtle import Screen

from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
from divide import Divide
from data import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    PADDLE_POSITION_LEFT,
    PADDLE_POSITION_RIGHT,
)

# Setup screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turn 'OFF' animation

# Initialise left & right paddles
paddle_left = Paddle(PADDLE_POSITION_LEFT)
paddle_right = Paddle(PADDLE_POSITION_RIGHT)

# Initialise scoreboard
score = ScoreBoard()

# Split the screen
divide = Divide()

# Initialise Ball
ball = Ball(p_left=paddle_left, p_right=paddle_right)
screen.update()

# Listen to events
screen.listen()

# Left paddle events
screen.onkey(key="w", fun=paddle_left.up)
screen.onkey(key="s", fun=paddle_left.down)

# Right paddle events
screen.onkey(key="Up", fun=paddle_right.up)
screen.onkey(key="Down", fun=paddle_right.down)

# Loop util game is over
while not score.game_over():
    screen.update()
    # Control ball speed
    time.sleep(0.01)

    result_l, result_r = ball.move()
    if result_l != 0 or result_r != 0:
        score.add_score(result_l, result_r)
        ball.reset()
        time.sleep(0.5)  # Pause the game for smooth reset

# Clear screen and display game over
score.clear()
divide.clear()
score.display_game_over()

screen.exitonclick()
