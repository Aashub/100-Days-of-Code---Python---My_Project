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

* **Initialize a list**: I have used an empty list `name_list` store all cleaned-up invited names so I can use them to create a letter 

* **starting_letter(draft letter)**: The starting letter file is opened and read using `with open()`. This letter contains a placeholder `[name]` which we need to replace with names to create our letters.

* **Read invited names**: The invited names are read from another file, line by line, and stored in `name_list` after stripping `\n` characters which is preventing me to create new automated file.
  
* **Create letters**: For each name in the list, a new file is created using `with open()` in write mode which allows us to create a new file if the file is not created. Initially, it just copies the draft letter text so we can modify them later.

* **Personalize the letters**: Each newly created file is opened again and the placeholder `[name]` is replaced with the actual invited name by using `replace` method of python.  and then we have opened the files again but this time in write mode so the updated content is written back into the same file.

---

## Project Highlights

* Used the replace() function to find and replace [name] in the draft letter
* Applied `with` statement to handle file operations safely and efficiently.
* Learned and used **relative file paths** for accessing folders and files inside the project directory.
* learned how to use open(), read() and write() function to read, create, and update the file.
---

