# Day 82 – Text to Morse Code Converter

## Overview

This is a Python project that converts plain text into Morse code. The program takes user input, processes each character, and translates it into the corresponding Morse code representation using a predefined dictionary. The project focuses on building a functional text-to-Morse converter using Python dictionaries, loops, and nested data structures. It is designed to handle uppercase and lowercase letters, numbers, special characters, and spaces, converting them all into their Morse code equivalents.


## How It Works 

### Morse Code Dictionary/`morse_code.py`

* **Alphabet Category**:  Contains mappings for all 26 English letters (A-Z) to their Morse code equivalents (e.g., A = ".-", B = "-...").

* **Numbers Category**: Contains mappings for numbers 0-9 (e.g., 1 = ".----", 5 = ".....").

* **Special Characters Category**: Contains mappings for punctuation and symbols like period, comma, question mark, exclamation mark, and others.

* **White Space Mapping**: Defines how spaces between words are represented in Morse code (using a forward slash /).

### Main Program Flow/`main.py`

* **Getting User Input**: The program first asks the user to enter the plain text they want to convert.

* **Converting Text to Morse Code**: The `converting_text_to_morse()` function processes the input by converting it to uppercase, then iterating through each character. For each character, it searches through the nested dictionary to find its matching Morse code, adds it to the result string with appropriate spacing, and returns the completed Morse code.

* **Displaying the Result**: The program prints both the original entered text and the converted Morse code.

* **Asking to Continue or Quit**: After displaying the result, the program asks the user if they want to exit. If they enter 'n', the program asks for new input and continues converting. If they enter 'y', the program stops. If an invalid input is entered, the program prompts the user to enter a valid response.

* **Handling Empty Input**:  If the user enters nothing (empty string), the program skips the conversion and directly asks if they want to quit, preventing any errors.


## Highlights

* **Nested Dictionaries**: Revised how to organise data using dictionaries containing multiple categories of mappings.
* **List Comprehension**: Revised using list comprehension to extract and store dictionary keys efficiently.
* **Nested Loops**: Used multiple for loops to iterate through nested dictionary structures.
* **Function-Based Design**: Organized the program into small, focused functions for better readability and reusability.
* **Space Handling**: Correctly translated spaces between words into Morse code's space representation (/).
* **Modular Code**: Separated data storage from conversion logic and user interaction for maintainability.
