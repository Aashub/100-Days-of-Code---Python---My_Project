# Day 21 - Pong Game 

##  Project Overview

This is a traditional **Pong Game** project which I have built using Python's `turtle` graphics module. The game involves two paddles and a ball — players control the paddles to prevent the ball from passing by. If a player misses the ball, the opponent scores a point. The first player to reach **10 points** wins the match.
while creating this project I have applied OOPs, how to use inheritance, python time module to reduce the loop speed time, keyboard event hanling, game loops and screen updated Turtle.Screen()

---

##  What I Learned

* Implementing **OOP principles** to break down a game into reusable components so we can use them again and again.
  
* Creating multiple **classes** like `Paddle`, `Ball`, and `Score` using **inheritance** from the `Turtle` class so we can modify and create our own class to do the specific functionality according of game.
  
* Using the time.sleep() method to dynamically control the game's speed, allowing smoother and adjustable difficulty.
  
* Handling real-time user inputs by listening to keystrokes using onkey() and listen() methods to move paddles instantly.
  
* Writing clean, modular, and maintainable code by separating logic into individual classes and keeping functions focused.

---

##  How It Works

* main.py: Manages the entire game setup including screen creation, object instantiation (paddles, ball, score), key bindings by which we can control our paddles, the main game loop for movement and collision detection, and checking the win condition.

* paddle.py: Defines the Paddle class inheriting from Turtle, sets visual properties, and includes methods to move the paddle up and down in response to user input.

* ball.py: Contains the Ball class that handles the ball's movement, detects wall and paddle collisions so the ball can change direction, adjusts speed, and resets position after each point is scored.

* score.py: Implements the Score class to track and display player scores, update the scoreboard, and show the winning message when a player reaches 10 points.

---

## ✨ Project Highlights

*  **Object-Oriented Design**: Organized code using OOP with clear responsibilities.
*  **Inheritance**: Used inheritance from the `Turtle` class to extend functionality in custom classes.
*  **Dynamic Game Speed**: Adjusted ball speed using `time.sleep()` to make the game progressively faster.
*  **Real-Time Input Handling**: Implemented key bindings (`onkey()`) for paddle control.
