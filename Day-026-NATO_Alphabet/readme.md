# Day 26 - NATO Alphabet

## Project Overview

This is a simple NATO Alphabet converter project. In this project we enter a word (like a name or any string), and the program returns its NATO phonetic code for each alphabet character. While making this project, I learned how to use **dictionary comprehension**, **list comprehension**, and how to **iterate through a pandas DataFrame** to build a custom dictionary. I also practiced working with CSV files and used **pandas** to read and access each row easily.

---

## What I Have Learned

* How to read a CSV file using pandas.read_csv(): We can use pandas.read_csv("filename.csv") to open a CSV file. It loads the data in a format called DataFrame, which is like a table(rows and columns). This way, We can easily go through each row or pull specific data from any column.

* How to loop through each row using .iterrows(): After loading the CSV data, we can use .iterrows() to go through each row one at a time. It gives you the index and also the row itself. From there, you can use things like row.letter and row.code to get the actual values.
  
* **dictionary comprehension:** We can use dictionary comprehension to create a new dictionary using just one line of code. We provide the row and index while looping through the DataFrame using .iterrows(), and then define what we want as the key and value. Based on our requirement, we can filter or customize the output. This helps us create a clean and efficient dictionary.
 
* **list comprehension:** We can use List comprehension to create a new list in a single line by looping through an existing sequence like a string, list, or dictionary. We can also add conditions to filter what gets added. In our case, we loop through each character of the user input and fetch its value from the dictionary only if that character exists in it. This makes the code shorter, cleaner, and easier to read.

---

## How It Works

* First, the CSV file (`nato_phonetic_alphabet.csv`) is loaded using `pandas.read_csv()`.
* Then, using dictionary comprehension, a new dictionary is made where each letter becomes a key and its NATO code becomes the value.
   Example: `'A': 'Alpha'`
* The user is prompted to input a word. The input is converted to uppercase to match the dictionary keys.
* The program loops through each character in the input and checks if that character is in the dictionary.
* If it is, it adds the corresponding NATO code to a new list.
* Finally, the list of NATO codes is created.

---

## Project Highlights

*  Used **pandas** to read data from a CSV file.
*  learned how to use a **dictionary comprehension**.
*  learned how to use a **list comprehension**.
*  Practiced reading and iterating through **DataFrames** with `.iterrows()`.

