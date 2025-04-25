# Day 16 - Coffee Machine Project with OOP 

## Project Overview
The main objective of this project is to recreate a coffee machine from scratch by implementing Object-Oriented Programming (OOP) concepts—without looking into to the provided code files where all the functions were already written.
This project brings together everything learned so far in Python, especially the fundamentals of OOP including classes, objects, attributes, and methods. It simulates a real-world coffee machine that allows users to order drinks like espresso, latte, or cappuccino, pay with virtual coins, and receive their coffee if both resources and payment are sufficient.

## How It Works
- **User Interaction:** The user is asked what they would like (espresso/latte/cappuccino). They can also enter `report` to check available resources or `off` to shut down the machine.
- **Menu & Resources:** Coffee options and their ingredient requirements are handled by the `Menu` and `CoffeeMaker` classes respectively.
- **Payment Processing:** The `MoneyMachine` class handles coin inputs, calculates totals, verifies if the inserted amount is sufficient, and returns change if needed.
- **Coffee Serving:** If resources and payment are sufficient, the machine deducts ingredients and serves the coffee.

## Project Highlights

- **Object-Oriented Design:** The project is built using Object-Oriented Programming (OOP) principles, divided into four main classes: `MenuItem`, which defines each coffee drink with its ingredients and price; `Menu`, which manages the coffee options and allows the user to choose their drink; `CoffeeMaker`, which takes care of managing ingredients like water, milk, and coffee, and brews the selected drink; and `MoneyMachine`, which processes coins, checks if the payment is enough, and tracks the profit from each transaction.

- **Classes and Objects:** Various class objects are used to handle specific tasks. For example, `coffee_item = Menu()` is used to manage the available drinks and the user's selection, `start_coffee_machine = CoffeeMaker()` checks the available ingredients and brews the coffee, and `to_get_profit = MoneyMachine()` processes payments and tracks the machine's earnings.

- **Attributes & Methods:** The project uses attributes like `resources`, `ingredients`, and `profit` to keep track of the machine’s state, while methods such as `report()`, `make_coffee()`, and `make_payment()` perform essential actions like checking resources, brewing the coffee, and handling payments, making the entire process run smoothly.


This project was not just about making coffee—it was about leveling up my Python skills by applying OOP to build real-world simulations. The challenge to build it without any reference made the experience even more rewarding.

