import pandas as pd
from turtle import Screen

from marker import Marker

# Configure Screen
screen = Screen()
screen.tracer(0)
screen.bgpic("blank_states.gif")

# Read all the 50 states
states = pd.read_csv("50_states.csv")
states["state"] = states["state"].str.lower()

score = 0

# Loop until the user 'exit' or predicts all the states
while not states.empty:
    user_input = screen.textinput(
        f"{score}/50 States Correct", "What's another state name?"
    )
    # If no input provided, re-run the loop
    if user_input == None:
        continue
    # Exit the game
    if user_input.lower() == "exit":
        break

    # Match the user input against the states and get the corresponding coordinates
    state = states[states["state"] == user_input.lower()]
    if not state.empty:
        X = state.head(1)["x"].item()
        Y = state.head(1)["y"].item()

        # Remove the row from the DataFrame where a user input is matched
        states = states.drop(index=state.index)
        score += 1
        # Turtle to place each state name on the image
        Marker(X=X, Y=Y, name=user_input)
        screen.update()

# Save all the missed states to a separate CSV
states["state"].reset_index(drop=True).to_csv("missed_states.csv")
# Close the screen
screen.bye()
