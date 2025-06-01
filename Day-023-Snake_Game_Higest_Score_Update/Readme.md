# Day 23 - Snake Game Updated
##  Project Overview

This is an updated Snake Game project with all the previous functionality intact. In this version, whenever the player reaches a new highest score, it gets stored in a file so it can be used later. When the game is restarted, the highest score from the file is displayed on the screen. This functionality is achieved using Python's read and write methods, which I learned in today’s lesson and used to update my Snake Game project.

---

##  What I Have Learned
* **read():** This method is used to read data from a file. When the game restarts, In this project it is used as to read the initial saved score from the file and displays it on the screen and after the update of highest score it also displays it whenver the game restarted. This is done using the with statement, which opens the file in read mode ("r") and ensures it is properly closed after reading.

* **write():** This method is used to save data to a file or update it. In this project it is used to update the new highest score if players exceed the current highest score into a file so it can be accessed later. This is also done using the with statement, which safely opens the file in write mode ("w") and automatically closes it afterward.

---

## How It Works

* **`__init__()` method**: Uses the `read()` method with the `with` statement to open `data.txt` and load the initial saved score when the game starts. This value is stored in `self.highest_score` and displayed on the screen along with the current score.

* **`reset_score()` method**: Uses the `write()` method with the `with` statement to update `data.txt` with a new highest score if the current score exceeds the previous one. This ensures the highest score is saved and persists across game sessions.


## Project Highlights
* Learned how to implement the functionality of to save the highest score so it stays saved even after restarting the game, letting players always see their best score when they play again. 



