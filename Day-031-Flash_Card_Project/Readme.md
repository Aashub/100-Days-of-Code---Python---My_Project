# Day 31 – Flash Card GUI App

## Project Overview

This project is a Flash Card GUI application built using Python and Tkinter to help users learn Telugu words with their English meanings. The app displays Telugu words on a flash card and automatically flips the card after a few seconds to show the English translation. Users can mark words as known or unknown, making the learning process interactive and efficient.
If a word is marked as known by right click button, it is removed from the learning list and new words_to_learn list created and know words does not appear again. The app also  handles missing files and continues smoothly without crashing is words_to_learn list don't exist. this is the capstone project where I have implemented all the things i learned so far and whatever things required to build this project.

## What I Have Learned

* Revised how to use try, except, and finally blocks to handle missing CSV files safely.

* Revised about how to Work with CSV files using the pandas library for reading, writing, and updating data.

* learned about how to convert CSV data into list of dictionaries using to_dict(orient="records").

## How It Works

* **File Handling & Data Loading**: When program runs first app tries to load `words_to_learn.csv`. If the file does not exist, it falls back to the original `telugu words.csv`. The loaded data is converted into a list of dictionaries for easy access and manipulation.

* **User Interface Setup**: A main window is created using Tk() module and than by using canvas widget Flash cards are displayed using a Canvas widget. Images are used for the front and back sides of the flash card to display. also Buttons images are added for marking words as known (right_button) or unknown (wrong_button).

* **right_button_clicked()**: After the display of the first word if user click on the right button than that word is being removed from the list of dictionary and also simultaneously an new words_to_learn.csv file also created so when the user runs the app again the app will only going to show him the words which he doesn't and he still needs to learn those words only know besides that this function also call the `update_words()` function which will display the current word on the flash card and after 3 seconds it will call the `card_flipped` function which will display the english meaning of that card.

* **wrong_button_clicked()**: If user click this button than this function will skip the word and then  randomly select the word from the list of dictionary. and call the `update_words()` function which will display the current word on the flash card and after 3 seconds it will call the `card_flipped` function which will display the english meaning of that card.

* **update_words()**: this function will display the current telugu word and telugu title on the screen. 

* **card_flipped()**: this function will get called after 3 seconds and display the current words english translation and english title on the screen.

## Project Highlights

* Built an interactive language learning flash card app..
* Implemented smart file handling using try and except.
* Used pandas for efficient CSV data management.
