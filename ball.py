from turtle import Turtle


class Ball(Turtle):
    """Initialize ball at (0, 0) and set its movement"""

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(5)
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1   # Initial movement speed (lower = faster)

    def move(self):
        """Move the ball in the current direction"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounce the ball when it hits the top or bottom wall"""
        self.y_move *= -1

    def bounce_x(self):
        """Bounce the ball when it hits the paddle"""
        self.x_move *= -1
        self.move_speed *= 0.9  # Increase speed by 10%

    def reset_position(self):
        """Reset the ball to the center after scoring"""
        self.goto(0, 0)
        self.move_speed = 0.1   # Reset the speed
        self.bounce_x() # Send the ball in the opposite direction
