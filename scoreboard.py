from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')

class Scoreboard(Turtle):
    """
    Class with scoreboard logic
    """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.goto(0, 280)
        self.pencolor("white")
        self.show_score()

    def read_highscore(self):
        """
        Reads the highscore from the data.txt file
        """
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def show_score(self):
        """
        Shows the score of the game in the screen
        """
        self.clear()
        self.read_highscore()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """
        Checks if the score of the game is higher than high score, if it is, it updates it
        """
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.show_score()

    def increase_score(self):
        """
        Increases the score by one
        """
        self.score += 1
        self.show_score()