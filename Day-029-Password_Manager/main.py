from tkinter import *
from tkinter import messagebox
import pyperclip

import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """this function will create a password"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # list which will contain all the characters
    password_list = []
    [password_list.append(random.choice(letters)) for letter in range(0, nr_letters)]
    [password_list.append(random.choice(numbers)) for number in range(0, nr_numbers)]
    [password_list.append(random.choice(symbols)) for symbol in range(0, nr_symbols)]


    #by using shuffle function we are randomly shuffling all the characters present in the list which will help us to create random strong password.
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input_field.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """this function will save the password in the txt file."""

    website_name = website_input_field.get()
    email_username =email_username_input_field.get()
    password = password_input_field.get()


    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message= "Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website_name, message= f"These are the details entered: \nEmail: {email_username}"
                                                                f" \nPassword: {password} \nDo you want to say this details?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_name} | {email_username} | {password}\n")

            if email_username != "ashishbam07@gmail.com":
                email_username_input_field.delete(0, "end")
                email_username_input_field.insert(0, "ashishbam07@gmail.com")

            website_input_field.delete(0, "end")
            password_input_field.delete(0, "end")

            website_input_field.focus()

# ---------------------------- UI SETUP ------------------------------- #

FONT = ("Arial", 10, "bold")
BUTTON_FONT = ("Arial", 8, "bold")

# window setup
window = Tk()
window.title("Password Manager")
window.config(width=200, height= 200)
window.resizable(False, False)
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height= 200)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image = logo_img)
timer_text = canvas.create_text(100, 100, font= ("Arial", 25, "bold"))
canvas.grid(row=0, column= 1, sticky="w")


# label, entry input & buttons are setup using the below code.
website_label = Label(text="Website: ", font = FONT)
website_label.grid(row= 1, column=0 , sticky= "w")

website_input_field = Entry(width=39, justify="left", font=FONT)
website_input_field.grid(row=1, column=1, pady=2, columnspan=2, sticky= "w")
website_input_field.focus()

email_username_label = Label(text="Email/Username: ", font = FONT)
email_username_label.grid(row= 2, column=0 , sticky= "w")

email_username_input_field = Entry(width=39, justify="left", font=FONT)
email_username_input_field.grid(row=2, column=1,pady=2, columnspan=2, sticky= "w")
email_username_input_field.insert(0, "anony@@gmail.com")

password_label = Label(text="Password: ", font = FONT)
password_label.grid(row= 3, column=0 , sticky= "w")

password_input_field = Entry(width=21, font=FONT)
password_input_field.grid(row=3, column=1, columnspan=2, pady=2, sticky= "w")

generate_pass_button = Button(text="Generate Password", font = BUTTON_FONT, command = generate_password)
generate_pass_button.place(x = 274, y = 252)


add_button = Button(text="Add", width= 38, font = BUTTON_FONT, command= save)
add_button.grid(row=4, column=1, columnspan=2,pady= 2,  sticky= "w")

window.mainloop()