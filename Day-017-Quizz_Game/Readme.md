# Day 17 - Quiz Game Project

## Project Overview
In this project, I have applied everything I learned in Day 17.
I worked with classes, attributes, class constructors (__init__ functions), and methods inside classes.
I learned how to create objects from classes and how to manage data using lists and dictionaries.
Using all these concepts, I built a fully working Quiz Game where users can answer a series of True/False questions, get feedback on each answer, and receive their final score at the end.  

## What I Have Learned
- How to create and use classes in Python
- How to create attributes and initialize them using the `__init__` method
- How to write methods (functions) inside a class
- How to create multiple objects and store them in a list
- How to pass objects to another class and work with them
- How to structure and organize code cleanly using multiple files

## How It Works
- The **question_data** list contains a collection of True/False questions, each stored as a dictionary with text and the correct answer. This data serves as the foundation of the quiz by providing all the questions that the user will be asked.
- Each dictionary from **question_data** is used to create a **Question** object containing the question text and correct answer. This organizes the data in a structured format.
- All **Question** objects are stored into a list  **question_bank**. This makes it easier to pass all the questions together to another class that will handle the quiz operations.
- A **QuizBrain** object is created by passing the **question_bank** list to it. This object is responsible for managing the flow of the quiz, keeping track of which question the user is on, and checking if there are more questions left or not.
- The **QuizBrain** object has a class **next_question** which uses a while loop to run the quiz until there are no more questions left. Inside the loop, it asks questions one by one, takes user input (True/False), checks if the input is correct, updates the user's score accordingly, and moves to the next question.
- Once all the questions have been asked, the final score is displayed to the user, showing how many questions they answered correctly out of the total. This provides a clear summary of the user's performance at the end of the quiz.


## Project Highlights
- Used object-oriented programming (OOP) concepts like classes and objects, attribute, methods.
- Organized code into multiple files (`question_model.py`, `data.py`, `quiz_brain.py`, and the main file).
- Created and managed a list of objects.



---


