from turtle import Turtle
ALIGN="center"
FONT=("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self,position,pos):
        super().__init__()
        self.color("white")
        self.score=0
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard(pos)
        
    def update_scoreboard(self,pos):
        self.write(f"Player {pos} : {self.score}",align=ALIGN,font=FONT)
        
    def increase_score(self,position,pos):
        self.goto(position)
        self.score+=1
        self.clear()
        self.update_scoreboard(pos)
        self.draw_line()
        
    def draw_line(self):
        for i in range(-230,230):
            self.goto(0,i)
            self.write("|",align=ALIGN,font=FONT)
            self.hideturtle()
            self.color("blue")
        
        self.color("white")
        
    def update_winner(self,win):
        self.goto(0,0)
        self.hideturtle()
        self.color("white")
        self.write(f"Game Over Winner is Player {win}",align=ALIGN,font=FONT)
        
    def remove_line(self):
        for i in range(-230,230):
            self.goto(0,i)
            self.write("|",align=ALIGN,font=FONT)
            self.hideturtle()
            self.color("black")
        