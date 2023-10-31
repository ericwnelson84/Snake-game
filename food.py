from turtle import Turtle
import random

# Below is an example of Class inheritence. unlike the snake class, this will directly inherit the Turtle class as
# the super class. so both the Food class and Turtle class need to be initialized as can be seen below. no methods
# and attributes can be called directly from the Turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

