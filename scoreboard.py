from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Score={self.score}", False, ALIGN, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGN, FONT)

    def increment_score(self):
        self.score+=1
        self.clear()
        self.update()