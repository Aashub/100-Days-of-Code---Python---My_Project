from tkinter import *

# here we are creating object of windows and defining its attributes & setting the window size.
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=50)
window.config(padx=50, pady= 40)


def convert_ml_km():
    """this function will convert miles into km."""

    miles_value = int(entry.get())
    km_value = round(miles_value * 1.609344, 2)
    converting_value.config(text = km_value)

# here we are creating object of miles and defining its attributes
miles = Label(text="Miles", font=("Arial", 10, "bold"))
miles.config(padx= 10)
miles.grid(row=0, column=2)

# here we are creating object of is_equal_to and defining its attributes
equal_to = Label(text="is equal to", font=("Arial", 10, "bold"))
equal_to.config(padx=10)
equal_to.grid(row=1, column=0)

# here we are creating object of converting_value and defining its attributes
converting_value = Label(text="0", font=("Arial", 10, "bold"))
converting_value.config(pady=5)
converting_value.grid(row=1, column=1)

# here we are creating object of Km and defining its attributes
label = Label(text="Km", font=("Arial", 10, "bold"))
label.grid(row=1, column=2)

# here we are creating object of entry filed and defining its attributes
entry = Entry(width=10)
entry.grid(row=0, column=1)

# here we are creating object of button and defining its attributes and calling the function as well
button = Button(text="Calculate", command=convert_ml_km, font=("Arial", 10, "bold"))
button.grid(row=2, column=1)

window.mainloop()

