  # Day 19 - Turtle Racing Game 

## Project Overview
In this project, I have created a Turtle Race Game using the turtle graphics module in Python.
The game begins by prompting the user to place a bet on which colored turtle will win the race. Once a valid input is given, multiple turtles start racing across the screen at random speeds. The first turtle to cross the finish line is declared the winner, and the program informs the user whether their bet was correct or not.
in day 19 of learning main focus was on understanding higher-order functions, working with event listeners, managing object states and instances, and exploring the Turtle module documentation to identify and implement the right methods effectively.


---

## What I Have Learned

- How to create and manage multiple turtle objects (instances).
- objects (instances): object instances are those thing where each object are similar to each other but they behave differently to each other like some turtle moving at different pace and their color this is called instances
- How to use `event listeners` and `screen.textinput()` to get user input.
- How to define and use **higher-order functions**.
- How to use documentation to find suitable methods and understand their purpose.

---

## How It Works

- **Screen Setup:** A Screen object is created with a width of 500 and height of 400. and then their is a pop-up input box asks the user to place a bet by entering the color of the turtle they think will win.

- **Color List & Constants:** A list of turtle colors is defined and Constant values are used for the starting X-axis and Y-axis positions to place turtles on the screen.

- **Turtle Creation & Positioning:** A for loop creates one turtle object for each color in the list, and than Turtles are placed at the same X-position but different Y-positions by using goto() method to form a vertical lineup, All turtles object than stored in a list for easy movement control

- **Finish Line Creation:** A separate hidden turtle draws a vertical finish line on the right side of the screen. A fixed X-coordinate finish_line_coord variable is created to check when a turtle crosses the finish line.

- **Winner Display text:** Another hidden turtle is created to display the race result (win or lose message) once a turtle reaches the finish line.

- **Game Start Condition:** The race starts only if the user enters some input for their bet.

- **Race Loop:** While the race is active each turtle moves forward by a random distance between 0 and 10 distance pace, After every move, the turtle’s X-coordinate is checked that they crossed the finish line coordinate or not, If a turtle crosses the finish line coordinate The race stops The turtle’s color is identified, A message is displayed showing whether the user won or lost based on their bet

---


