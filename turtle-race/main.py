import random
from turtle import Turtle, Screen

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Prepare the screen
screen = Screen()
screen.setup(width=500, height=400)

# User input prompt
while True:
    
    user_bet = screen.textinput(
        title="Make your best",
        prompt=f"Which turtle will win the race? Enter a color [ {", ".join(COLORS)} ]: ",
    )

    # Validate input
    if not user_bet or user_bet.lower() not in COLORS:
        print("Invalid input. Try again.")
        continue

    break

turtles = []

# Initial coordinates of the turtle
initial_x = -220
initial_y = -150

# To randomize turtle position (position is based on colors)
random.shuffle(COLORS)

# Create turtles and arrange them for the race
for color in COLORS:
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.color(color)
    my_turtle.goto(x=initial_x, y=initial_y)
    turtles.append(my_turtle)
    initial_y += 60

# Loop until a turtle crosses the line
winner = None
while not winner:
    
    winner_pos = 0
    for my_turtle in turtles:
        # Randomize the distance of each turtle
        distance = random.randint(0, 10)
        my_turtle.fd(distance)
        x = my_turtle.xcor()
        
        # Check for winner
        if x >= 225 and x > winner_pos:
            winner_pos = x
            winner = my_turtle.pencolor()


# Result
if winner == user_bet.lower():
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")

screen.exitonclick()
