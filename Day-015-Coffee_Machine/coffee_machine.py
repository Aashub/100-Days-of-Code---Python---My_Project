













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
