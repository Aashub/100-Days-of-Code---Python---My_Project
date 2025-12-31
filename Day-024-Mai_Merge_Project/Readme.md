# Day 24 - Mail Merge

## Project Overview

This is a Mail Merge project where I automated the process of creating personalized letters using Python. The idea is simple we have a draft letter and a list of invited names, and the program creates individual ready-to-send letters for each name automatically. To build this project, I learned how to work with files in Python. I used functions like `open()`, `read()`, and `write()` inside a `with` statement, and also understood the concept of absolute and relative file paths. All these skills helped me create this mail merge project.

---

## What I Have Learned

* **open, read, and write files:** I learned how to use the open() function to access a file, read() to get its contents, and write() to create or update a file. This helped me manage the draft letter and create new personalized letters.

* **`with` keyword:** The with statement automatically handles opening and closing files. This makes the code cleaner and prevents errors that can happen if we forget to close a file manually.

*  **absolute and relative file paths:** An absolute path starts from the root so it gives us the full location of a file on your system from where we can navigate to retrieve whichever file we want to aceess, A relative file path points to the file location which is relative to your current working directory, I have used relative paths to easily navigate to files in my project
---

## How It Works

* **create_namelist()**: The create_namelist() function is responsible for preparing the invited names list. First, it reads names line by line from the invited_names.txt file and stores them in a list. Since each name contains a \n at the end, the function also strips that extra character to clean the names.
& Finally, it returns a list of properly formatted names that can be used to generate letters.

* **create_letter()**: Inside the create_letter() function, the starting_letter.txt file is opened in read mode. This file contains the base letter format with a placeholder [name], which will later be replaced with each invited person’s name.

  * The function loops through the cleaned name list and replaces the [name] placeholder with the actual name using Python’s replace() method.
  This creates a personalized version of the letter for each person.

  * For every name, a new text file is created inside the ReadyToSend folder. Each file is named using the invited person’s name (for example: letter_for_asteroid.txt) and contains the personalized letter content.

* **Automated letter creation**: Once the functions are called, the entire process runs automatically reading names, cleaning them, personalizing the letter, and generating ready-to-send files without any manual effort.

---

## Project Highlights

* Used the replace() function to find and replace [name] in the draft letter
* Applied `with` statement to handle file operations safely and efficiently.
* Learned and used **relative file paths** for accessing folders and files inside the project directory.
* learned how to use open(), read() and write() function to read, create, and update the file.
---

