Snake Game
==========

This project is a simple implementation of the classic Snake Game using Python and the Pygame library. In this game, the player controls a snake that grows in length by eating fruits while avoiding collisions with the walls and itself. The objective is to score as many points as possible by collecting fruits.

Features
--------

- Classic Snake gameplay mechanics
- Score tracking that increases with each fruit eaten
- Simple controls for movement (up, down, left, right)
- Game over conditions when colliding with walls or the snake's own body
- Responsive and fluid game experience

Requirements
------------

- Python 3.x
- Pygame library

Installation
------------

To install the required dependencies, run the following command: ``pip install pygame``.


Gameplay
--------

- Use the arrow keys to control the direction of the snake:
  - **Up Arrow**: Move Up
  - **Down Arrow**: Move Down
  - **Left Arrow**: Move Left
  - **Right Arrow**: Move Right

- The snake will grow longer each time it eats a fruit, and the game ends if the snake collides with the walls or itself.
- Your score will be displayed at the top of the game window.

Unit Tests
----------

This project includes unit tests to verify the game logic. You can run the tests using the following command:
 ``python -m unittest test_snake_game.py``.



