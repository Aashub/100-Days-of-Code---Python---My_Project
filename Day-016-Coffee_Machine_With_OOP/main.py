from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#here we have created object and their classes.
coffee_item = Menu()
start_coffee_machine = CoffeeMaker()
to_get_profit = MoneyMachine()


should_continue = True

while should_continue:
    # loop will run until user don't decide to turn off the machine.

    select_coffee =  input(f"What would you like? {coffee_item.get_items()}: ").lower()

    if select_coffee == "off":
        should_continue = False

    elif select_coffee == "report":

        # by using this two methods we can get the details of how much current resource and profit we had in machine
        start_coffee_machine.report()
        to_get_profit.report()


    elif select_coffee == "espresso" or select_coffee == "latte" or select_coffee == "cappuccino":

        # find drink method will give us the Menu_item object by the name of *Drink* by searching all three Menu.
        Drink = coffee_item.find_drink(order_name=select_coffee)
        
        # this method will check that the resources is sufficient or not to make the coffee 
        if start_coffee_machine.is_resource_sufficient(drink=Drink):

            # this method will check that user has provided enough money or not if not then if will give us prompt to 
            # provide enough money to make a coffee
            if to_get_profit.make_payment(cost= Drink.cost):
                
                # this final method then finally makes a coffee and deduct all necessary resources to make a coffee
                start_coffee_machine.make_coffee(order = Drink)




        









