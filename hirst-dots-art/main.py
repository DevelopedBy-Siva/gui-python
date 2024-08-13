import random
import turtle
import colorgram


# Extract the colors from 'art.jpg'
colors = colorgram.extract("art.jpg", 30)
color_codes = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_codes.append((r, g, b))


# Allow RGB
turtle.colormode(255)

# Turtle global configs
my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.speed("fastest")

# initialize the turtle position
my_turtle.setposition(-220, -220)

for count in range(1, 101):
    color = random.choice(color_codes)
    my_turtle.dot(20, color)
    my_turtle.forward(50)
    # Shift to one row above
    if count != 100 and count % 10 == 0:
        x, y = my_turtle.position()
        my_turtle.setposition(x=-220, y=y + 50)

# Screen
screen = turtle.Screen()
screen.exitonclick()
