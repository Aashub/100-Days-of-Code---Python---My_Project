# DAy-20 Snake Game 
##  Project Overview

This project is a traditional snake game where the snake increases in size whenever it eats food. After being eaten, the food relocates to a random position on the screen. The game ends when the snake collides with the wall or its own body. A score is displayed and updated with each food consumed.
The project uses Python's `turtle` graphics module and applies Object-Oriented Programming (OOP) concepts like classes, inheritance. It also includes global variables, list slicing, and basic game logic.

---

##  What I Have Learned

* Creating and managing multiple objects using **Object-Oriented Programming**
* Using **inheritance** to use Turtle class features in a Snake  
* Applying list slicing to manage parts of the snake, such as checking for self-collision by comparing the head segment with the rest of the body (snake[1:]), allows for efficient and readable code that helps maintain the game logic.
* Using **event listeners** to bind keys for controlling the snake
* Using global variables and loops effectively
* Structuring a program using multiple files and modules

---

## How It Works

* **main.py**: This is the main driver file that initializes the game environment and controls the core gameplay loop.

  * Functions like `screen.setup()`, `screen.bgcolor()`, and others are used to configure the game window, including its dimensions, background color, and Game title.
  * Keyboard key bindings are set using event listeners to allow the player to control the snake’s direction.
  * The game loop continuously updates the screen and checks for key events like collisions with the wall, the snake’s own body, or food.

* **snake.py**:

  * The `snake_object()` method initializes the snake by creating multiple turtle segments and storing them in a list.
  * The `snake_body()` method arranges these segments on the screen to form a linear snake.
  * The `snake_movement()` method ensures that all snake segments follow the head's direction, updating their positions frame by frame.
  * Directional methods such as `up()`, `down()`, `left()`, and `right()` allow the snake to change direction in response to keyboard inputs.
  * The `extend()` method adds a new segment to the snake’s body each time it eats food, increasing the snake's length.

* **food.py**:

  * This file defines a `Food` class that inherits from the `Turtle` class and customizes the appearance of the food item (e.g., shape, color).
  * The `refresh()` method randomly relocates the food on the screen when the snake eats it, providing new targets for the snake.

* **score.py**:

  * This module handles all scoring functionalities by using turtle text to display the score.
  * The `score_card()` method updates the score on the screen every time food is eaten.
  * The `game_over()` method displays a "Game Over" message at the center of the screen when the player loses the game.

## Project Highlights

* Uses **OOP principles**: Everything is structured using classes for better code management
* Applies **inheritance**: `Food` and `Score` classes inherit from `Turtle` to use Turtle class property and also uses their own method.
* Includes **list slicing**: To check if the head of the snake collides with any part of its body
* Real-time **collision detection** with wall and snake body
* Dynamic **score update** and Game Over screen
* User can **control the snake** using arrow keys


