from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=3)
        self.penup()
        self.starting_position = (0, -300)
        x_cor = self.starting_position[0]
        self.xcor = x_cor
        self.goto(self.starting_position)
        self.showturtle()

    def move_left(self, ball_object):
        """Move paddle to the left. If the ball has not been released, it will follow the paddle."""
        if self.xcor <= -330:
            pass
        else:
            self.xcor -= 20
            if not ball_object.released:
                ball_object.goto(self.xcor, -290)
            self.goto(self.xcor, -300)

    def move_right(self, ball_object):
        """Move paddle to the right. If the ball has not been released, it will follow the paddle"""
        if self.xcor >= 330:
            pass
        else:
            self.xcor += 20
            if not ball_object.released:
                ball_object.goto(self.xcor, -290)
            self.goto(self.xcor, -300)
