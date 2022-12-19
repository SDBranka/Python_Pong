import turtle as t


class Net(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.setposition(0, -290)
        self.left(90)
        self.draw_net()


    def draw_net(self):
        for i in range(61):
            if self.isdown():
                self.penup()
            else:
                self.pendown()
            self.forward(10)


