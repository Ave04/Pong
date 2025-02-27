import turtle as t
import random as r


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(0.5, 0.5, 1)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.dx = 7
        self.dy = 7

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    # call when ball hits paddle or wall
    def oncollisiontop(self):
        self.sety(280)
        self.dy *= -1

    def oncollisionbottom(self):
        self.sety(-280)
        self.dy *= -1

    def recentre(self):
        self.goto(0, 0)
        self.dx *= -1



