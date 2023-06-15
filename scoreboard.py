from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.update_score()

    def detectscore(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.clear()  # Clear previous score
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER ", align="center", font=FONT)
