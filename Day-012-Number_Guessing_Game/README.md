# Day 12 - Number Guessing Game

## Project Overview
This Number Guessing Game is a console-based program that was designed to apply concepts I learned in Day 12 of the #100DaysOfCode challenge. It focuses on understanding local and global scope, using constants, modifying global variables, and building reusable functions to keep the code clean, organized, and easy to update.

## What I Learned
- Local Scope: Variables that are only accessible within a function.
- Global Scope: Variables that can be accessed anywhere in the code.
- Block Scope: Variables that exist within a block of code (e.g., inside loops or conditionals).
- Constants and Global Variables: How to use constants and how to modify global variables from within functions.
- Modular Code: Breaking down the program into smaller, reusable functions for better organization and maintainability.

## How It Works
- The program begins by welcoming the user and asking them to choose a difficulty level: easy, medium, or hard.
- Based on the difficulty level, the player is given a specific number of attempts to guess a randomly generated number between 1 and 100.
- After each guess, the game tells the user whether the guess was too high, too low, or correct.
- If the guess is correct, the user wins and is prompted to play again.
- If all attempts are used up, the user loses and can choose to restart the game.

## Code Highlights
- **Difficulty Levels:** The game allows users to select between easy (10 attempts), medium (7 attempts), and hard (5 attempts).
- **Reusable Functions:** The main logic is split into smaller functions such as `check_correct_guess()`, `select_difficulty_level()`, and `game_restart()`.
- **Error Handling:** Input validation is used to ensure the user enters valid difficulty levels and options.
- **User Experience:** The game includes a restart option and gives feedback on each guess.

---

