# Day 12 - Number Guessing Game

## Project Overview
This Number Guessing Game is a console-based program that was designed to apply concepts I learned in Day 12 of the #100DaysOfCode challenge. It focuses on understanding local and global scope, using constants, modifying global variables, and building reusable functions to keep the code clean, organized, and easy to update.

## What I Learned
- Local Scope: Variables (or functions) declared inside functions have local scope (also called function scope). They are only used by other code within the same block of code.
- Global Scope: Variables or functions declared at the top level (unindented) code have global scope. It is accessible anywhere in the code inside the local scope as well outside the local scope.
- Block Scope: Python is a bit different from other programming languages in that it does not have block scope. which means that variables created nested in blocks of code like for loops, if statements, while loops etc. don't get local scope. but their are  function scope if they are within a function.
- How to modify global variable: You can force the code in local scope which is function and by using a keyword global and it will allow us to to modify that variable and than that variable will be modified outside the local scope as well 
- Global Constant: We can define global constants in our code for easy access. Their job is meant to be "set and forget" so we can use their values but never required any need to modify them later. we can define global variable as LL_CAPS with a underscore in between.

## How It Works
- The program begins by welcoming the user and asking them to choose a difficulty level: easy, medium, or hard.
- Based on the difficulty level, the player is given a specific number of attempts to guess a randomly generated number between 1 and 100.
- After each guess, the game tells the user whether the guess was too high, too low, or correct.
- If the guess is correct, the user is being asked that does he want to play the again or not.
- If all attempts are used up, the user loses and can choose to restart the game or exit.

## Code Highlights
- **Difficulty Levels:** The game allows users to select between easy (10 attempts), medium (7 attempts), and hard (5 attempts).
- **Reusable Functions:** The main game logic is organized into functions like `start_number_guessing_game()` and `guessing_the_number()` for better structure and readability.
- **Error Handling:** The program checks for valid difficulty selection and restart options to prevent incorrect inputs..
- **User Experience:** The game provides feedback on each guess, displays remaining attempts, and includes a restart option..

---

