from turtle import Turtle
# constants defines below in all CAPS
MOVE_DISTANCE = 20
STARTING_POS = [(20, 0), (0, 0), (20, 0)]
class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]


# method creation
    def create(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        #below is a work around to remove old snake from the screen. this was from angela
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create()
        self.head = self.segments[0]


# position is a turtle method. turtle.pos(). Return the turtle’s current location (x,y) (as a Vec2D vector).
    # adds another segment in the position of the last square
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
         self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)



