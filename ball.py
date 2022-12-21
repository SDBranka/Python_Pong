import turtle as t


SPEED_UP_BY = 7


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("circle")
        # rate of change in x
        self.dx = 10
        # rate of change in y
        self.dy = 10
        # # make ball 10x10 pixels 
        # self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        # this will be used to determine which direction
            # the ball is served to after respawning
        self.serve_direction = 1


    def move(self):
        self.goto(self.xcor() + self.dx,
                    self.ycor() + self.dy
        )


    def speed_up(self):
        if self.dx > 0:
            self.dx += SPEED_UP_BY
        else:
            self.dx -= SPEED_UP_BY
        if self.dy > 0:
            self.dy += SPEED_UP_BY
        else:
            self.dy -= SPEED_UP_BY


    def ball_respawn(self):
        self.goto(0, 0)
        self.serve_direction *= -1
        self.dx = 10
        self.dy = 10
        if self.serve_direction < 0:
            self.dx *= -1