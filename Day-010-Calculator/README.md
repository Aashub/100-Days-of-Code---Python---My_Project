# Day 10 - Calculator Project

## Project Overview
This Calculator project is a console-based tool that allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division. The calculator can be used continuously with the current result or restarted for a fresh calculation. The main goal of this project was to strengthen my understanding of functions with output, loops, dictionaries, and input handling in Python.

## How It Works
- The program begins by displaying an ASCII art logo for the calculator (imported from the `art` module).
- It prompts the user to input a number, then shows the available operations: `+`, `-`, `*`, and `/`.
- After choosing an operator and entering the next number, the chosen arithmetic operation is performed.
- The result is displayed, and the user is asked whether they want to continue with the current result (`y`), start a new calculation (`n`), or exit the program by giving the prompt (`exit`).
- The calculator continues running until the user explicitly exits.

## Code Highlights
- Used **nested functions** to organize logic cleanly: a main function to start the calculator and an inner function to restart it with new or existing values.
- Applied **dictionaries** to map operators (`+`, `-`, `*`, `/`) to their corresponding function implementations.
- Included **input validation** within a `while` loop to make sure the user provides proper input for the next steps.
- Made use of **recursion** to either restart the calculator or continue with the latest result without breaking the flow.
- Demonstrated how **functions** can take inputs (parameters like `num1`, `num2`) and return outputs (results of calculations) to make the logic reusable and modular.

This project helped me get more comfortable using functions to organize logic and keep user interaction smooth. It also showed how dictionaries can make it easy to trigger specific actions based on user input.

