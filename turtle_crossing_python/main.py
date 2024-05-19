from turtle import Turtle,Screen
from player import Player
from carManager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

my_screen=Screen()
my_screen.bgcolor("white")
my_screen.setup(width=600,height=600)
my_screen.title("Turtle Crossing Game")

my_screen.tracer(0)
player=Player()
scoreboard=Scoreboard()
carManager=CarManager()
is_game_on=True

my_screen.listen()
my_screen.onkey(player.move,"Up")

while is_game_on:
    time.sleep(0.1)
    my_screen.update()
    
    if player.check_finish():
        scoreboard.increase_score()
        player.reset_position()
        carManager.level_up()
        
    carManager.create_car()
    carManager.move()
    
    for car in carManager.all_cars:
        if car.distance(player)<20:
            is_game_on=False
            my_screen.bgcolor("black")
            scoreboard.result()
            break
        
    

my_screen.exitonclick()