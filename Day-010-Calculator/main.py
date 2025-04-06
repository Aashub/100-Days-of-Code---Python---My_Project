from art import logo

"""this function will start the Calculator"""
def start_calculator():

    print(logo)

    def add(num1, num2):
        sum = num1 + num2
        print(f"{num1} + {num2} = {sum}")
        return sum

    def subtract(num1,num2):
        sub = num1 - num2
        print(f"{num1} + {num2} = {sub}")
        return sub

    def multiply(num1,num2):
        mul = num1 * num2
        print(f"{num1} + {num2} = {mul}")
        return mul

    def divide(num1,num2):
        div = num1 / num2
        print(f"{num1} + {num2} = {div}")
        return div

    calculation_operators = {"+": add,
                            "-": subtract,
                            "*": multiply,
                            "/": divide
                            }

    #to stop avoiding unbound local variable error, passed a variable in
    # a restart_calculator function so don't get error
    n1 = float(input("What's the First number? :"))

    """This function will restart the Calculator """
    def restart_calculator(n1):

        #this for loop will print out operators which we want to perform
        for to_print_operators in calculation_operators:
            print(to_print_operators)

        operations = input("Pick an Operation: ")
        n2 = float(input("What's the next number? :"))

        #here from dictionary 'key' which are operators are being checked that which calculation operation
        #user wants to perform and as per that operation will be performed.
        for operator in calculation_operators:
            if operations == operator:

                #here we are accessing function operators like(func add) and also giving them the value
                #to perform on which number they should perform calculation.
                calc_result  = calculation_operators[operator](n1, n2)

                """here if the user gives the wrong input then this while loop runs until the user don't provide
                the correct input"""
                correct_user_input = True
                while correct_user_input:
                    continue_calculation = input(f"Type 'y' to continue calculating with {calc_result} "
                                                f"or type 'n' to start a new calculation or type 'exit' to "
                                                 f"exit the program:").lower()

                    if continue_calculation == "y":
                        #here calculated value is being assigned to n1 variable
                        n1 = calc_result
                        restart_calculator(n1)

                    elif continue_calculation == "n":
                        print("\n" * 17)
                        start_calculator()

                    elif continue_calculation == "exit":
                        print("Good Bye!")
                        exit()

                    else:
                        print("Invalid Input, Please Provide correct Input!\n")

    restart_calculator(n1)
    
start_calculator()










