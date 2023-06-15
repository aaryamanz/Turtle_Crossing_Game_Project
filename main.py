import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# creating Objects
turtle1 = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle1.move, "Up")


game_is_on = True
count = 0

while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()
    cars.randomgeneration()
    cars.movecar()

    # for detection of collision
    for car in cars.all_cars:
        if turtle1.distance(car) < 20:
            game_is_on = False
            score.gameover()

    # for detection of level complete
    if turtle1.ycor() > 300:
        score.detectscore()
        turtle1.reset_turtle()
        cars.levelup()

screen.exitonclick()
