from turtle import Turtle
from paddle import Paddle
from turtle import Screen
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Best Pong Game")
screen.tracer(0)

line = Turtle()
line.hideturtle()
line.color("white")
line.goto(0, 250)
line.setheading(270)
line.forward(550)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
score_1 = ScoreBoard(150, 220)
score_2 = ScoreBoard(-150, 220)

screen.listen()
screen.onkeypress(paddle_1.up, "Up")
screen.onkeypress(paddle_1.down, "Down")
screen.onkeypress(paddle_2.up, "w")
screen.onkeypress(paddle_2.down, "s")

game_is_on = True
turn = 1

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 \
            or ball.distance(paddle_2) < 50 and ball.xcor() < 320:
        print("boi")
        ball.bounce_x()

    if ball.xcor() > 420:
        score_2.clear()
        ball.reset()
        score_2.increase_score()
        #game_is_on = False

    if ball.xcor() < -420:
        score_1.clear()
        ball.reset()
        score_1.increase_score()


screen.exitonclick()
