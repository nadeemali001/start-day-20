from turtle import Turtle

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
        self.write(f"Score={self.score}", False, "center", ("Arial", 24, "normal"))

    def increment_score(self):
        self.score+=1
        self.clear()
        self.update()