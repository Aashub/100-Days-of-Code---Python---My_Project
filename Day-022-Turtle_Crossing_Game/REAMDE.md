
# Day 22 - Turtle Crossing Game 

## Project Overview

This is a **Turtle Crossing Game** where the turtle tries to cross a busy road filled with moving cars. If the turtle gets hit by a car, the game ends and displays "Game Over". If the turtle successfully crosses the road, the level increases, and the cars move faster, making the game more challenging. This project was created using everything I've learned so far, including Object-Oriented Programming (OOP), Inheritance, The `time` module, Turtle graphics, Global variables, Keyboard input handling with `onkey()`

--- 

## What I Learned
This project is all about to implement everyting which I have learned so far, not about to learn new thing and implement in this project.

* Learned how to break the game into multiple classes (Turtle, Cars, Level) to keep the code organized, reusable, and easier to debug or expand.
  
* Used inheritance by extending the turtle.Turtle class to create customized turtles with specific properties and methods.
  
* Implemented keyboard event listeners with screen.onkey() to control turtle movement based on real-time user input.
  
* Controlled game flow and pacing using a game loop combined with time.sleep() to update the screen and simulate smooth motion.
  
* Used Turtle graphics to display text on the screen, such as the current level and "Game Over" message, and dynamically updated it.
  
* Managed the game state with global variables and instance attributes, tracking things like speed, score, and turtle position.
  
* Dynamically created and moved multiple car objects with different colors and positions, making each game level unpredictable and fun.

---

## How It Works

* **main.py:** Handles the core game logic including setting up the screen, initializing all game objects like (turtle, cars, level), listening for keypresses so the turtle can move, and running the main game loop that manages collisions with cars, car movement, and level progression each time turtle crosses the road..

* **TURTLE.py:** This module Defines a custom turtle class using inheritance from turtle.Turtle, initializes the player turtle with specific properties, and provides movement methods to control its upward and downward motion.

* **cars.py:** Manages car behavior through a Cars class that create cars, stores them in a list, and moves car objects across the screen in random location and increases cars speeds as the level progresses.

* **level.py:** Contains the Level class responsible for displaying and updating the current level on the screen and showing the game over message when the turtle collides with a car.

---

## Project Highlights

*  **Object-Oriented Design**: Used OOP to organize code into multiple classes (`Turtle`, `Cars`, and `Level`).
*  **Inheritance**: Inherited from `turtle.Turtle` to create custom behavior for turtle and level class.
*  **Global Variables & Game State**: Managed speed, score, and car creation logic efficiently.



