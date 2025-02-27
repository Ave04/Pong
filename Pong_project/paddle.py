import turtle as t

# each paddle will be three squares big
# create positions for initial segments
segmentpos = [(-400, -20), (-400, 0), (-400, 20)]
UP = 90
DOWN = 270
movedistance = 20

class Paddle(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1, 5, 1)
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(UP)

    def up(self):
        # if self.heading() != DOWN:
        #     self.setheading(UP)
        ycordup = self.ycor()
        ycordup += movedistance
        self.sety(ycordup)

    def down(self):
        # if self.heading() != UP:
        #     self.setheading(DOWN)
        ycorddown = self.ycor()
        ycorddown -= movedistance
        self.sety(ycorddown)
