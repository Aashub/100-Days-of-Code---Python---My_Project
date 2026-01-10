from tkinter import *
import pandas
import random

# this try except block will check that words_to_learn.csv file exist or not if not than it will run the already existing telugu words existing file.
try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_data = pandas.read_csv("data/telugu words.csv")
finally:
    words_list = words_data.to_dict(orient="records")

print(len(words_list))

# constants
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FRONT = ("Arial", 30, "italic")
WORD_FONT = ("Arial", 50, "bold")

def card_flipped(random_word):
    """after every three seconds this function will get called and show the translated english version of telugu words"""

    canvas.itemconfig(card_background, image = back_image)
    canvas.itemconfig(title_text, text=f"English", fill="white")
    canvas.itemconfig(word_text, text=f"{random_word["English"]}", fill="white")

def update_words(rand_word):
    """this function will help in display the telugu words everytime right button or wrong button got clicked"""

    canvas.itemconfig(title_text, text=f"Telugu", fill="black")
    canvas.itemconfig(word_text, text=f"{rand_word["Telugu"]}", fill="black")
    canvas.itemconfig(card_background, image=front_image)

def right_button_clicked():
    """this function will remove every known words of the user and create a new list of words_to_learn so when user come back again it will start learning from the rest of learning words."""

    global flip_timer, words_list, to_learn_list
    window.after_cancel(flip_timer)
    current_word = random.choice(words_list)

    update_words(current_word)
    if current_word in words_list:
        words_list.remove(current_word)
        print(len(words_list))
        df = pandas.DataFrame(words_list)
        df.to_csv("data/words_to_learn.csv", index=False)

    flip_timer = window.after(3000, card_flipped, current_word)

def wrong_button_clicked():
    """this function will skip to next word everytime it get clicked so that user can check that new word he knows or not."""

    global flip_timer, words_list
    window.after_cancel(flip_timer)
    current_word = random.choice(words_list)

    update_words(current_word)
    flip_timer = window.after(3000, card_flipped, current_word)


# window setup
window = Tk()
window.title("Flashy")
window.resizable(False, False)
window.config(bg= BACKGROUND_COLOR, padx= 50, pady= 50)

flip_timer = window.after(3000, card_flipped)
start_word = random.choice(words_list)

# flash card setup.
canvas = Canvas(width=800, height= 526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image = front_image)
title_text = canvas.create_text(400, 150, text=f"Telugu", font= TITLE_FRONT)
word_text = canvas.create_text(400, 263, text=f"{start_word["Telugu"]}", font= WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column= 0, columnspan= 2)

# button setup
right_image = PhotoImage(file= "images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command= right_button_clicked)
right_button.grid(row=1, column= 0)

wrong_image = PhotoImage(file= "images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command= wrong_button_clicked)
wrong_button.grid(row=1, column= 1)

window.mainloop()

