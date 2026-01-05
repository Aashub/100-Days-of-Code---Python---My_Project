# Day 27 - Miles and Km Converter 

## Project Overview

This  project is a beginner-friendly **Graphical User Interface (GUI)** Project of MIles to Km Converter tool where, The user types in a number representing miles & km and when he Clicks the “Calculate” button The program then takes that input, converts it into kilometers and miles as per whatever changes the user wants, and displays the result on the screen.
To build this project, I learned about how to use  the **Tkinter** library, which is used to create GUI applications in Python. I learned about python advanced function like Default arguments, args: many positional arguments, kwargs: many keyword arguments and tkinter module for how to create windows, add buttons, text fields, labels, and handle input events.

---

## What I Have Learned

* **Advanced Functions**:
  * Default arguments: These are function parameters that already have a value. If you don’t pass that value while calling the function, Python uses the default one.
  * args (many positional arguments): It allows a function to accept any number of positional arguments. The values are stored as a tuple inside the function. for example def add_numbers(*args) and it will take any number of positional argument add_numbers(10, 20, 30).
  * **kwargs (many keyword arguments): It allows a function to accept any number of keyword arguments. The values are stored as a dictionary inside the function. for example while creating a function we can create is something like def function(**kwargs) and while calling a function(name=, age=, age=, profession= .....) 

* **`Tk()`**: This initializes the main window where everything in the GUI appears. It's the base of the GUI.

* **`Label()`**: Used to display static text on the screen like "Miles", "Km", and "is equal to". It helps guide the user.

* **`Entry()`**: This creates an input box where users can type the text(string number) which we have letter converted it into int variable so we do the calculations.

* **`Button()`**: This creates a clickable button. which we can use to perform any kind of functionality where we can trigger some event to happen in my project case I assigned a command to it so that when it's clicked, the `unit_converter()` function happens and runs so it can do the calculations of miles to km & km to miles & similarly i have created unit switch button which switches the unit to miles to km and km  to miles with function of `unit_switcher()`.

* **`grid()`**: This method arranges all the widgets (like labels, buttons, inputs) in a structured row and column format.

* **`place()`**: This method arranges all the widgets in a specific location in a screen by giving their x and y coordinate.

* **`config()`**: this method is used to  update the text of a widget dynamically. I have used it to show the updated km value once its being calculated.

* **`mainloop()`**: this method will help us to Keeps the GUI running in a loop so it doesn’t close instantly. It's necessary for any interactive GUI app.

---

## How It Works 

Here’s how the project works behind the scenes:

* **GUI Initialization**: The program starts by creating a window object by using `Tk()`. by using this windows object  we set the size of the screen by using `minsize()` method and we have used `title()` method to name the windows the project title.

* **Input Field**: Then we have used an `Entry()` class which allows us to create a field in GUI to add any input, and by creating its object entry we have set their initial values to 0. 

* **Text Labels**: Several `Label()` widgets are used in this project to display static text like "Miles", "Km", and "is equal to".

* **Calculate Button**: A button labeled "Calculate" is created using `Button()` class . in this program by using calculate_button object it has allows us to trigger the unit_converter function When its clicked, it calls the `unit_converter()` function and as per user requirement it changes  miles to km and km to miles and show invalid input if the user has entered invalid input I have used `try & except block` to catch input error.

* **Switch Button**: A switch button is created using `Button()` class. this swtich button switches the unit up and down as per the user requirement so that it displays on the screen from which unit to which unit user wants to convert the unit when the button got clicked it calls the `unit_switcher()` function and change the units on the screen.

* **unit_converter()**: The `unit_converter()` function reads the number entered using `.get()` and then it converts the value from miles to km & km to miles, Then it updates the `converting_value` label with the new value using `.config()`.

* **Displaying the Result**: The result is shown just next to the “is equal to” label text dynamically.

* **Running the GUI**: The `mainloop()` method keeps the window open until the user closes it.

---

## Project Highlights

* Built this project using Python's Tkinter library which allows us to use GUI.
* Learned how to use input fields, labels, and buttons interactively.


