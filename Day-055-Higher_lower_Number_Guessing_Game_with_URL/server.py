from flask import Flask
import random

app = Flask(__name__)

def make_header(func):
    "this decorator function is used to decorate the title and show image as per the user answer."

    def wrapper(*args, **kwargs):
        title, number_image = func(*args, **kwargs)

        return (f"<h1> {title} </h1>\n"
                f"<img src={number_image}>")

    wrapper.__name__ = func.__name__
    return wrapper

@app.route('/')
@make_header                       # at this point of time wrapper function get called inside flask & when this get called the function which is inside the wrapper function get called
def home_page():
    return "Guess a number between 0 and 9", "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"

# generating random number between 0 to 9
random_num = random.randint(0, 9)

@app.route("/<int:number>")
@make_header                        # at this point of time wrapper function get called inside flask & when this get called the function which is inside the wrapper function get called
def guess_the_number(number):
    """this function will check which number is greater, lesser or equal to the random number."""

    if random_num < number: # if guess is higher
        return f"{number} too high,Try again!", "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"

    elif random_num > number: # if guess is lower
        return f"{number} too low,Try again!", "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"

    elif random_num == number: # if correct guess
        return f"You found me!", "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

if __name__ == "__main__":
    app.run(debug=True, port=5001)

