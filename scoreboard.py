from turtle import Turtle

with open("data.txt", mode="r") as file:
    high_score = int(file.read())


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.score = 0
        self.high_score = high_score
        self.hideturtle()
        self.pencolor("white")
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score} ", align="center",
                   font=("Arial", 15, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score} ", align="center",
                   font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score} ", align="center",
                   font=("Arial", 15, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.pencolor("red")
        self.write(arg=f"GAME OVER ", align="center", font=("Arial", 15, "normal"))
