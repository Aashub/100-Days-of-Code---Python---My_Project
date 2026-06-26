from morse_code import morse_code_dict

morse_code_key = [each_key for each_key in morse_code_dict]


def converting_text_to_morse(text):
    """this function convert the plain text into morse code and return the morse code in the form of string"""

    morse_code = ''
    uppercase_text = text.upper()

    for letter in uppercase_text:    # this for loop concatenate white_space, letter, dict, number in a single string.

        if letter in morse_code_dict:
            morse_code += morse_code_dict[letter] + " "

    return morse_code


def enter_user_input():
    """this function is used for plain text user input."""

    txt_input = input("Enter the Plain Text: ")

    return txt_input

def asking_quit_program():
    """this function is used for asking user to quit the program."""

    quit_program = ""

    while quit_program not in ["y", "n"]:
        quit_program = input("Do you want to exit? (y/n): ").lower()
        if quit_program not in ["y", "n"]:
            print('Please enter a valid input between y/n\n')

    return quit_program

text_input = enter_user_input()

should_continue = True
while should_continue:    # loop will continue until the should_continue condition doesn't become false

    if len(text_input) > 0:
        converted_morse_code = converting_text_to_morse(text_input)  # function calling
        print(f'\nEntered Text: {text_input}\nMorse Code: {converted_morse_code}\n')

    elif len(text_input) == 0:
        pass

    quit_prog = asking_quit_program()   # function calling

    if quit_prog == 'y':
        should_continue = False

    elif quit_prog == 'n':
        text_input = enter_user_input()  # function calling
