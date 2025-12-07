import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# list which will contain all the characters
password_list = []

# in this three for loop we are randomly picking a characters of letters, symbols and numbers and appending them in password_list
for let in range(0, nr_letters):
    password_list.append(random.choice(letters))
for let in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for let in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)

# level 1 of password list project challenge
easy_password = ""

#by using this for loop we are concatenating each character of easy password
for password in password_list:
    easy_password += password

print(easy_password)

# level 2 of password list project challenge
#by using shuffle function we are randomly shuffling all the characters present in the list which will help us to create random strong password.
random.shuffle(password_list)
strong_password = ""

#by using this for loop we are concatenating each character of strong password
for password in password_list:
    strong_password += password

print(strong_password)





