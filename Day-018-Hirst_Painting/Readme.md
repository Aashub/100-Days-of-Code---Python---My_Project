
# Day 18 - Hirst Painting Project


##  Project Overview

In this project, I created a digital version of a hirst painting inspired by **Damien Hirst** using Python. I used the `turtle` graphics module to draw, and optionally the `colorgram` module to extract colors from an image. The final output is a grid of randomly colored dots, each chosen from a list of RGB values.
This project helped me understand how to use **modules**, Read and understand **Python documentation** to use methods, Work with **tuples** and **lists** & Control the turtle graphics screen and cursor

---

##  What I have Learned

* How to import & use modules like `turtle`,  and `colorgram`
* How to **extract RGB colors from an image** using the `colorgram` module
* The concept of tuples and how to use them for RGB values
* How to navigate Python documentation to understand methods like .dot(), .setx(), .sety(), and .penup() and how to use them
* How to use **colormode(255)** to enable RGB-based coloring in turtle graphics

---

##  How It Works

* A list of RGB color tuples is created, by using the `colorgram.extract()` method.
* A turtle object is set up with pen removed, speed set to fast, and color mode switched to RGB.
* A function named `create_dot()` draws a horizontal line of 15 randomly colored dots.
* A loop moves the turtle vertically upword after each line and resets the x-position to start a new row.
* The loop repeats this process to create a 15x15 dot grid pattern.
* The program waits for a mouse click to exit using `exitonclick()`.

---

##  Project Highlights

*  Used the **Turtle Graphics** module to create visual output.
*  Stored RGB colors as **tuples** and selected them randomly for each dot.
*  Practiced **working with external modules** like `colorgram` (optional for color extraction).
*  Explored **Python documentation** to understand turtle methods and how to use them.
