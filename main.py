from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()


# Listen to keyboard input
screen.listen()

# Keyboard bindings for right paddle (up/down arrow keys)
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

# Keyboard bindings for left paddle ('w' and 's' keys)
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)     # Use ball's current speed
    screen.update()
    ball.move()

    # Check for collision with the top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check for collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Check for collision with the left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Reset the ball if it goes out of bounds
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

# Keep screen open when game ends
screen.mainloop()
