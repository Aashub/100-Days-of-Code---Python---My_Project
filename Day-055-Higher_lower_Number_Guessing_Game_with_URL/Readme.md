# Day 55 – Higher-Lower Number Guessing Game with URL

## Exercise Overview

This is a simple yet interactive number guessing game built using Flask. The web application generates a random number between 0 and 9, and users can guess the number by typing it directly in the URL (e.g., http://127.0.0.1:5001/5). The app responds with a fun, color-coded HTML page that tells users whether their guess is too high, too low, or correct—complete with matching GIFs from GIPHY. in order th build this project i have learned about advanced decorators, rendering html, variable paths, parsing urls, flask debugging.

## What I Have Learned

* **Advanced Decorators**: Learned how to create custom decorators like @make_header that wrap functions to add additional functionality. In this project, the decorator takes the return values from route functions (a title string and an image URL) and formats them into proper HTML with heading tags and image embedding. This taught me how decorators can modify function outputs without changing the original function code.
* **Flask Routing with @app.route()**: Understood how to create different routes in a Flask application. The root route (/) displays the home page with instructions, while the dynamic route (/<int:number>) captures user guesses from the URL.
* **Variable Paths and Type Conversion**: Learned how to define variable paths in URLs using <int:number> syntax. This automatically converts the captured URL segment to an integer data type, eliminating the need for manual type conversion and providing built-in validation.
* **Parsing URLs**: Understood how Flask parses URL segments and passes them as arguments to view functions. When a user visits http://127.0.0.1:5001/7, Flask extracts "7" from the URL, converts it to an integer, and passes it to the guess_the_number() function as the number parameter.
* **Rendering HTML Dynamically**: Learned to generate HTML on-the-fly by returning strings containing HTML tags. The @make_header decorator takes plain text responses and wraps them in proper HTML structure with heading tags and image elements, demonstrating how to create dynamic web content without using template files.
* **Flask Debugging**: Learned about the flask debugging mode that after we set the debug=True mode in app.run() this thing enables Auto-reloading of the server when code changes so after when we change the code we just need to save it and and reload the page and the changes get reflected.

## How It Works

* **`@app.route('/')`**: This route handles the home page. When users visit the root URL, the home_page() function returns a title string "Guess a number between 0 and 9" and a thinking GIF URL, which the @make_header decorator formats into HTML when get called.
* **`make_header(func)`**: This advanced decorator function wraps route functions that return two values (a title string and an image URL). than It calls the original function, which captures both return values, and formats them into a complete HTML string with an `<h1>` heading and an `<img>` tag before sending to the browser.
* **Random Number Generation**: When the Flask application starts, it generates a random integer between 0 and 9 using random.randint(0, 9) and stores it globally. This number persists throughout the server session until the server restarts.
* **`@app.route("/<int:number>")`**: This dynamic route captures user guesses from the URL. The <int:number> syntax automatically extracts the URL segment, converts it to an integer, and passes it to the guess_the_number() function.
* **`guess_the_number(number)`**: This function contains the main game logic. It compares the user's guess with the random number and returns appropriate messages and GIF URLs too high, too low, or correct if guess is correct, which are then formatted by the @make_header decorator.
* **Application Entry Point**: The `if __name__ == "__main__":` block ensures the Flask development server only runs when the script is executed directly, not when imported as a module.

## Project Highlights

* **Custom decorator**: learned about a custom decorator and how to create them & how they work.
* **Dynamic URL Routing**: Learned and implemented  both static (/) and dynamic (/<int:number>) routes to handle different types of requests
* **Variable Path**: Learned about the variable path that we can pass the variable path in the url in the format of str, integer, float values.
* **Flask Debug Mode**: Leveraged Flask's debug features for development efficiency & auto reloading which saves time, and the interactive debugger helps identify issues quickly.
