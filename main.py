from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
tm = Turtle()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    if ball.distance(r_paddle) <50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 420:
        score.l_point()
        ball.retry()

    if ball.xcor() < -420:
        score.r_point()
        ball.retry()


    if score.r_score > 1:
        game_is_on = False
        score.game_over("Right")

    if score.l_score > 1:
        game_is_on = False
        score.game_over("Left")
screen.exitonclick()