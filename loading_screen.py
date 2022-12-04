from turtle import Turtle


class LoadingScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.loading_message = "Loading Breakout"
        self.color("white")
        self.write(self.loading_message, align="center", font=("Courier", 40, "normal"))
