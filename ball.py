from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.width(20)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
    
    def bouncetop(self):
        self.y_move *= -1

    def bouncepaddle(self):
        self.x_move *= -1