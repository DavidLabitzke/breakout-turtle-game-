from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5)
        self.penup()
        self.starting_position = (0, -290)
        self.goto(self.starting_position)
        self.showturtle()
        self.released = False
        self.x_move = 5
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Moves ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def release(self):
        """Releases ball from the paddle at the start of the game. Also determines if it should
        start moving to the right or to the left"""
        if not self.released:
            if self.xcor() < 0:
                self.x_move *= -1
            self.released = True

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_ball(self, coordinates):
        self.hideturtle()
        self.goto(coordinates)
        self.showturtle()
        self.x_move = 5
        self.y_move = 10
        self.released = False
