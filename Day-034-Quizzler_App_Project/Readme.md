# Day 34 - Quizzler App

## Project Overview

In this project, I have expanded my Day 17 learning by building a fully functional Quiz Game with a Graphical User Interface (GUI) using Tkinter. This project combines object-oriented programming concepts with API integration and GUI development. The quiz fetches real-time True/False questions from the Open Trivia Database API, displays them on a graphical interface, provides them instant feedback as per user answer is correct or wrong, and keeps track of the user’s score until the quiz ends. while building this project i have learned about how to unescaping html entities python typing: type hint and Arrows ->.

## What I Have Learned

* **HTML module**: I have learned about the html module and used it to convert HTML-escaped characters received from the Open Trivia Database API into normal, readable text before displaying them in the Tkinter interface.

* **Python Typing: Type Hint**: I have learned about the type hint feature of python where it allows us to specify the data type of variable so that later when we add value to that variable it will give him hint that please enter correct data type.

* ***Python Arrow (->) in Type Hint***: I have learned about the python arrow feature as well so we can use -> arrow in function to specify which data type of output this function should return.

* ***Revised about OOP concepts***: I have revised about OOP concept while building this project.

## How It Works 

* **`data.py`**: The quiz questions are fetched dynamically from the Open Trivia Database API using the `requests module`. Each time the app runs, new True/False questions are loaded which we can use in the app. The received API data is stored in question_data, where each question is represented as a dictionary containing the question text and the correct answer. The received API data is stored in question_data, where each question is represented as a dictionary containing the question text and the correct answer.

* **`main.py`**: In main file Each question dictionary from question_data  `Question` object created using `Question` class that stores the question text and answer in a structured way. All Question objects are stored inside a list called `question_bank`. This allows all questions and answers to be passed together to another class.

* **`quizzbrain.py`**: A QuizzBrain is created using the question bank list, this class controls the quiz logic such as tracking the current question number, checking that if question are still available or not, after each answer give user the next question and also checking the answer is correct or not.

* **`ui.py`**: The QuizInterface class handles the GUI using Tkinter. It displays the question on the screen, shows True and False buttons, updates the score, and provides visual feedback by changing colors for correct and incorrect answers. When a user clicks a button, the answer is checked using the check_answer() method from QuizzBrain, and feedback is shown before moving to the next question. Once all questions are completed, the app displays an end message and disables the buttons.

## Project Highlights 

* Revised about the OOP concepts

* Updated older quiz game project to GUI based Quiz application

* learned about Python Typing: Type Hint and Python Arrow (->) in Type Hint and to use them.