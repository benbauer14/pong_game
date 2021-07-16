from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def moveUp(self):
        if(self.ycor() <= 200):
            self.goto(self.xcor(), self.ycor() + 20)
    
    def moveDown(self):
        if(self.ycor() >= -200):
            self.goto(self.xcor(), self.ycor() - 20)