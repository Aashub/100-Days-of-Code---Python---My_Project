# Day 29 - 30 - Password Manager GUI App

## Project Overview
 This project is a **Password Manager** app using **Python’s Tkinter library**, which introduced me to building real-world GUI applications that are not only interactive but also practical for daily use. In this  **Password Manager GUI App** user can Generate **strong, complex passwords** that are hard to crack and Save those passwords along with the **website/platform name** and **email/username** in a `.json` file so they don't have to be remembered and can use them later and they can also search the email address and password using serarch button if they want to look into that password. In order to create this project i have learned about how to use pyperclip library for auto copy the generated password, Tkinter class, revised and implemented how to use list comprehension and file handling in python and learned about how to read, write and update data in `.json` file, & how to do error handling using try, except, else, finally block of code and also learned about how to raise custom error using raise block.  

---

## What I Have Learned

* I learned how to build an interactive GUI using Python's Tkinter library. To begin with, I used Tk() to create the main window where everything appears. Then I added static text using Label() and used Entry() for input fields where the user can type their website, email, and password.

* To make the interface functional, I used Button() class to trigger specific actions like generating or saving a password. I added a logo to the window using Canvas() and PhotoImage() which allowed me to display an image (logo.png) in the GUI.

* To handle user interactions smartly I have learned about how ot use a  messagebox.showinfo() to notify users when they leave fields empty, and messagebox.askokcancel() to confirm the details before saving. This added a layer of error prevention and better UX.

* Also I have revised and implemented the use of list comprehensions for generating a mix of letters, symbols, and numbers to create a password. Then I learned ow to use .join() to combine them into one string. I also learned how to automatically copy the password to clipboard using pyperclip.copy().

* by building this project I have learned about how to read(`.load()`), write(`.dump()`), append(`.update()`) data in existing json file and also create a new .json file if it doesn't exist automatically.

* Also I have learned about `try, except, else, and finally` block of code to handle error where on certain situation programs give us an error if somethign will go wrong for example in this program when the user runs the program first time the .jason file is not exist so this try except block of code execute and create a new file so that users data get stored in the file.

* Besides that I also learned about how to raise a custom error in certain situation using `raise` keyword

---

## How It Works 

* **User Interface Setup**: A window is created using `Tk()` class, and widgets like labels, input fields, and buttons are arranged using `.grid()`.

* **Input Fields**:The user types the website/platform name, their email or username, and either their own password or clicks on **“Generate Password”** to auto-generate one.

* **Generating a Password**: When the **Generate Password** button is clicked A strong password is created using `generate_password` function that randoms letters, numbers, and symbols via list comprehension and created a strong password. The password is displayed in the password field and automatically copied to the clipboard to use it.

* **Validation & Saving the Data**: If any input field is empty and the user tries to save, a **pop-up alert** appears saying not to leave fields empty. When all fields are filled and the **Add** button is clicked a confirmation pop-up appears showing all the input details. If the user clicks OK, the details are saved to a `data.json` file. The input fields are then cleared for the next entry.

* **JSON File Handling**:The password details are stored in a data.json file using dictionary format. If the file does not exist, it is automatically created; otherwise, the new data is merged with the existing data.  

* **Exception Handling**: A try-except-else-finally block is used to safely handle file operations in case the file does not exist than this block of code will prevent the program from crashing when the data file is missing and create a new file.

* **Searching Saved Passwords**: The Search button allows users to retrieve saved credentials. If the website exists in the JSON file, the email and password are shown in a pop-up and the password is copied to the clipboard. If not found or if the file is missing, an appropriate alert message is displayed.
## Project Highlights

* Built the GUI application
* Revised how to use list comprehension.
* learned how to use, User-friendly field validation and pop-up messages.
* Revised myself about how open() and write() a file.
* learned about how to do error handling using try, except, else, and final block of code
* learned about how to raise a custom error.
* learned about how to read, write and update data in .json file.
* Real-world utility app that actually helps manage passwords.

---

