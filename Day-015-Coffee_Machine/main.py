MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
units = ["ml", "ml", "gm"]
MONEY = 0
COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

def check_resources(coffee):
    """this function will check coffee machine have enough resources or not and return some value for further processing"""

    for resource_checking in MENU[coffee]["ingredients"]:
        resource = MENU[coffee]["ingredients"][resource_checking]

        # if coffee machine have less resources than this if statement will run
        if resources[resource_checking] < resource:
            print(f"Sorry there is not enough {resource_checking}")
            return 0

    else:
        return "enough_resources"

def insert_coins():
    """this function will do total of coins inserted by user and return overall total of coins."""
    coins_total = 0
    print("Please insert coins.")

    for inserted_coin in COINS:
        insert_coin = float(input(f"how many {inserted_coin}?: "))
        coins_total += (COINS[inserted_coin] * insert_coin)

    return coins_total

def check_transaction_successful(inserted_coins_total, coffee):
    """this function will check that transaction is being successfully completed or not and as per that return coffee cost."""

    coffee_cost = MENU[coffee]["cost"]
    if inserted_coins_total >= coffee_cost:
        change_amount = round(inserted_coins_total - coffee_cost, 2)

        print(f"Here is ${change_amount} dollars in change.")

    elif inserted_coins_total < coffee_cost:
        return 0

    return coffee_cost

def make_coffee(cof_amount, coffee_selected):
    """this function will reduce the ingredients as per the coffee selected and add money in the coffee machine."""

    global  MONEY
    # this for loop will help in to reduce each items ingredients one by one.
    for consuming_ingredients in MENU[coffee_selected]["ingredients"]:
        item_resource = MENU[coffee_selected]["ingredients"][consuming_ingredients]
        resources[consuming_ingredients] -= item_resource

    MONEY += cof_amount

    print(f"Here is your {coffee_selected} ☕️. Enjoy!")

start_machine = True

while start_machine:
    selected_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # this statement will run when maintainer will use off keyword for updating refueling the ingredients and taking the money.
    if selected_coffee == "off":
        start_machine = False

    # this statement will run when user wants to check that how much resources are available in the machine currently
    elif selected_coffee == "report":
        # num variable is used for updating the units of each ingredients one by one.
        num = 0
        for current_resources in resources:

            print(f"{current_resources}: {resources[current_resources]}{units[num]}")
            num += 1
        print(f"Money: ${MONEY}")

    # this statement will run if user selected any of this coffee
    elif selected_coffee == "espresso" or selected_coffee == "latte" or selected_coffee == "cappuccino":

        is_enough_resources = check_resources(selected_coffee)

        # this statement will check that if enough resources available than coin insertion and coffee making process will be implemented
        if is_enough_resources == "enough_resources":
            coins_value = insert_coins()
            coffee_amount = check_transaction_successful(inserted_coins_total= coins_value, coffee =selected_coffee)

            if coffee_amount == 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                make_coffee(cof_amount=coffee_amount, coffee_selected= selected_coffee)













