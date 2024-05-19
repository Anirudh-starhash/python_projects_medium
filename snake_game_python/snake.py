from turtle import Turtle
Starting_position=[(0,0),(-20,0),(-40,0)]
d=20

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.turtle_list=[]
        self.create_snake()
        self.head=self.turtle_list[0]
        
    def create_snake(self):
        for position in Starting_position:
            self.add_segment(position)
           
            
    def add_segment(self,position):
        t=Turtle("square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.turtle_list.append(t)
        self.head=self.turtle_list[0]
        
    def extend(self):
        self.add_segment(self.turtle_list[-1].position())
    
    def move(self):
        for i in range(len(self.turtle_list)-1,0,-1):
          new_x = self.turtle_list[i-1].xcor()
          new_y=self.turtle_list[i-1].ycor()
          self.turtle_list[i].goto(new_x,new_y)
        
        self.head.forward(d)
        
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)