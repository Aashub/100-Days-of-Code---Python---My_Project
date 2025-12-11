from art import  logo

def calculator():
    """this function will start the calculator"""
    print(logo)
    output_result = 0

    num1 = float(input("What is the first number?: "))
    should_continue = True

    # the while loop will run until user don't exit the code.
    while should_continue:

        # this four function will do all the calculation and give us the required calculated output
        def add(n1, n2):
            return n1 + n2

        def subtract(n1, n2):
            return n1 - n2

        def multiply(n1, n2):
            return n1 * n2

        def divide(n1, n2):
            return n1 / n2

        # this dictionary store the operators as 'key' and each key stores each operator function so we can use them.
        operator_dictionary = {"+": add,
                               "-": subtract,
                               "*": multiply,
                               "/": divide}

        # this for loop will print all the operator
        for chose_operator in operator_dictionary:
            print(chose_operator)

        selected_operator = input("Pick an operation: ")

        num2 = float(input("What is the next number?: "))

        # Loop through the operator dictionary to find the selected operator.
        # When it matches, call the corresponding function using its key
        # and store the rounded result.
        for operator in operator_dictionary:
            if operator == selected_operator:

                output_result = round(operator_dictionary[operator](num1, num2),2)

        print(f"{num1} {selected_operator} {num2} = {output_result}")

        continue_calculation = input(f"Type 'y' to continue calculating with {output_result}, or type 'n' to start a new calculation or 'exit' to stop: ").lower()

        if continue_calculation == "y":
            num1 = output_result

        elif continue_calculation == "n":
            print("\n" * 20)

            # here we are calling calculator function again using recursion so that new calculation can happen
            calculator()

        elif continue_calculation == "exit":
            exit()

calculator()


