from turtle import Turtle


class Paddle:

    def __init__(self):
        self.right_paddle = Turtle()
        self.left_paddle = Turtle()

    def create_rpaddle(self):
        self.right_paddle.shape("square")
        self.right_paddle.color("white")
        self.right_paddle.penup()
        self.right_paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.right_paddle.goto(350, 0)

    def create_lpaddle(self):
        self.left_paddle.shape("square")
        self.left_paddle.color("white")
        self.left_paddle.penup()
        self.left_paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.left_paddle.goto(-350, 0)

    def rpaddle_up(self):
        new_y = self.right_paddle.ycor() + 20
        self.right_paddle.goto(self.right_paddle.xcor(), new_y)

    def rpaddle_down(self):
        new_y = self.right_paddle.ycor() - 20
        self.right_paddle.goto(self.right_paddle.xcor(), new_y)

    def lpaddle_up(self):
        new_y = self.left_paddle.ycor() + 20
        self.left_paddle.goto(self.left_paddle.xcor(), new_y)

    def lpaddle_down(self):
        new_y = self.left_paddle.ycor() - 20
        self.left_paddle.goto(self.left_paddle.xcor(), new_y)


