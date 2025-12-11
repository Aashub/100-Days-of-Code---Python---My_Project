# Day 10 - Calculator Project

## Project Overview
This Calculator project is a console-based tool that allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division. The calculator can be used continuously with the current result or restarted for a fresh calculation. The main goal of this project was to strengthen my understanding of functions with output, loops, dictionaries, and input handling in Python.

## What I have Learned
- Function with Output: A function that takes some input, do the processing, and gives back a result using the return statement which we can store in variable to reuse. It helps make the code reusable and lets us store the output for further calculations.
  - Function with multiple return value: A function that returns more than one value at the same time, which we can use for further processing This is useful when we want to send back multiple pieces of information from a single function.
  - Docstring: A short description written inside triple quotes (""" """) at the beginning of a function. It explains what the function does, making the code easier to understand and maintain.
  - Recursion: When a function calls itself to repeat a process. In this project, I have used recursion to restart the calculator with fresh values without ending the program.

## How It Works
- The program begins by displaying an ASCII art logo for the calculator (imported from the `art` module).
  - It prompts the user to input a number, then shows the available operations: `+`, `-`, `*`, and `/`.
  - After choosing an operator and entering the next number, the chosen arithmetic operation is performed.
  - The result is displayed, and the user is asked whether they want to continue with the current result (`y`), start a new calculation (`n`), or exit the program by giving the prompt (`exit`).
  - The calculator continues running until the user explicitly exits.

## Code Highlights
- Used **nested functions** to organize operations logicly: a main function to start the calculator and an inner function do the calculation operations restart it with new or existing values.
  - Applied **dictionaries** to map operators (`+`, `-`, `*`, `/`) to their corresponding function implementations.
  - Included **input validation** within a `while` loop to make sure the user provides proper input for the next steps.
  - Made use of **recursion** to restart the calculator for new values.
  - Demonstrated how **functions** can take inputs (parameters like `num1`, `num2`) and return outputs (results of calculations) to make the logic reusable and modular.

This project helped me get more comfortable using functions to organize logic and keep user interaction smooth. It also showed how dictionaries can make it easy to trigger specific actions based on user input.

