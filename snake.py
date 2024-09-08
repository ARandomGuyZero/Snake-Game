from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    Class with the snake logic
    """
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Creates a new snake of three squares
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        """
        Adds a new segment to the snake
        """
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        """
        Creates a new segment
        """
        new_segment = Turtle("square")  # New square-shaped segment
        new_segment.color("white")  # Change color to white
        new_segment.penup()  # Disable drawing
        new_segment.goto(position)  # This snake goes to new position
        self.segments.append(new_segment)

    def move(self):
        """
        Moves the snake by moving each segment from the end of the snake's tail to the next segment's coordinates.
        Then moves the snake forwards.
        :return:
        """
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x_coordinates = self.segments[segment_number - 1].xcor()
            new_y_coordinates = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x_coordinates, new_y_coordinates)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Changes the snake's heading up if the snake is not heading down
        """
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Changes the snake's heading down if the snake is not heading up
        """
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Changes the snake's heading left if the snake is not heading right
        """
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Changes the snake's heading right if the snake is not heading left
        """
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
