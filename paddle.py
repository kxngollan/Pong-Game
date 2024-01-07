from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setheading(90)
        self.goto(x ,y)

    def up(self):
        y = self.ycor()
        if y > 235:
            pass
        else:
            y += 20
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor()
        if y < -235:
            pass
        else:
            y -= 20
        self.goto(self.xcor(), y)
