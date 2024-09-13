"""
Snake Game

Author: Alan
Date: September 7th 2024
Update: September 11th 2024

This script generates the famous snake game.
The user starts with a snake with a length of three squares.
The user can get fruit, which increases the score and the length of the snake.
The user loses if they collide with a wall or with the snake's body.
"""

from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
from time import sleep

# Generates a new screen
screen = Screen()
screen.setup(width=600, height=600) # This line setups the screen size
screen.bgcolor("black") # Changes the background color to black
screen.title("Snake") # Changes the window's title
screen.tracer(0) # Freezes the screen animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True

# Enables key input listening for snake directional commands using the arrow keys
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# Simple loop to keep the game running
while game_is_on:

    # Updates the screen to give the impression the snake is moving
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food using the snake's distance
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        food.refresh()
        snake.reset()
        scoreboard.reset()

    # Defect collision with wall
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            food.refresh()
            snake.reset()
            scoreboard.reset()

screen.exitonclick()
