from turtle import Turtle, Screen

# W -> Move Forward
# S -> Move Backward
# D -> Turn Right
# A -> Turn Left


# Forward
def move_forward():
    my_turtle.forward(10)


# Backward
def move_backward():
    my_turtle.backward(10)


# Right
def turn_right():
    heading = my_turtle.heading() - 10
    my_turtle.setheading(heading)


# Left
def turn_left():
    heading = my_turtle.heading() + 10
    my_turtle.setheading(heading)


# Reset sketch
def reset_sketch():
    my_turtle.reset()


my_turtle = Turtle()

screen = Screen()
screen.listen()

# Listener events
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=reset_sketch, key="c")

screen.exitonclick()
