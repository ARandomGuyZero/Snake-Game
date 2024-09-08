from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')

class Scoreboard(Turtle):
    """
    Class with scoreboard logic
    """
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.hideturtle()
        self.goto(0, 280)
        self.pencolor("white")
        self.show_score()

    def show_score(self):
        """
        Shows the score of the game in the screen
        """
        self.clear()
        self.write(f"Score: {self.total_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Shows once the game is over
        """
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increases the score by one
        """
        self.total_score += 1
        self.show_score()