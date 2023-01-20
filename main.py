from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

scoreboard = ScoreBoard()
game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 290 or ball.ycor() < - 290:
        ball.bounce_y()

    if (ball.distance(paddle_r) < 50 and ball.xcor() > 330) or (ball.distance(paddle_l) < 50 and ball.xcor() > -330):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < - 380:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()
