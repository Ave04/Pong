import turtle as t
ALIGNMENT = 'center'
FONT = ('Futura', 24, 'normal')
CLEARSCORE = 10

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.ht()
        self.color("white")
        self.speed("fastest")
        self.score1 = 0
        self.score2 = 0
        self.write(f"{self.score1} : {self.score2}", False, ALIGNMENT, FONT)

    def updatescore1(self):
        self.score1 += 1
        self.clear()
        self.write(f"{self.score1} : {self.score2}", False, ALIGNMENT, FONT)

    def updatescore2(self):
        self.score2 += 1
        self.clear()
        self.write(f"{self.score1} : {self.score2}", False, ALIGNMENT, FONT)

    def checkgameover(self):
        if self.score1 == CLEARSCORE and self.score2 < CLEARSCORE:
            self.clear()
            self.goto(0, 0)
            self.write("GAME OVER, PLAYER 1 WINS", False, ALIGNMENT, FONT)
            return True
        elif self.score2 == CLEARSCORE and self.score1 < CLEARSCORE:
            self.clear()
            self.goto(0, 0)
            self.write("GAME OVER, PLAYER 2 WINS", False, ALIGNMENT, FONT)
            return True