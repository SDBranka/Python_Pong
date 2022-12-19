import turtle as t

screen = t.Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
# screen.tracer(0)

paddle = t.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(-280, 0)




screen.exitonclick()