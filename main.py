from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# creating snake with initial length of 3 squares. default square size is 20x20
# xpos = -40
# segments = []
# for _ in range(3):
#     new_segment = Turtle("square")
#     new_segment.penup()
#     new_segment.color("white")
#     new_segment.goto(xpos, 0)
#     xpos += 20
#     segments.append(new_segment)
snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# turning the screen.tracer(0) method off then running screen.update() method determines when the image gets updated
# so the image doesn't jump around because each turtle object is moving 1 at a time as the code asks it to

game_is_on = True
while game_is_on:
    screen.update()
    # time.sleep() delays the script for specified interval in seconds
    time.sleep(.2)
    # code below will cause the segments to inch forward and follow the head. Thats why teh range starts at
    # the back segment
    #     for seg_num in range(len(segments) - 1, 0, -1):
    #         new_x = segments[seg_num-1].xcor()
    #         new_y = segments[seg_num - 1].ycor()
    #         segments[seg_num].goto(new_x, new_y)
    #     segments[0].forward(20)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        score_board.update()
        snake.extend()
        food.refresh()
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # detect collision with tail not including the head because the game would never start. Using list slicing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()



screen.exitonclick()
