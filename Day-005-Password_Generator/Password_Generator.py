import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#in this list i will append all the characters
password_list = []

# this string will concatenate each password characters
seq_password = ""
strg_password = ""

# this three for loop will give us random character from the numbers, letter and symbol list
# and assign them in a password list
for letter in range(0, nr_letters):
    let = random.choice(letters)
    password_list.append(let)

for number in range(0, nr_numbers):
    num = random.choice(numbers)
    password_list.append(num)

for symbol in range(0, nr_symbols):
    sym = random.choice(symbols)
    password_list.append(sym)

#this loop will perform the string concatenation of password_list
for password in password_list:
    seq_password += password
print("The Sequence Password: ")
print(f"{seq_password}\n")

strong_password = []

# this for loop will create strong password which will be random
for rand in range(0, nr_symbols + nr_numbers + nr_letters):
    password = random.choice(password_list)
    strong_password.append(password)

# here string concatenation of strong password will happen
for password in strong_password:
    strg_password += password

print("the Strong Password: ")
print(f"{strg_password}")


