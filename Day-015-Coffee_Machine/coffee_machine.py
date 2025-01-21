from main import MENU, resources
from art import logo

print(logo)

"""these are the actual value of all this coins"""
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

"""in this function we basically check we have enough ingredients in order to make coffee"""
def is_resource_sufficient(coffee_ingredients):

    for ingred in coffee_ingredients:

        # if coffee ingredients contains more resources than available resources then it will not create coffee
        if coffee_ingredients[ingred] >= resources[ingred]:
            print("Sorry there is not enough resources")
            return False

    return True

"""here user will insert their coins so he can get coffee"""
def insert_coin():
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))

    inserted_amount = QUARTERS * quarters + DIMES * dimes + NICKLES * nickles + PENNIES * pennies

    return inserted_amount

"""in this function we can check transaction that amount provided by user is enough 
or not if enough then coffee is being dispensed"""
def check_transaction(inserted_amo, actual_cost):

    if inserted_amo < actual_cost:
        print("Sorry that's not enough money. Money refunded")
        return 0

    elif inserted_amo >= actual_cost:
        change = inserted_amo - actual_cost
        print(f"Here is ${round(change,2)} dollars in change.")
        return  actual_cost

"""in this function once the transaction is being successful then coffee is created and from overall resources the selected
coffee amount is being reduced and profit amount is being added in the coffee machine use 'report' to check"""
def reduce_the_ingredient(profit_amount, ordered_cof_ingred):

    for ingred in ordered_cof_ingred:
        resources[ingred] -= ordered_cof_ingred[ingred]

    resources["profit"] += profit_amount


should_continue = True

while should_continue:
    try:
        select_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()

        if select_coffee == "off":
            should_continue = False

        # here actual overall profit and current resources contain will show
        elif select_coffee == "report":
            print(f"Water: {resources["water"]}ml")
            print(f"Milk: {resources["milk"]}ml")
            print(f"Coffee: {resources["coffee"]}gm")
            print(f"Money: ${resources["profit"]}")

        else:
            ordered_coffee = MENU[select_coffee]
            if is_resource_sufficient(ordered_coffee["ingredients"]) :

                print("Insert The Coins:")
                inserted_amount = insert_coin()

                profit = check_transaction(inserted_amount, ordered_coffee["cost"])

                if profit > 0:
                    reduce_the_ingredient(profit, ordered_coffee["ingredients"])
                    print(f"Here is your {select_coffee} ☕ ️. Enjoy!")

    # if user provide wrong input then this msg will appear
    except Exception as e:
        print(f"The value provided is incorrect please provide correct value: {e}")




# ___________________________________________________________________________Previously created Coffee machine code_____________________________________________________________________________

# # todo: menus
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#             "milk":0,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100


# }


# def is_resource_sufficient(order_ingredient):

#     """check is resources are sufficient or not."""

#     for item in order_ingredient:

#         if order_ingredient[item] >= resources[item]:

#             print(f"Sorry there is not enough {item}.")
#             return False

#     return True

# def process_coin():

#     """return the total calculated from coins inserted"""

#     print("Please insert coin.")

#     input_quarter = int(input("how many quarters?: "))

#     input_dime = int(input("how many dimes?: "))

#     input_nickel = int(input("how many nickels?: "))

#     input_pennies = int(input("how many pennies?: "))

#     quarter_value = 25 / 100
#     dime_value = 10 / 100
#     nickel_value = 5 / 100
#     pennies_value = 1 / 100

#     paid_price = quarter_value * input_quarter + dime_value * input_dime + nickel_value * input_nickel + pennies_value * input_pennies


#     return paid_price

# def is_transaction_successful(coffee_cost, money_recieved):

#     """check if transaction is successful then subtract the money and add on profit also if money is not enough then
#     money is refunded """

#     if money_recieved >= coffee_cost:
#         global profit
#         change = round(money_recieved - coffee_cost, 2)
#         print(f"Here is ${change} in change.")
#         profit += coffee_cost
#         return True

#     else:
#         print("Sorry that's not enough money, Money refunded")
#         return False

# def start_coffee(choice, order_ingredient):

#     """here ingredients are substracted and if coffee is being made """

#     for item in order_ingredient:

#         resources[item] -= order_ingredient[item]

#     print(f"Here is your {choice} ☕")

# should_continue = True

# while  should_continue:
#     choice = input("What would you like? (espresso/latte/cappuccino):")
#     if choice == "off":
#         should_continue = False
#     elif choice == "report":
#         print(f"Water:{resources['water']} ")
#         print(f"Milk: {resources['milk']}")
#         print(f"Coffee:{resources['coffee']}")
#         print(f"Money :{profit}")
#     else:
#         order = MENU[choice]
#         if is_resource_sufficient(order["ingredients"]):
#            payment = process_coin()

#            if is_transaction_successful(order["cost"],payment ):
#                start_coffee(choice, order["ingredients"])
