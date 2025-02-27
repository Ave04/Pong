import turtle as t
import time
import random as r
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# # improve: CHANGE BALL SPEED EACH TIME BALL HITS PADDLE -> RESET SPEED WHEN POINT IS DONE
# Create game screen
screen = t.Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Pong")


screen.tracer(0)

# create scoreboard
scoreboard = Scoreboard()

# create player 1's paddle
paddle1 = Paddle()
paddle1.goto(-450, 0)

# create player 2's paddle
paddle2 = Paddle()
paddle2.goto(450, 0)

# create ball
ball = Ball()
ball.goto(0, 0)

# listen for user input to move paddle up and down
screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

# loop to keep game running
gameon = True
while gameon:
    screen.update()
    time.sleep(0.02)
    ball.move()

    # collision of paddles with top and bottom walls
    # if paddle1.ycor() < -280 or paddle1.ycor() > 280:

    # collison detection
    if (ball.xcor() > 440  and ball.xcor() < 470) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
        ball.dx *= -1

    if (ball.xcor() < -440 and ball.xcor() > -470) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
        ball.dx *= -1

    # upper and lower wall collisions
    if ball.ycor() > 280:
        ball.oncollisiontop()

    if ball.ycor() < -280:
        ball.oncollisionbottom()

    # win conditions for each player
    if ball.xcor() > 480:
        ball.recentre()
        scoreboard.updatescore1()
    elif ball.xcor() < -480:
        ball.recentre()
        scoreboard.updatescore2()

    # end game if either player scores 10
    if scoreboard.checkgameover():
        gameon = False



screen.exitonclick()