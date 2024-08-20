import time
from turtle import Turtle

SNAKE_SPEED = 0.1
DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        self.setup_initial_snake()  # setup initial snake body
        self.head = self.snake_body[0]

    def setup_initial_snake(self):
        """
        Create a snake with 3 parts
        """
        for pos in range(3):
            body_part = self.construct_part()
            body_part.goto((-pos * DISTANCE, 0))  # x & y coordinates
            self.snake_body.append(body_part)

    def construct_part(self):
        """
        Creates a turtle object representing each snake part
        Returns:
            Turtle: A snake turtle object
        """
        body_part = Turtle(shape="square")
        body_part.penup()
        body_part.color("white")
        return body_part

    def grow(self):
        """
        Increases the size of the snake by adding a new part.
        """
        body_part = self.construct_part()
        x, y = self.snake_body[-1].position()  # Get the tail coordinates
        body_part.goto((x, y))  # x & y coordinates
        self.snake_body.append(body_part)

    def move(self):
        """
        Move the snake's head forward by 20 units.
        The rest of the body moves by shifting each part to the prev position of the part in front of it.
        """
        time.sleep(SNAKE_SPEED)  # Control snake speed

        no_of_segments = len(self.snake_body) - 1
        for idx in range(no_of_segments, 0, -1):
            x, y = self.snake_body[idx - 1].position()
            self.snake_body[idx].goto((x, y))
        self.head.fd(DISTANCE)

    def check_collision(self):
        """
        Check if snake collided or gone past the screen
        Returns:
            boolean: If game over, returns True, else False
        """
        # Check head collide with the wall
        x, y = self.head.position()
        if abs(x) > 280 or abs(y) > 280:
            return True

        # Check snake head collide with the tail
        for part in self.snake_body[1:]:
            if self.head.distance(part) < 10:
                return True
        return False

    def reset_snake(self):
        """
        Reset the snake
        """
        # Hide the existing snake
        for body in self.snake_body:
            body.hideturtle()

        self.snake_body.clear()
        self.setup_initial_snake()
        self.head = self.snake_body[0]

    def up(self):
        """
        Move the snake's head upward when 'Up' key is pressed.
        """
        self.update_head_position((90, 270))

    def down(self):
        """
        Move the snake's head upward when 'Down' key is pressed.
        """
        self.update_head_position((270, 90))

    def left(self):
        """
        Move the snake's head upward when 'Left' key is pressed.
        """
        self.update_head_position((180, 0))

    def right(self):
        """
        Move the snake's head upward when 'Right' key is pressed.
        """
        self.update_head_position((0, 180))

    def update_head_position(self, directions: tuple):
        """
            Checks if head direction needs to be changed or not,
            and head is updated accordingly.

        Args:
            directions (tuple): Allowed directions.
            Direction at index '0' is used to update the head
        """
        direction = int(self.head.heading())
        if direction not in directions:
            self.head.seth(directions[0])
