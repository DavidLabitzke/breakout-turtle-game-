from turtle import Turtle


class Brick(Turtle):

    def __init__(self, color):
        super().__init__()
        self.brick_color = color

    def create_bricks(self, y_coordinate, master_list):
        """Creates 2 rows of bricks of the specified color"""
        x_position = -350
        y_position = y_coordinate
        self.hideturtle()
        screen_filled = False
        second_row_created = False
        while not screen_filled:
            new_brick = Turtle("square")
            new_brick.hideturtle()
            new_brick.penup()
            new_brick.shapesize(stretch_wid=0.5, stretch_len=2.5)
            new_brick.color(self.brick_color)
            new_brick.goto(x_position, y_position)
            new_brick.showturtle()
            x_position += 50
            master_list.append(new_brick)
            if x_position == 400:
                if second_row_created:
                    screen_filled = True
                else:
                    x_position = -350
                    y_position += 15
                    second_row_created = True
