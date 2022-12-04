from turtle import Turtle


class LifeCounter(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.update_lives()

    def write_white_line(self):
        self.goto(-400, 250)
        self.pendown()
        self.forward(800)
        self.penup()

    def update_lives(self):
        self.clear()
        self.goto(225, 250)
        self.write(f"Lives: {self.lives}", align="Center", font=("Courier", 40, "bold"))
        self.write_white_line()
