# Day 15 - Coffee Machine Project

## Project Overview
This Coffee Machine Project is a Python console application that simulates a real-world coffee vending machine. Where Users can select a drink, by insert coins, and get their beverage if the machine has enough resources and correct payment has been done. This project is all about to implement all the Python concepts I have learned so far, including dictionaries, functions, conditionals, loops, exception handling, and arithmetic, to manage user input, process payments, and update resources(inventory) and profits, for espresso, latte, and cappuccino orders.

---

## How It Works

- User Interaction: The user selects a coffee (espresso, latte, cappuccino), views available resources by typing report, or turns off the machine with off.
- Displaying Resources: The machine shows the current available resources, including the amount of water, milk, coffee, and the total profit accumulated.
- Checking Resources: Before making the coffee, the program checks if there are enough ingredients (water, milk, and coffee) to fulfill the user’s request.
- Accepting Coins: The program prompts the user to insert coins in (quarters, dimes, nickels, and pennies). The total money inserted is calculated by adding up the values of the coins entered.
- Processing Payments: Once the coins are inserted, the program checks if the total amount matches the cost of the selected coffee. If the user has inserted more than required, it calculates the refund (change) that needs to be given back.
- Serving the Coffee: If the inserted payment is sufficient and resources are available, the coffee is served. A message is displayed to confirm the coffee is ready, and any necessary change is returned to the user.

---

## Project Highlights

- **Modular Functions**: Each task is handled by its own function (`check_resources()`, `insert_coins()`, `check_transaction_successful()`,`make_coffee()`), making the code clean and easy to maintain.
- **REsource Tracking**: Tracks ingredients and automatically updates after each transaction.
- **Profit Calculation**: Tracks total profit from coffee sales.

---


