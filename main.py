from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
TIME_SLEEP = 0.2

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(TIME_SLEEP)

    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.new_food()
        scoreboard.increase_score()
        if scoreboard.score % 5 == 0:
            TIME_SLEEP *= 0.9

    if snake.head.xcor() > 290 or snake.head.ycor() > 290 \
            or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        # is_on = False
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 3:

            # is_on = False
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
