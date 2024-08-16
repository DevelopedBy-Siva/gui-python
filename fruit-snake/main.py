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

# Loop until snake collides
while not snake.check_collision():
    screen.update()
    snake.move()  # Move snake

    # If food is close to the snake head, relocate food position
    if snake.head.distance(food) < 15:
        food.relocate()  # Relocate food to a diff position
        snake.grow()  # Increase snake size
        score.add_point()  # Increment score

# Display game over message on the screen
score.game_over()

screen.exitonclick()
