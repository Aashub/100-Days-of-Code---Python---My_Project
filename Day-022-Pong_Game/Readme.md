# Day 22 - Pong Game 

##  Project Overview

This is a traditional Pong Game project which I have built using Python’s turtle graphics module. The game involves two paddles and a ball — players control the paddles to prevent the ball from passing by. If a player misses the ball, the opponent scores a point. The first player to reach 5 points wins the match.
While creating this project I have applied OOP concepts, how to use inheritance, implemented game loops, keyboard event handling, collision detection, and real-time screen updates using Turtle.Screen().

---

##  What I Learned

* Implementing Object-Oriented Programming (OOP) to break down a complete game into reusable components so that they can be used and modified easily.
  
* Creating multiple classes like Paddle, Ball, Score, and Boarder using inheritance from the Turtle class to create game-specific behaviors.
  
* Handling real-time user inputs by listening to keystrokes using onkey() and listen() methods to move paddles instantly.
  
* Writing clean and modular code by separating logic into individual files (main.py, ball.py, paddle.py, score.py, boarder.py).

---

##  How It Works

* main.py: Manages the entire game setup including screen creation, object instantiation (paddles, ball, scoreboard, border), key bindings for paddle movement, the main game loop, collision detection logic, ball speed control, and checking the win condition.

* paddle.py: Defines the Paddle class using inheriting from Turtle module. It creates left and right paddles and includes methods to move paddles up and down with boundary checks.

* ball.py: Contains the Ball class which handles ball movement, detects wall and paddle collisions and as per that changes direction accordingly, increases ball speed after ball hits the paddle each time, and adds random angle variation to make gameplay less predictable.

* score.py: Implements the Score class to track and display left and right player scores, update the scoreboard dynamically, and display the winner message when a player reaches 5 points.
  
* boarder.py: Draws the center dividing line and top boundary of the game screen to visually separate both sides of the Pong arena.

---

##  Project Highlights

*  **Object-Oriented Design**: Organized code using OOP with clear responsibilities.
*  **Inheritance**: Used inheritance from the `Turtle` class to extend functionality in custom classes.
*  **Dynamic Game Speed**: Ball speed increases after every paddle hit to increase difficulty gradually.
*  **Real-Time Input Handling**: Implemented key bindings (`onkey()`) for paddle control.
