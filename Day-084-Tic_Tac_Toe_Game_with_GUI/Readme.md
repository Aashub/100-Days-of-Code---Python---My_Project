# Day 84 – Tic Tac Toe Game with GUI (Tkinter)

## Project Overview

This is a fully functional Tic Tac Toe game built with Python's Tkinter library. The game features a graphical user interface (GUI) where two players can take turns placing X and O symbols on a 3x3 grid. It includes score tracking for multiple rounds, win detection with visual feedback (highlighting the winning line), match winner detection (first to win 5 rounds), and an interactive home screen where players can choose their opponent (Friend mode). The game resets automatically after each round and offers a rematch option at the end of a match.

The code is also designed with a future upgrade in mind, A Computer mode where players can play against an AI opponent, which can be added later by extending the existing game structure.

## What I Have Learned

* **Tkinter GUI Development**: Revised about how to build a graphical user interface using Python's built-in Tkinter library. Created windows, frames, canvases, buttons, labels, and handled user events like mouse clicks.

* **Object-Oriented Programming (OOP)**: Built the entire application using classes. The UserInterface class inherits from Tk and contains all the methods for creating UI elements, handling game logic, and managing game states.

* **Event Handling**: Used Tkinter's event binding system to capture mouse clicks on the game board. The bind("<Button-1>", screen_clicked) method triggers a function whenever a player clicks on the game grid.
    
* **Coordinate Mapping**: Created systems to map mouse click positions to specific cells on the game board. Used lists of x and y coordinates to determine which cell was clicked and where to draw the symbol.
 
* **Game State Management**: Managed game state using global variables to track whose turn it is, which cells are filled, player scores, and win conditions. Used TOTAL_CELL to count remaining empty cells.
 
* **Win Condition Detection**: Built a win detection system using sets. Each cell has a number (1-9), and the game checks if a player's cells match any winning combination (rows, columns, diagonals) by comparing sets.
 
* **Visual Feedback**: Used Tkinter's Canvas to draw game elements including grid lines, X and O symbols, win lines (yellow), and pop-up messages for round winners and match winners.

* **Nested Functions and Closures**: Used nested functions inside methods to handle specific tasks like the home screen button logic, which needed access to parent function variables.
 
* **Recursive UI Updates**: Used methods like create_game_layout() and reset_board() to redraw the game board after each round, while preserving player scores and game state.
 
* **Timeout and Delayed Execution**: Used self.after(1500, function) to delay the execution of functions. This allowed the win line to be displayed before the board resets.
 
* **For Loops with zip()**: Learned how to use zip() method with for loop to iterate through multiple lists. In the check_round_winner() method, I used zip() to iterate through row conditions, column conditions, and diagonal conditions simultaneously, checking all three types of win conditions in a single loop structure. 
 
* **Working with Sets**: Learned how to use Python sets for efficient win condition checking. Each cell is assigned a number (1-9). When a player clicks a cell, that cell number is added to their list. To check for a winner, I converted the list to a set using set() and compared it against all possible winning combinations using the <= operator (subset check) to check a winner. 


## How It Works

* **Imports and Global Variables**: The file imports Tkinter modules for game design, Global variables are defined including background colors, grid colors, symbol colors, win line color, total cells (9), winning score (5), and current scores for both players. Empty lists store player moves, and coordinate lists map click positions to cells.

* **Coordinate Systems**: Three parallel lists map the game board where `x_axis_limit_list` and `y_axis_limit_list` store the x and y boundaries for each cell (9 cells total), `symbol_cord_list` stores the center coordinates where symbols should be drawn, Each cell is numbered 1-9 for win condition checking
 
* **Win Conditions**: `win_condition_dict` stores all possible winning combinations sets of 3 rows, 3 columns, and 2 diagonals. `winning_line_dict` maps each winning combination to the x,y coordinates needed to draw the winning line.

* **UserInterface Class**: UserInterface Class Inherits from Tk and manages the entire application. The __init__ method sets up the window with a centered position, fixed size, and background color. .

* **home_screen_ui() method**: Displays the home screen with the game title and "Choose Your Opponent" options. When a player selects "Friend" or "Computer", the UI transitions to symbol selection (X or O) using nested function `home_screen_btn()`. The selected mode and symbols are passed to the `create_game_layout()` method.

* **create_game_layout() method**: `create_game_layout()` Destroys all previous widgets and creates the game board with grid lines (2 horizontal, 2 vertical), displays the score label showing current scores for both players, and calls `draw_symbol()` to start the game.

* **draw_symbol() method**: This method Binds mouse clicks to the canvas using <Button-1>. When a player clicks, the nested screen_clicked() function gets the mouse coordinates relative to the window and checks which cell was clicked using the coordinate lists. It alternates turns based on TOTAL_CELL % 2 - odd numbers mean Player 1's turn (X) and even numbers mean Player 2's turn (O). The symbol is drawn at the center of the clicked cell using symbol_cord_list, then the cell is removed from the coordinate lists to prevent overwriting, and TOTAL_CELL is decreased by 1 before calling `latest_cell_clicked()` to check for a winner.

* **latest_cell_clicked() method**: This method Converts player cell lists to sets and calls `check_round_winner()` to determine if a player has won.

* **check_round_winner() method**: check_round_winner() method is used to Compares player cell sets against all winning combinations in win_condition_dict. If a player matches any winning set, it increments their score, calls `draw_win_line()` to highlight the winning cells, and calls `show_round_winner()` to display a pop-up message, it also sets player_won  = True so it can call reset_board() method to reset the board for new round. If no winner is found and TOTAL_CELL == 0, it declares a draw by a pop up message.

* **draw_win_line() method**: Finds the winning combination in winning_line_dict, retrieves the coordinates, and draws a thick yellow line across the winning cells. Different line styles are used for rows, columns, and diagonals.

* **show_round_winner() method**: Creates a pop-up canvas with a white background centered on the game board. Displays either "Player 1 Won!", "Player 2 Won!", or "This round is Draw!".

* **reset_board() method**: This method Calls reset_game_variables() method to clear player moves and reset coordinate lists. After a 1.5-second delay, it calls create_game_layout() to redraw the board, and check_match_winner() to see if anyone has won the overall match.

* **check_match_winner() method**: This method Checks if either player's score has reached WINNING_SCORE (5). The nested `display_match_winner()` function shows a pop-up declaring the match winner with the final score. After 1.5 seconds, it calls `rematch()` method.

* **reset_game_variables() method**: Resets all game variables - TOTAL_CELL set back to 9, clears player cell lists, resets coordinate lists to their original positions, and unbinds the mouse click event.

* **rematch() method**: Displays a pop-up asking "Do you want to Play Again?" with Yes and No buttons. If the player clicks Yes, the nested `reset_new_match()` function resets both scores to 0, clears the screen, and returns to the home screen. If the player clicks No, the `exit_game()` function closes the application window.


## Project Highlights

* **Tkinter GUI**: Built a complete graphical interface with custom styling, colors, and fonts.
* **Full Game Logic**: Implemented turn-based gameplay, win detection, draw detection, and score tracking.
* **Visual Win Feedback**: Highlights winning cells with a yellow line and displays pop-up messages for round winners.
* **Coordinate Mapping**: Used custom coordinate systems to detect which cell was clicked and place symbols accurately.
* **OOP Design**: Organized the code using classes and methods for clean, maintainable code.
* **Event Handling**: Used mouse click events to capture user input and update the game state.
* **Using zip() with For Loops**: Learned how to iterate through multiple lists simultaneously using zip() in for loops, which made the code cleaner and eliminated complex nested loops
* **Working with Sets**:  Learned how to use Python sets to store player moves and efficiently check for winning combinations using subset comparisons (<=).
