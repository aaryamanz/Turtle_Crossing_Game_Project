import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def randomgeneration(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)


    def movecar(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


    def levelup(self):
        self.carspeed += 1




