import turtle
from turtle import Turtle
from random import choice

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0
colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
          (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
          (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
          (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
          (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    turtle.colormode(255)

    def create_snake(self):
        for position in starting_position:
            self.create_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def create_segment(self, position):
        new_segment = Turtle("circle")
        new_segment.color(choice(colors))
        new_segment.penup()
        new_segment.shapesize(stretch_len=0.8, stretch_wid=0.8)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.create_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
