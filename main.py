from turtle import Screen, Turtle
from paddle import Paddle
import ball

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

paddle_right = Paddle()
paddle_left = Paddle()
paddle_left.goto(-350, 0)
paddle_right.goto(350,0)



screen.listen()
screen.onkey(paddle_right.moveUp, "Up")
screen.onkey(paddle_right.moveDown, "Down")
screen.onkey(paddle_left.moveUp, "w")
screen.onkey(paddle_left.moveDown, "s")


screen.exitonclick()