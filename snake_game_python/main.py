# tips 

# create a snake body
# move the snake
# keyboard controls
# detect collisions with food
# create a scoreboard
# detect collision with wall
# detect collision with tail


from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")


is_game_on=True

while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    # collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # collision with wall
    
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        is_game_on=False
        reason="due to collision with wall"
        scoreboard.game_over(reason)
    
    #collison with tail
    
    for x in snake.turtle_list[1:]:
        if snake.head.distance(x)<10:
            is_game_on=False
            reason="due to collision with tail"
            scoreboard.game_over(reason)
   
   
      
        
    
        





my_screen.exitonclick()


