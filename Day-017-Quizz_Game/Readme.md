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
- How to pass class to another class and work with them
- How to structure and organize code cleanly using multiple files

## How It Works
- The **question_data** list contains a collection of True/False questions, each stored as a dictionary with text and the correct answer. This data serves as the foundation of the quiz by providing all the questions that the user will be asked.
- Each dictionary from **question_data** is used to create a **Question** object containing the question text and correct answer. This organizes the data in a structured format.
- All **Question** **Answer** attributes are stored into a list  **question_bank** in a form of classes. This makes it easier to pass all the questions & answer together to another class that will handle the quiz operations.
- A **quiz** object is created by using Quizbrain class and by passing the **question_bank** list to it. This object is responsible for managing the flow of the quiz, keeping track of which question the user is on, and checking if there are more questions left or not.
- The **quiz** object has a method **next_question()** which will ask the user next question each time he will guess correct or wrong answer. **stil_has_question()** will check that is their any other question left or not, **check_answer()** method will check that the user entered answer is correct or not and as per that give us an output & increase score.
- Once all the questions have been asked, the final score is displayed to the user, showing how many questions they answered correctly out of the total. This provides a clear summary of the user's performance at the end of the quiz.


## Project Highlights
- Used object-oriented programming (OOP) concepts like classes and objects, attribute, methods.
- Organized code into multiple files (`question_model.py`, `data.py`, `quiz_brain.py`, and the main file).
- Created and managed a list of classes.



---


