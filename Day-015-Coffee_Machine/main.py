from art import logo

# this is the dictionary of coffee ingredients and their cost prices
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
    "profit": 0

}

# these are the global variables which will never going to be changed
QUARTERS =  0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

def resource_deducted(selected_coffee):
    """this function will deduct the resources from ingredients once the transaction is being completed successfully."""
    detectable_ingredients = MENU[selected_coffee]["ingredients"]

    # count variable will help us to not get into the profit key in resources dictionary so we don't get error.
    count = 0
    for to_deduct in resources:
        count += 1
        if count <= 3:
            resources[to_deduct] -= detectable_ingredients[to_deduct]
        else:
            pass

def check_resources(selected_coffee):
    """this function will check that in coffee machine do it have enough resources to make coffee or not."""
    coffee_ingredients = MENU[selected_coffee]["ingredients"]
    coffee_cost = MENU[selected_coffee]["cost"]

    # count variable will help us to not get into the profit key in resources dictionary so we don't get error.
    count = 0
    for enough_resources in resources:
        count += 1

        if count <= 3:

            # if we have enough resources then we will return coffee cost and ingredient(it's a variable we have assigned
            # in function call) return value as true that coffee machine have enough resources
            if resources[enough_resources] > coffee_ingredients[enough_resources]:
                return True, coffee_cost

            # if not then this line of code execute and it will return ingredient(it's a variable we have assigned in
            # function call) return value as Fase that coffee machine don't have enough resources
            elif resources[enough_resources] < coffee_ingredients[enough_resources]:
                print(f"Sorry there is not enough {enough_resources}.")
                return False, 0
        else:
            pass


def process_coins(coffee_cost, coffee):
    """this function will check that user have given the enough amount or not to make coffee."""

    correct_input = True
    while correct_input:

        print("Please insert coins.")

        # try except block of code will help us to check that user has provided correct variable input or not if not
        # then it will ask the user again to enter correct input.
        try:
            inserted_quarters = int(input("how many quarters?: "))
            inserted_dimes = int(input("how many dimes?: "))
            inserted_nickles = int(input("how many nickles?: "))
            inserted_pennies = int(input("how many pennies?: "))

            # here overall inserted amount will be calculated.
            inserted_amount = (inserted_quarters * QUARTERS) + (inserted_dimes * DIMES) + (inserted_nickles * NICKLES) + (
                        inserted_pennies * PENNIES)

            # this if else statement will check that user inserted amount is enough or not to create coffee.
            if inserted_amount >= coffee_cost:
                refund_amount = inserted_amount - coffee_cost

                print(f"Here is ${round(refund_amount, 2)} in change.")
                print(f"Here is your {coffee} ☕️. Enjoy!")

                resource_deducted(coffee)
                return coffee_cost

            elif inserted_amount < coffee_cost:
                print(f"Sorry that's not enough money. Money refunded.")
                return 0

        except ValueError:
            print("Please enter a valid number for coins.")


print(logo)
should_continue = True
while should_continue:

    #this while loop will run until the user don't provide the correct input.
    select_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # this statement will turn off the coffee machine.
    if select_coffee == "off":
        should_continue = False

    # this statement will help us to check that in coffee machine we have enough resources or not.
    elif select_coffee == "report":

        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["profit"]}")

    elif select_coffee == "espresso" or select_coffee == "latte" or select_coffee == "cappuccino":
        enough_ingredient, cost_of_coffee = check_resources(select_coffee)

        if enough_ingredient:
            deducted_amount = process_coins(cost_of_coffee, select_coffee)

            resources["profit"] += deducted_amount

    else:
        print("invalid input")

