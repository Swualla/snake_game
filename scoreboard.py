from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.draw_scoreboard()

    def draw_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.clear()
        self.draw_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


