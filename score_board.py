from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")


class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.position(x, y)
        self.color("white")
        self.write(f"0", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.score = 0

    def position(self, x, y):
        self.goto(x, y)

    def score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)








