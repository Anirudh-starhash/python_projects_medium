from turtle import Turtle

FONT=("Courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,240)
        self.color("black")
        self.score=0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"{self.score}",font=FONT,align="center")
        
    def result(self):
        self.goto(0,0)
        self.clear()
        self.color("white")
        self.write(f"Game Over your score is {self.score} ",align="center",font=FONT)
        