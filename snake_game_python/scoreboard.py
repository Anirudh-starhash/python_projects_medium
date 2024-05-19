from turtle import Turtle
ALIGN="center"
FONT=("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("D:\\nitw\\academics\\demo_py\\snake_game_python\\score.txt") as f:
            self.high_score=int(f.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
       
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}",align=ALIGN,font=FONT)
        
    def game_over(self,reason):
        self.goto(0,260)
        self.score=0
        self.update_scoreboard()
        self.goto(0,0)
        self.write(f"Game Over {reason}",align=ALIGN, font=FONT)
        
    def increase_score(self):
        self.score+=1
        if self.score> self.high_score:
            self.high_score=self.score
        
        with open("D:\\nitw\\academics\\demo_py\\snake_game_python\\score.txt","w") as f:
            f.write(str(self.high_score))
            
        self.update_scoreboard()
        