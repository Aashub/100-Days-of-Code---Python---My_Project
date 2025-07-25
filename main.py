from tkinter import  *
from tkinter import  messagebox
import random
import pyperclip
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
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """this function will help us in to save data in a data.txt file"""

    #by using to .get() function we can extract that particular field actual value
    filled_data = website_field.get() + " | " + email_or_username_field.get() + " | " + password_field.get()

    # if website, email, password field is empty then this if statement will get triggered and we will get a notification
    # to fill the details
    if website_field.get() == "" or email_or_username_field.get() == "" or password_field.get() == "":
        messagebox.showinfo(title= "Oops", message= "Please don't leave any field empty!")

    # if all the details are filled then this condition will run
    else:

        with open("data.txt", "a") as file:
            file.write(f"{filled_data}\n")

        #this messagebox will show the field details this will show the pop up so customer
        # can decide if he wants to make any changes or not in the field details.
        is_oky = messagebox.askokcancel(title= "Website", message= f"These are the details entered: \n\nWebsite: {website_field.get()}"
                                                                          f"\nEmail: {email_or_username_field.get()}\n"
                                                                          f"Password: {password_field.get()}\n\n Is it oky to save?")

        # this part will clear out the field which was being filled up so next time password and other details will get
        # filled
        if is_oky:
            website_field.delete(0, "end")
            email_or_username_field.delete(0, "end")
            password_field.delete(0, "end")



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
website_text.grid(row= 1, column = 0, sticky = "w")

email_or_username_text = Label(text = "Email/Username:")
email_or_username_text.grid(row= 2, column = 0, sticky = "w")

password_text = Label(text = "Password:")
password_text.grid(row= 3, column = 0, sticky = "w")

website_field = Entry(width=52)
website_field.grid(row= 1, column = 1,  columnspan=2, sticky = "w")
website_field.focus()

email_or_username_field = Entry(width=52)
email_or_username_field.grid(row= 2, column = 1,  columnspan=2, sticky = "w")
email_or_username_field.insert(0, "ashishbam07@gmail.com")

password_field = Entry(width=33)
password_field.grid(row= 3, column = 1, sticky = "w")


password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row= 3, column = 2)
password_field.get()
add_button = Button(text="Add", width= 44, command=save)
add_button.grid(row= 4, column = 1, sticky = "w", columnspan=2)

window.mainloop()