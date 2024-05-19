from turtle import Turtle
initial=50
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.head=self.create_ball()
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1
        
    def create_ball(self):
        self.shape("circle")
        self.shapesize(stretch_len=0.8,stretch_wid=0.8)
        self.penup()
        self.goto(0,0)
        self.color("white")
        return self
        
        
    def move(self):
        new_x=self.head.xcor()+self.xmove
        new_y=self.head.ycor()+self.ymove
        self.head.goto(new_x,new_y)
        
    def bounce_Y(self):
        self.head.ymove*=-1
    def bounce_X(self):
        self.head.xmove*=-1
        self.move_speed*=0.9
        
    