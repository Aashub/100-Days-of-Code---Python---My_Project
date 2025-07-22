# Day 28 - Pomodoro Timer

---

## Project Overview

This project is a **Pomodoro timer** project that helps manage work and break intervals, When the user clicks the **Start** button, a 25-minute work session begins. After each session, the timer automatically switches to a **5-minute short break**. Every 8th rep (4 work sessions), it gives a **15-minute long break** instead. After each work session, a **✔ tick mark** is displayed to visually track progress The timer can also be **reset anytime** with the Reset button whenever the user click on it . In order to built this project I have learned about how to control and loop time using Python and Tkinter, and how to manage GUI elements and states with timers. how to use global variables and dynamic typing.

---

## What I Have Learned

* **`global`**: I used global variables like `reps` and `timer` to track session counts and control the timer across multiple functions.

* **Dynamic Typing**: I understood how Python allows variables like `second` to be redefined (e.g., from an int to a formatted string).

* **`Tk()`**: How to Initializes the main GUI window.

* **`Label()`**: How to Displays text such as the timer title, tick marks, etc on the screen.

* **`Canvas()`**: How to use canvas module to  show an image (like the tomato) on the GUI and how to add text over it.

* **`PhotoImage()`**: How to use photoimage which helps in adding and loading images inside the GUI.

* **`Button()`**: Creates clickable buttons like Start and Reset, with assigned `command=` actions.

* **`grid()`**: Places each element (labels, buttons, canvas) into its exact position in a grid layout where we want them to placed.

* **`after()`**: Delays function execution, allowing me to count down in real time (every second).

* **`itemconfig()`**: Dynamically updates the text and other details inside the canvas (like the timer).

* **`math.floor()`**: I have used to round down values (like converting seconds to minutes).

---

## How It Works 

* **GUI Setup**: First we have set a window by using a  `Tk()` class, and configured its padding and background color. Elements like labels, buttons, and canvas are placed using `grid()`.

* **Start Timer**: When the user clicks **Start** button, the `start_timer()` function runs. It increases the `reps` count and determines whether it’s time for:
     * A 25-minute work session
     * A 5-minute short break
     * Or a 15-minute long break

* **Countdown**: than The `countdown()` function runs every second using `after()` until it reaches zero once it  hits zero `start_timer()` functions is triggered again for the next session and this goes on. Time is shown in minutes and seconds, formatted neatly. Once it hits zero, 

* **Visual Feedback**: After each work session, a ✔ mark is added using a loop that tracks how much work reps as of now has been completed .

* **Reset Timer** Whenever user Clicks **Reset** button to cancels the timer using `after_cancel()`, resets the label, tick marks, and session count to start fresh.

---

## Project Highlights

* GUI-based Pomodoro timer using Tkinter.
* Learned how to use global variable
* **Dynamic Typing**: I understood how Python allows variables like `second` to be redefined (e.g., from an int to a formatted string).

---

