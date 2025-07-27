import json
from tkinter import  *
from tkinter import  messagebox
import random
import  pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():

    """this function will help us to create a random strong password by using list comprehension"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.append([random.choice(letters) for char in range(nr_letters)])
    password_list.append([random.choice(numbers) for char in range(nr_numbers)])
    password_list.append([random.choice(symbols) for char in range(nr_symbols)])

    password_list = ["".join(characters) for characters in password_list]

    password = []
    for char in password_list:
      password += char

    random.shuffle(password)
    password = "".join(password)
    password_field.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """this function will help us in to save data in a data.txt file"""
    website = website_field.get()
    email = email_or_username_field.get()
    password = password_field.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    # if website, email, password field is empty then this if statement will get triggered and we will get a notification
    # to fill the details
    if website_field.get() == "" or email_or_username_field.get() == "" or password_field.get() == "":
        messagebox.showinfo(title= "Oops", message= "Please don't leave any field empty!")


    # if all the details are filled then this condition will run
    else:
        try:
            with open("data.json", "r") as data_file:

                #reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating the old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        # it will clear out the field
        finally:
            website_field.delete(0, "end")
            password_field.delete(0, "end")


# ---------------------------- Find password ------------------------------- #

def find_password():
    """this function will help us out to find out the existing password and other details in data file"""

    # here we are handling an error in case file is not their
    try:
        with open("data.json" , "r") as search_file:
            searched_file = json.load(search_file)


    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:

        searched_website = website_field.get()
        if searched_website == "":
            messagebox.showinfo(title="Oops", message=f"Please don't leave website search field empty.")

        else:
            for data in searched_file:

                if searched_website in searched_file:

                    if searched_website == data:
                        email = searched_file[data]["email"]
                        password = searched_file[data]["password"]
                        messagebox.showinfo(title=data, message=f"Email: {email}\nPassword: {password}")
                        pyperclip.copy(email)
                        pyperclip.copy(password)
                        break

                else:
                    messagebox.showinfo(title="Hmm", message=f"No Details for the {searched_website} exists.")
                    break

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(padx=50, pady= 50)

window.grid()

canvas = Canvas(width=200, height=200, )
lock_image = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image = lock_image)

canvas.grid(row = 0, column = 1)

website_text = Label(text = "Website:")
website_text.grid(row= 1, column = 0, sticky = "w", pady= 1)

email_or_username_text = Label(text = "Email/Username:")
email_or_username_text.grid(row= 2, column = 0, sticky = "w",pady= 1)

password_text = Label(text = "Password:")
password_text.grid(row= 3, column = 0, sticky = "w" ,pady= 1)

website_field = Entry(width=33)
website_field.grid(row= 1, column = 1, sticky = "w",pady= 1)
website_field.focus()

email_or_username_field = Entry(width=52)
email_or_username_field.grid(row= 2, column = 1,  columnspan=2, sticky = "w",pady= 1)
email_or_username_field.insert(0, "ashishbam07@gmail.com")

password_field = Entry(width=33)
password_field.grid(row= 3, column = 1, sticky = "w", pady= 1)


password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row= 3, column = 2,sticky = "e", pady= 1)
password_field.get()

add_button = Button(text="Add", width= 44, command=save)
add_button.grid(row= 4, column = 1, sticky = "w", columnspan=2,pady= 1)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row= 1, column = 2, sticky = "e", pady= 1)

window.mainloop()
