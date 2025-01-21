# Day 15 - Coffee Machine Program  

## Overview  
The **Coffee Machine Program** is a Python application that simulates the operations of a coffee vending machine. It allows users to choose their preferred coffee, ensures resources are available, processes coin transactions, and updates the machine's resources and profits. This project consolidates various programming concepts such as functions, loops, conditionals, and error handling.  

---

## Key Features  
1. **Coffee Options**:  
   - Users can select from three coffee options: espresso, latte, and cappuccino.  
2. **Resource Management**:  
   - Checks if the machine has enough water, milk, and coffee to prepare the selected beverage.  
3. **Coin Transactions**:  
   - Accepts quarters, dimes, nickels, and pennies to process payments.  
   - Calculates the total amount inserted and ensures it covers the coffee's cost.  
   - Provides change if overpaid.  
4. **Profit Tracking**:  
   - Tracks the total money earned from coffee sales.  
5. **Reports**:  
   - Displays the current status of water, milk, coffee, and money in the machine.  
6. **Error Handling**:  
   - Includes a `try-except` block to catch invalid inputs or errors.  

---

## How It Works  
1. **User Input**:  
   - The user selects an option: espresso, latte, cappuccino, "report," or "off."  
2. **Report**:  
   - Displays the machine's current resource levels and total profit.  
3. **Coffee Selection**:  
   - Checks if resources are sufficient for the selected coffee.  
   - Processes coin transactions and updates resources if the transaction is successful.  
4. **Error Handling**:  
   - Prompts the user to enter valid input if an error occurs.  
5. **Exit**:  
   - Typing "off" ends the program.  

