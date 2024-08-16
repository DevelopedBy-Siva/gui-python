from turtle import Screen

from snake import Snake
from food import Food

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Fruit Snake")
screen.tracer(0)


snake = Snake()
food = Food()

# Listen to events
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while not snake.check_collision():
    screen.update()
    snake.move()  # Move snake

    # If food is close to the snake head, relocate food position
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.grow()

screen.exitonclick()
