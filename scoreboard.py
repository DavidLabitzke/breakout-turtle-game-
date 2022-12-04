from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates player's score and life count"""
        self.clear()
        self.goto(-225, 250)
        self.write(f"Score: {self.score}", align="Center", font=("Courier", 40, "bold"))
