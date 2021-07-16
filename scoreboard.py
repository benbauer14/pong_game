from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.color("white")
        self.write("0         Score          0",False, "center", ("Arial",24,"normal"))
        self.left = 0
        self.right = 0

    def score(self, who):
        if(who == "left"):
            self.clear()
            self.left += 1
            self.write(f"{self.left}         Score          {self.right}",False, "center", ("Arial",24,"normal"))
        if(who == "right"):
            self.clear()
            self.right += 1
            self.write(f"{self.left}         Score          {self.right}",False, "center", ("Arial",24,"normal"))
