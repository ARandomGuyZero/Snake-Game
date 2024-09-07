"""
Snake Game

Author: Alan
Date: September 7th 2024

This script generates famous snake game.
"""

from turtle import Screen
from snake import Snake
import time

# Generates a new screen
screen = Screen()
screen.setup(width=600, height=600) # This line setups the screen size
screen.bgcolor("black") # Changes the background color to black
screen.title("Snake") # Changes the window's title
screen.tracer(0) # Freezes the screen animation

snake = Snake()

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
    time.sleep(0.1)

    snake.move()

screen.exitonclick()