from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# here are creating objects of each class
menu = Menu()
coffee_maker = CoffeeMaker()
insert_money = MoneyMachine()

# the while loop will run until the maintainer don't decide to turn this off.
is_machine_on = True
while is_machine_on:

    choose = input(f"What would you like? ({menu.get_items()}):").lower()

    if choose == "report":

        # below two methods will print the current resources of coffee ingredients and current profit amount of coffee machine
        coffee_maker.report()
        insert_money.report()

    elif choose == "off":
        is_machine_on = False

    elif choose == "latte" or choose == "espresso" or choose == "cappuccino":

        # menu object find drink method will look into the chosen drink and if drink name matches then return that drink items object.
        menu_item = menu.find_drink(order_name = choose)

        # coffee_maker object method  is_resource_sufficient will take menu_item object and it will check that does
        # coffee machine have enough resources or not and as per that return True or False for further processing
        enough_resources = coffee_maker.is_resource_sufficient(drink = menu_item)

        if enough_resources:

            # insert_money object make_payment method will check that by using the menu_item.cost parameter that user has
            # inserted enough money or not and as per that if will return True or False
            enough_coins = insert_money.make_payment(cost = menu_item.cost)

            if enough_coins:

                # coffee_maker object make_coffee method take menu_item object as input and deduct all the resources and give the user its coffee.
                coffee_maker.make_coffee(order = menu_item)




