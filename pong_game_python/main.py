from turtle import Turtle,Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

my_screen=Screen()
my_screen.title("Pong Game")
my_screen.bgcolor("black")
my_screen.setup(width=800,height=600)

my_screen.tracer(0)

paddle1=Paddle((350,0))
paddle2=Paddle((-350,0))
scoreboard2=Scoreboard((150,230),2)
scoreboard1=Scoreboard((-150,230),1)
ball=Ball()


scoreboard2.draw_line()
my_screen.listen()
my_screen.onkey(paddle1.up,"Up")
my_screen.onkey(paddle1.down,"Down")
my_screen.onkey(paddle2.up,"w")
my_screen.onkey(paddle2.down,"s")


is_gam_on=True
while is_gam_on:
    my_screen.update()
    time.sleep(ball.move_speed)
    ball.move()
 
    # collisions with wall
    
    if ball.head.ycor()>280 or ball.head.ycor()<-280:
        ball.bounce_Y()
        
    if ball.head.distance(paddle1)<50 and ball.head.xcor()>320 or ball.head.distance(paddle2)<50 and ball.head.xcor()<-320:
        ball.bounce_X()
        
    if ball.head.xcor()>380:
        ball.head.goto(0,0)
        scoreboard1.increase_score((-150,230),1)
        
    elif ball.head.xcor()<-380:
        ball.head.goto(0,0)
        scoreboard2.increase_score((150,230),2)
        
    if scoreboard2.score==5:
        is_gam_on=False
        scoreboard2.clear()
        scoreboard1.clear()
        scoreboard1.remove_line()
        scoreboard2.update_winner(2)
        
    elif scoreboard1.score==5:
        is_gam_on=False
        scoreboard1.clear()
        scoreboard2.clear()
        scoreboard1.remove_line()
        scoreboard1.update_winner(1)
        
    
        
        


my_screen.exitonclick()