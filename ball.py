from turtle import Turtle
import random

DIRECTION = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.choice(DIRECTION))
        self.move_speed = 0.1

    def move(self):
        self.forward(10)

    def bounce_y(self):
        self.setheading(360 - self.heading())

    def bounce_x(self):
        self.setheading(180 - self.heading())
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.111
