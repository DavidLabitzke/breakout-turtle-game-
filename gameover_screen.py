from turtle import Turtle


class GameOverScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.game_over_message = "Game Over!"
        self.color("white")
        self.write(self.game_over_message, align="center", font=("Courier", 40, "normal"))
