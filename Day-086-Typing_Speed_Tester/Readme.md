# Day 86 – Typing Speed Tester Desktop App

## Project Overview

This is a fully functional Typing Speed Tester Desktop App built with Python's Tkinter library. The application allows users to test their typing speed and accuracy by typing out randomly selected paragraphs in three difficulty levels - Easy, Normal, and Hard. The app features a clean, dark-themed interface with real-time character highlighting (white for correct, red for incorrect), a countdown timer with three options (60, 120, or 180 seconds), and a Words Per Minute (WPM) calculation at the end of the test. Users can reset the test anytime, switch between difficulty modes, and track their typing performance.

The code is designed with a modular structure where the typing paragraphs, user interface, and main application logic are separated into different files for better organization and maintainability.

## What I Have Learned

* **Tkinter GUI Development**: Revised how to build a desktop application using Python's Tkinter library. Created windows, buttons, labels, text widgets, radiobuttons, and handled user events like key presses.

* **Object-Oriented Programming (OOP)**: Built the entire application using classes. The UserInterface class inherits from Tk and contains all the methods for creating UI elements, handling user interactions, and managing application state.

* **Text Widget and Character Formatting**: Learned how to use Tkinter's Text widget to display paragraphs and apply formatting to individual characters using tags. Used tag_config() and tag_add() to change character colors in real-time.
    
* **Event Binding**: Used Tkinter's event binding system to capture key press events using <KeyRelease>. This allowed the application to detect when a user typed a character and trigger the comparison logic.
 
* **Real-Time Character Comparison**: Implemented logic to compare user input with the displayed paragraph character by character. Correct characters turn white, incorrect characters turn red, and untyped characters remain the default text color.

* **Timer Implementation**:  Used Tkinter's after() method to create a countdown timer. The timer starts when the user begins typing and stops when the time runs out or the user completes the test.

* **Words Per Minute (WPM)**: Calculated WPM by counting the number of correctly typed words, dividing by the total minutes, and rounding to the nearest whole number.
 
* **Difficulty Levels**: Implemented three difficulty levels with different paragraph lengths and complexity - Easy (simple sentences), Normal (moderate complexity), and Hard (complex, technical content).

* **Reset Functionality**: Built a reset feature that clears the user's input, removes all character formatting, resets the timer, and loads a new random paragraph.
 
* **Radiobutton Widgets**: Used Radiobuttons for difficulty selection (Easy, Normal, Hard) and timer selection (60, 120, 180 seconds) with shared variables.

* **Global Variables for State Management**: Used global variables to track character position, timer start status, and stop timer flag across multiple methods.

* **Data Separation**: Stored all typing paragraphs in a separate typing_data.py file to keep the main application code clean and organized.


## How It Works

### main.py

* **Imports and Setup**: The file imports the UserInterface class from userinterface.py, creates an instance, calls the methods to set up the UI, binds the key release event, and starts the main application loop.

### userinterface.py

* **Global Variables**: Defines window dimensions, text colors, background color, button color, and global tracking variables for character position (fg_color_index), timer start status (START_TIMER), and stop timer flag (STOP_TIMER_COUNTDOWN).
 
* **__init__ Method**: Sets up the main application window with a centered position on the screen, fixed size, and title. Initializes the font for displaying paragraphs and sets the default difficulty mode to "easy_mode".

* **add_typing_test_screen()**: Loads and displays the background image on the screen using a Label widget with a PhotoImage.

* **all_widget_button()**: Creates all the control widgets including the reset button (⭮), difficulty radiobuttons (Easy, Normal, Hard), timer radiobuttons (60, 120, 180), a hidden text entry field for capturing user input, and labels for displaying timer and WPM.

* **display_typing_text()**: Creates a Text widget to display the typing paragraph. It randomly selects a paragraph from the current difficulty level and inserts it into the text widget with default text color.

* **check_retrieved_text()**: This is the core logic method triggered on every key release. It gets the user's input from the hidden text entry field and the displayed paragraph text. When the user starts typing, it initiates the timer. It handles backspace to allow correction by reverting the character color to default. It compares each character position and changes the color using tags - white for correct, red for incorrect. It increments the character position counter with each keystroke.

* **get_foreground_at_index()**: Returns the current text color of a specific character in the display text. This is used when the user presses backspace to restore the character to its default color.

* **timer_countdown()**: Implements the countdown timer using after() recursion. It displays the remaining seconds in the timer label. When the timer reaches zero, it disables the input field, calculates and displays the WPM.

* **calculate_word_per_minute()**: Calculates the WPM by splitting the user's input into words and counting the number of correctly typed words. It divides the word count by the total minutes (seconds / 60) and rounds to the nearest integer.

* **reset_typing()**: Resets all variables to their initial state. Clears the user's input, removes all character tags from the display text, resets the character position counter, stops the timer, hides the WPM label, and loads a new random paragraph.

* **handle_typing_mode()**: Called when the user selects a difficulty level. It resets the typing test, clears the display text, and loads a new random paragraph from the selected difficulty mode.

### typing_data.py

* **typing_paragraph_dict**: Contains a dictionary with three difficulty levels - "easy_mode", "normal_mode", and "hard_mode". Each mode contains a list of 5 long paragraphs with varying complexity. Easy mode has simple sentences, normal mode has moderate complexity, and hard mode has complex, technical content.


## Project Highlights

* **Tkinter GUI**: Built a complete desktop application with a dark-themed professional interface.
* **Real-Time Typing Feedback**: Characters turn white when correct and red when incorrect instantly as the user types.
* **Backspace Support**: Users can correct mistakes by pressing backspace, which reverts the character color to default.
* **Three Difficulty Levels**: Easy, Normal, and Hard paragraphs to suit different skill levels.
* **Adjustable Timer**: Users can choose between 60, 120, or 180 seconds for the typing test.
* **Words Per Minute Calculation**: Automatically calculates and displays WPM when the timer ends.
* **Reset Functionality**: Users can reset the test anytime to start fresh with a new random paragraph
* **Random Paragraph Selection**: Each difficulty level has 5 different paragraphs, randomly selected each time
* **Clean Code Structure**: Separated data (paragraphs), UI, and main logic into different files for maintainability.
* **Keyboard Focus**: The application captures all keystrokes without requiring the user to click on an input field.