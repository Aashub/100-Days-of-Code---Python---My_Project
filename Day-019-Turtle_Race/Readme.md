  # Day 19 - Turtle Race Game 

## Project Overview
In this project, I have created a Turtle Race Game using the turtle graphics module in Python.
The game begins by prompting the user to place a bet on which colored turtle will win the race. Once a valid input is given, multiple turtles start racing across the screen at random speeds. The first turtle to cross the finish line is declared the winner, and the program informs the user whether their bet was correct or not.
in day 19 of learning main focus was on understanding higher-order functions, working with event listeners, managing object states and instances, and exploring the Turtle module documentation to identify and implement the right methods effectively.


---

## What I Have Learned

- How to create and manage multiple turtle objects (instances).
- How to use `event listeners` and `screen.textinput()` to get user input.
- How to define and use **higher-order functions**.
- How to use documentation to find suitable methods and understand their purpose.
- How to use `for` loops effectively to handle multiple turtle objects.

---

## How It Works

- **Color List Initialization**: A list of turtle colors is defined to assign unique colors to each turtle.

- **`create_turtle()` Function**: Creates multiple turtle object(instances), assigns each one a color, and stores them in a list.

- **`starting_line()` Function**: Positions each turtle at the starting line with evenly spaced vertical placement using `goto()` and `penup()` methods.

- **`draw_finish_line()` Function**: A vertical line is drawn at the right end of the screen using a hidden turtle object to represent the finish line.

- **User Input**: Uses `screen.textinput()` to get a color input from the user, which is stored as a bet. which is later used in a program that selected color turtle won the race or not. 

- **`move_turtle()` Function**: Moves each turtle forward by a random amount on every loop iteration. If a turtle crosses the finish line, the race ends and the winner is displayed.

- **Main Loop**: Runs the race only if the user's input matches one of the defined turtle colors.

---

## Project Highlights

- Used **tuples and loops** to manage turtle objects efficiently.
- Demonstrated use of **object states** and **methods**.

