from turtle import Turtle
starting=(350,0)
class Paddle(Turtle):
    def __init__(self,starting):
        super().__init__()
        self.head=self.create_paddle(starting)
      
        
    def create_paddle(self,position):
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(position)
        self.color("white")
        return self
        
    def up(self):
        if self.head.ycor()>230:
            pass
        else:
            new_y=self.head.ycor()+20
            self.head.goto(self.head.xcor(),new_y)
        
    def down(self):
        if self.head.ycor()<-220:
            pass
        else:
            new_y=self.head.ycor()-20
            self.head.goto(self.head.xcor(),new_y)