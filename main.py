from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong Game")

score = Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 270)
score.write("Score", align="center", font=("Courier", 20, "normal"))

# print(screen.window_width())
# print(screen.window_height())

# create the net
# net = Paddle((0, 0))
# net.shape("square")
# net.color("white")
# net.shapesize(stretch_len=0.1, stretch_wid=30)

# create the paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))

# create the ball
ball = Ball()

# create scoreboard
scoreboard = Scoreboard()

# create the paddle move
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # print("collision")
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        print("game over")
        ball.reset_position()
        scoreboard.increase_r_score()


    # Detect right paddle misses
    if ball.xcor() < -380:
        print("game over")
        ball.reset_position()
        scoreboard.increase_l_score()


screen.exitonclick()