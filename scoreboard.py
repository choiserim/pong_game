from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.clear()
        self.write(f"{self.r_score}", align="left", font=("Courier", 30, "normal"))
        self.goto(100, 200)
        self.write(f"{self.l_score}", align="right", font=("Courier", 30, "normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()
