from scoreboard import Scoreboard
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle()
paddle_left = Paddle()
scoreboard= Scoreboard()
paddle_left.goto(-350, 0)
paddle_right.goto(350,0)

ball = Ball()
ball.goto(0,0)
ball.setheading(45)



screen.listen()
screen.onkey(paddle_right.moveUp, "Up")
screen.onkey(paddle_right.moveDown, "Down")
screen.onkey(paddle_left.moveUp, "w")
screen.onkey(paddle_left.moveDown, "s")

game_over = False
while game_over == False:
    screen.update()
    ball.move()
    time.sleep(0.05)
    if(ball.ycor() > 200 > 0):
        ball.bouncetop()
    elif(ball.ycor() < -200):
        ball.bouncetop()
    if(ball.distance(paddle_right) <= 20):
        ball.bouncepaddle()
    if(ball.distance(paddle_left) <= 20):
        ball.bouncepaddle()
    if(ball.xcor() >= 400):
        scoreboard.score("left")
        ball.bouncepaddle()
        ball.goto(0,0)
    if(ball.xcor() <= -400):
        scoreboard.score("right")
        ball.bouncepaddle()
        ball.goto(0,0)
    if(scoreboard.left >=10):
        game_over = True
        scoreboard.goto(0,0)
        scoreboard.clear()
        scoreboard.write(f"Left wins!",False, "center", ("Arial",24,"normal"))
    if(scoreboard.right >=10):
        game_over = True
        scoreboard.goto(0,0)
        scoreboard.clear()
        scoreboard.write(f"Right wins!",False, "center", ("Arial",24,"normal"))        

screen.exitonclick()