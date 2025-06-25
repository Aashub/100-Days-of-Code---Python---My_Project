
# Day 25 - India State/UT Guess Game 
## Project Overview

This project is a **state/UT guessing game** where the player is asked to name all the states and union territories of India. When the player guesses a correct name (with exact spelling), the name appears on the map at its respective location. The guessing continues until either all 36 names are guessed or the player chooses to exit. If the player types **"Exit"**, the game stops and generates a `states_to_learn.csv` file that lists all the states/UTs that the player didn’t guess correctly. I’ve used a combination of **turtle graphics** and **pandas** to build this project. This was a great way to bring together everything I’ve learned so far, including working with CSV files, coordinates, input handling, and turtle screen manipulation.

---

## What I Have Learned

* I learned how to read data from a .csv file using pandas.read_csv("indian_states_coordinates_turtle.csv"). This helps me load all the data into a table-like format called a DataFrame, where each row is one entry and each column is a type of information. Once the data is loaded, I can easily work with it like checking a specific row or column.

* I also understood the difference between a DataFrame and a Series. A DataFrame is the whole table, and a Series is just one column from that table. I can filter the rows using conditions like df.loc[df['column_name'] == 'value'] to get only the rows that match what I’m looking for.

* Lastly, I learned how to save my own data into a .csv file. First, I take my list (or dictionary), convert it into a DataFrame using pandas.DataFrame(), and then save it using .to_csv("states_to_learn.csv", index=False). The index=False part is important—it just makes sure row numbers don’t get saved in the file.

---

## How It Works

* The map of India is set up using a `.gif` image registered with the turtle screen.
* The CSV file (`indian_states_coordinates_turtle.csv`) contains a list of all Indian states/UTs and their `x` and `y` coordinates.
* When a loop runs where the user is prompted to enter a state name.
* If the guessed name matches any from the CSV file (case-sensitive with `.title()`), the guessed state or UT will be get displayed at the correct location on the map.
* Also Correct guesses are stored in a list (`correct_guees`) so later we can use this file to find out which states player is unable to guessed it.
* If the user enters `"Exit"`, the game stops and the list of **missed states/UTs** is saved in a file named `states_to_learn.csv` so the user can check that file to know which state he is unable to guessed.
* If all 36 state/UT names are guessed, a congratulatory message appears on the screen displaying that he has able to guess all the states.

---

## Project Highlights

* Used **turtle graphics** to display state names on a visual map of India.
* learned who to use **pandas** library for reading and writing CSV data.
* Generated a custom **output file** listing unguessed states using Python logic.
* Practiced working with **data filtering** and conditional logic using pandas.
---
