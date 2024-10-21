from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        """Initialize the paddle with a specific position"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Move the paddle up, but stop at the top edge"""
        if self.ycor() < 250:   # Prevent moving out of bounds (top)
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """Move the paddle down, but stop at the bottom edge"""
        if self.ycor() > -240:  # Prevent moving out of bounds (bottom)
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

