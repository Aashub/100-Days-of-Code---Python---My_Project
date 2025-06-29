import tkinter
from tkinter import *


def calculate():
    """this function will convert the basically miles into km and config the converted value in a result so it gets updated"""
    number = input.get()
    Km = int(number) * 1.60934
    km_result.config(text = int(round(Km, 0)))

# here we are creating a window of GUI
window = Tk()
window.minsize(width=250, height=100)
window.title("Mile to Km Converter")

# this is who we add text in a screen in GUI
is_equal_to = Label(text="is equal to",font=("Roboto",8,"bold"))
is_equal_to.grid(column=0,row=1,padx=15)

# here we are adding a field which will take user input so we can use to convert in into km
input = Entry(width=10,font=("Roboto",8,"bold"))
input.insert(END, string="0")
input.grid(column=1,row=0,pady=10)

km_result = Label(text="0", font=("Roboto", 8, "bold"))
km_result.grid(column = 1, row = 1, pady=4)

# when this button get clicked everytime the calculation function gets triggered and it will call the calculation function
button = Button(text="Calculate", font=("Roboto",8,"bold"), command= calculate)
button.grid(column=1, row=2)

#miles text
miles = Label(text="Miles", font=("Roboto",8,"bold"))
miles.grid(column = 2, row=0,padx=10)

#km text
km = Label(text="Km", font=("Roboto",8,"bold"))
km.grid(column=2, row=1 ,padx=10)


window.mainloop()