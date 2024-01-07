from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

playing = True

while playing:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()
