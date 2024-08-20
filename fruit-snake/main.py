from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Fruit Snake")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()

# Listen to events
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Press 'x' to exit the game
screen.onkey(key="x", fun=score.game_over)

while not score.exit:
    screen.update()
    snake.move()  # Move snake

    # If food is close to the snake head, relocate food position
    if snake.head.distance(food) < 15:
        food.relocate()  # Relocate food to a diff position
        snake.grow()  # Increase snake size
        score.add_point()  # Increment score

    # Check for snake collides
    if snake.check_collision():
        # Reset game
        score.reset_score()
        food.relocate()
        snake.reset_snake()
