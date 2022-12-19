import time
import turtle as t
from turtle import Screen
from paddle import Paddle
from net import Net
from scoreboard import Scoreboard
from ball import Ball


END_SCORE = 10


# create screen
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
# set tracer to 0 to enable using the update
# method and turn off animation
screen.tracer(0)

# draw net
net = Net()
# create scoreboard
scoreboard = Scoreboard()
# create and move a paddle
l_paddle = Paddle(x = -360, y = 0)
# create another paddle
r_paddle = Paddle(x = 360, y = 0)
# create ball and make it move
ball = Ball()

# create screen listeners
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="e")
screen.onkey(fun=l_paddle.down, key="c")


# main game cycle
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    # move the ball
    ball.move()

    # detect collision with wall and bounce
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.dy *= -1

    # detect collision with paddle and bounce 
    if (ball.distance(l_paddle) < 72 and ball.xcor() < -333) \
        or (ball.distance(r_paddle) < 72 and ball.xcor() > 333):
        # print("Ball hit paddle")
        ball.dx *= -1
        ball.speed_up()

    # detect when paddle misses
    if ball.xcor() > 399:
        # print("Right paddle missed")
        # keep score
        scoreboard.l_score += 1
        # reset ball
        ball.ball_respawn()
    elif ball.xcor() < -399:
        # print("Left paddle missed")
        # keep score
        scoreboard.r_score += 1
        # reset ball
        ball.ball_respawn()
    scoreboard.update_scoreboard()

    # detect when game over
    if scoreboard.l_score == END_SCORE:
        # print("Left player wins!")
        scoreboard.game_over(winner = "Left")
        game_on = False
    elif scoreboard.r_score == END_SCORE:
        # print("Right player wins!")
        scoreboard.game_over(winner = "Right")
        game_on = False


screen.exitonclick()