from scoreboard import Scoreboard
from bricks import Brick
from paddle import Paddle
from ball import Ball
from life_counter import LifeCounter
from gameover_screen import GameOverScreen
from loading_screen import LoadingScreen
import turtle
import time

# Set screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Breakout Game")
screen.setup(width=760, height=650)
screen.tracer(False)

loading = LoadingScreen()
time.sleep(5)
loading.reset()

# Constants
GAME_SPEED = 0.1
ORANGE_FIRST_CONTACT = False
RED_FIRST_CONTACT = False

# Points Dictionary
points = {
    "yellow": 1,
    "green": 3,
    "orange": 5,
    "red": 7
}

# Create all the bricks
all_bricks = []
yellow_bricks = Brick("yellow")
yellow_bricks.create_bricks(120, all_bricks)
green_bricks = Brick("green")
green_bricks.create_bricks(150, all_bricks)
orange_bricks = Brick("orange")
orange_bricks.create_bricks(180, all_bricks)
red_bricks = Brick("red")
red_bricks.create_bricks(210, all_bricks)

# Create other aspects of the game
scoreboard = Scoreboard()
life_tracker = LifeCounter()
life_tracker.write_white_line()
paddle = Paddle()
ball = Ball()

# Code for the keys
screen.listen()
screen.onkey(lambda ball_object=ball: paddle.move_left(ball_object=ball_object), "Left")
screen.onkey(lambda ball_object=ball: paddle.move_right(ball_object=ball_object), "Right")
screen.onkey(ball.release, "Up")

game_is_on = True
while game_is_on:
    bricks_gone = 0
    time.sleep(GAME_SPEED)
    screen.update()
    if ball.released:
        ball.move()

    if ball.xcor() == 370 or ball.xcor() == -370:
        ball.bounce_x()

    if ball.ycor() == 240:
        ball.bounce_y()

    if ball.distance(paddle) < 30 and ball.ycor() < -280 and ball.y_move < 0:
        ball.bounce_y()

    for brick in all_bricks:
        if ball.distance(brick) < 30:
            scoreboard.score += points[brick.color()[0]]
            scoreboard.update_scoreboard()
            brick.reset()
            all_bricks.remove(brick)
            ball.bounce_y()
            if bricks_gone == 4 or bricks_gone == 12:
                GAME_SPEED *= 0.5

            if not ORANGE_FIRST_CONTACT:
                if brick.color()[0] == "orange":
                    GAME_SPEED *= 0.5
                    ORANGE_FIRST_CONTACT = True

            if not RED_FIRST_CONTACT:
                if brick.color()[0] == "red":
                    GAME_SPEED *= 0.5
                    RED_FIRST_CONTACT = True

    if ball.ycor() < -320:
        life_tracker.lives -= 1
        life_tracker.update_lives()
        ball.reset_ball((paddle.xcor, -290))

    if life_tracker.lives == 0 or len(all_bricks) == 0:
        paddle.reset()
        ball.reset()
        time.sleep(1)
        game_over_message = GameOverScreen()
        game_is_on = False

# Mechanism for exiting the screen
screen.exitonclick()
