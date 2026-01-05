from tkinter import *

FONT = ("Arial", 10, "bold")

km_text = "Km"
Miles_text = "Miles"

# here we are creating object of windows and defining its attributes & setting the window size.
window = Tk()
window.resizable(False, False)
window.title("Mile to Km Converter")
window.minsize(width=200, height=50)
window.config(padx=70, pady= 40)


def unit_converter():
    """this function will convert miles into km & km into miles."""

    # it will prevent the previous text alignment & color of wrong input to the custom alignment which we have done initially.
    if entry.get():
        converting_value.config(text="Invalid input", fg="black")
        converting_value.grid(sticky="w")

    try:
        if Miles_text == "Miles" and km_text == "Km":

            miles_value = float(entry.get())
            km_value = round(miles_value * 1.609344, 2)
            converting_value.config(text = km_value)

        elif Miles_text == "Km" and km_text == "Miles":
            km_value = float(entry.get())
            miles_value = int(round(km_value / 1.609344))
            converting_value.config(text=miles_value)

    except ValueError:
        converting_value.config(text="Invalid input", fg= "red")
        converting_value.grid(sticky= "")


def unit_switcher():
    """this function will switch units of Km and miles"""

    # it will prevent the previous text alignment & color of wrong input to the custom alignment which we have done initially.

    global km_text, Miles_text

    converting_value.config(text="0", fg= "black")
    converting_value.grid(sticky="w")
    entry.delete(0, "end")

    if km_text == "Km" and Miles_text == "Miles":

        miles.config(text="Km")
        km.config(text="Miles")
        km_text = "Miles"
        Miles_text = "Km"

    elif km_text == "Miles" and Miles_text == "Km":

        miles.config(text="Miles")
        km.config(text="Km")
        km_text = "Km"
        Miles_text = "Miles"



# here we are creating object of miles and defining its attributes
miles = Label(text="Miles", font = FONT)
miles.config(padx= 7)
miles.grid(row=0, column=2, sticky= "w")

# here we are creating object of is_equal_to and defining its attributes
equal_to = Label(text="is equal to", font = FONT)
equal_to.config(padx=10)
equal_to.grid(row=1, column=0)

# here we are creating object of converting_value and defining its attributes
converting_value = Label(text=0, font = FONT,)
converting_value.config(pady= 5)
converting_value.grid(row=1, column= 1, sticky= "w")


# here we are creating object of Km and defining its attributes
km = Label(text="Km", font = FONT)
km.grid(row=1, column=2, padx= 7, sticky= "w")

# here we are creating object of entry filed and defining its attributes
entry = Entry(width=14, justify="left", font=FONT)
entry.grid(row=0, column=1)


# here we are creating object of button and defining its attributes and calling the function as well
calculate_button = Button(text="Calculate", width= 12, command=unit_converter, font = FONT)
calculate_button.grid(row=2, column=1, sticky= "w")

switch_button = Button(text="🔄", font = ("Segoe UI", 13, "bold"), command = unit_switcher)
switch_button.place(x= 250, y = 4)



window.mainloop()
