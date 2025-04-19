
# Day 14 - Higher Lower Game

## Project Overview  
This project is a console-based guessing game inspired by the concept of comparing social media follower counts. It was built as part of Day 14 of the #100DaysOfCode challenge. The goal of this game is to test your guessing skills by choosing between two public figures and deciding who has more followers.

## How It Works  
- The game starts by displaying two public figures with basic details like name, profession, and country.  
- You have to guess which one has more followers by typing 'A' or 'B'.  
- If your guess is correct, you score a point and move on to the next round.  
- The second figure becomes the first for the next round, and a new figure is randomly selected for comparison.  
- If the guess is wrong, the final score is displayed and you are asked if you want to restart the game.  
- The game continues until the player chooses to exit or makes an incorrect guess.

## Code Highlights  
- **compare_a() and compare_b():** Functions that randomly select and display public figures from the data set.  
- **shuffle_compare():** Moves Compare B to Compare A and selects a new Compare B for the next round.  
- **Score Management:** Keeps track of the user’s score and displays it after each correct guess.  
- **Restart Functionality:** Asks the user if they want to play again after a wrong guess.  
- **Input Validation:** Ensures the user types only valid responses like 'a', 'b', 'y', or 'n'.

--- 
