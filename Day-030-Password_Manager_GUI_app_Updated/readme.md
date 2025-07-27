# Day 30 - Password Manager GUI App Updated

## Project Overview

This is an updated version of the Password Manager app project. In this version, users can not only generate strong, complex passwords but also search for their saved passwords using a Search button. If the website data exists in the .json file, the app will show a pop-up with the email and password, and the password will be automatically copied to the clipboard so users don’t have to remember it. If the website doesn’t exist, a prompt notifies them that the provided key does not exist.

To build this project, I learned how to use try, except, else, and finally blocks for proper error handling, how to use the pyperclip library for auto-copying passwords, and how to handle file operations and JSON data using load(), update(), and dump() in Python.

## What I Have Learned

* To handle user interaction smartly, I  used `messagebox.showinfo()` to alert the user when fields are left empty  & if the file didn't exist and if they didn't gave any input in search field, 

* I also practiced reading and writing JSON data, handling missing files with `FileNotFoundError`, and updating existing records using `json.load()` and `json.dump()`.

* I also learned how to use `try, except, else, and finally blocks` to handle file operations and user errors exception. For example, I used try to open data.json file even when it doesn't exit so it gives me an notification that file does not exit that how i handledthe FileNotFoundError.

## How It Works

* **User Interface Setup**: A window is created using `Tk()`, and all widgets like labels, entry fields, and buttons are positioned using `.grid()`.

* **Input Fields**: The user types the website/platform name, email/username, and password. They can also click on **"Generate Password"** to auto-generate a strong password.

* **Generating a Password**: When the user clicks the **"Generate Password"** button, the app uses random letters, numbers, and symbols to create a strong password using list comprehension. The generated password is shown in the input field and also copied to the clipboard for immediate use.

* **Validation & Saving Data**: If any input is left empty, a pop-up alert is shown. that fill all the input, if all the input is filled and user clicks to add then data will be saved in `data.json` file if file doesn't exist then new file also created if the user has filled all the details.

* **Finding a Saved Password**: if user try to search the website name and for the first time when file is not present it will get notification of file not found and if it is present and When the user enters a website name and clicks **"Search"**, the app looks up the website in the `data.json` file. If found, it shows the associated email and password in a pop-up and copies them to the clipboard. If not found, an alert is shown saying no details exist. This feature adds convenience and quick access to stored credentials.

---

## Project Highlights

* Built a full-fledged GUI application.
* Learned user-friendly field validation and pop-up handling with messageboxes.
* Practiced working with files using `open()`, `write()`, and `json.load()`/`json.dump()`.
* Applied clipboard functionality to copy both email and password instantly.
* Learned how to use `try, except, else, and finally blocks` for error handling

---
