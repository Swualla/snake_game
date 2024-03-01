from turtle import Turtle
MOVE_DISTANCE = 20
START_POSITION = (0, 0)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.start_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]

    def start_snake(self):
        x_cord = START_POSITION[0]
        for i in range(0, 3):
            self.add_snake(START_POSITION)
            x_cord -= 20

    def add_snake(self, position):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.snake_body.append(new_snake)

    def extend(self):
        self.add_snake(self.tail.position())


    def move(self):
        for snake_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_num - 1].xcor()
            new_y = self.snake_body[snake_num - 1].ycor()
            self.snake_body[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
