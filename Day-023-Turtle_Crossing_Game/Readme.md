
# Day 23 - Turtle Crossing Game 

## Project Overview

This is a **Turtle Crossing Game** where the turtle tries to cross a busy road filled with moving cars. If the turtle gets hit by a car, the game ends and displays "Game Over". If the turtle successfully crosses the road, the level increases, and the cars move faster, making the game more challenging. This project was created using everything I've learned so far, including Object-Oriented Programming (OOP), Inheritance, The `time` module, Turtle graphics, Global variables, Keyboard input handling with `onkey()`

--- 

## What I Learned
This project is all about to implement everyting which I have learned so far, not about to learn new thing and implement in this project.

* Learned how to break the game into multiple classes (ScoreBoard, Player, CarManager) to keep the code organized, reusable, and easier to understand.
  
* Used inheritance in Scoreboard & Player class to create customized turtles with specific attributes and methods.
  
* Implemented keyboard event listeners with screen.onkey() to control turtle movement based on real-time user input.
  
* Controlled game flow and pacing using a game loop combined with time.sleep() to update the screen and simulate smooth motion.
  
* Used Turtle graphics to display text on the screen, such as the current level and "Game Over" message.
  
* Managed the game state with global variables to increase speed of cars after each level increase.

---

## How It Works

* **main.py:** This file controls the complete game flow. It sets up the game screen, creates all main objects like the turtle player, cars, and scoreboard, and handles keyboard input so the turtle can move up and down. It also runs the main game loop where cars are created randomly, cars keep moving, level increases when the turtle crosses the finish line, and the game ends if the turtle collides with any car.

* **player.py:** This module defines the Player class using inheritance from turtle.Turtle. It sets the turtle shape, color, starting position, and direction. It also contains movement methods that allow the turtle to move forward and backward and a reset method that sends the turtle back to the starting position after crossing the finish line.

* **car_manager.py:** This module defines & manages all car-related behavior. The CarManager class creates cars at random positions with random colors and stores them in a list. It moves all cars across the screen and increases their speed each time the player levels up. It also checks for collision between the turtle and any car and returns true if a collision occurs. which will help in to stop the game.

* **scoreboard.py:** This module handles the game level display. It draws a horizontal finish line, shows the current level on the screen, updates the level whenever the turtle successfully crosses the road, and displays the “GAME OVER” message when the turtle collides with a car.

---

## Project Highlights

*  **Object-Oriented Design**: Used OOP to organize code into multiple classes (`Player`, `CarManager`, and `Scoreboard`).
*  **Inheritance**: Inherited from `turtle.Turtle` to create custom behavior for Scoreboard and Player class.




