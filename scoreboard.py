import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}              {self.r_score}",
                    align = "center",
                    font = ("Arial", 20, "normal")
                    )

    def game_over(self, winner):
        # self.clear()
        self.goto(0, 0)
        self.write(f"Game Over\n{winner} Wins!!!", align = "center",
                    font = ("Arial", 30, "normal"))