# Day 56 – Name Card Website with Flask

## Project Overview

This is a personal name card website built using Flask and a pre-designed HTML5 template. The project serves as a simple yet elegant personal landing page that displays a profile picture, name, title, and social media links. Built with Flask, the application renders a static HTML template with proper CSS styling and demonstrates how to serve static files (images, CSS, JavaScript) in a Flask application. The website features a clean, professional design with a minimalistic theme which includes links of  Twitter, Instagram, and Facebook page links in order to complete this challenge i have learned about static files, html, css file rendering.

## What I Have Learned

* **Static Files**: Learned how to serve static files (CSS, JavaScript, images) in a Flask application. Understood that in order to work with flask i nee to store the files such as css, images, javascript needs to be stored inside the the static folder/directory in order to work with otherwise the css styling, images and javascript will not get implemented in front end. 
* **HTML and CSS File Rendering**: Learned the process of rendering HTML templates using Flask's render_template() function. The render_template("index.html") call looks for HTML files inside a templates folder and renders them with the Jinja2 templating engine. This project showed me how to integrate pre-designed HTML5 templates with Flask backend.
* **Personal Website Development**: Built a personal landing page that serves as an online identity card. The site includes a profile avatar, name, professional title, and social media links & all essential elements of a personal website. while building this website also taught me how to customize existing templates.

## How It Works

* **`server.py`**: app = Flask(__name__) Creates a new Flask web application instance that helps Flask locate resources like templates and static files relative to the current module. @app.route('/') decorator is used calling home function and root url, When users visit the home page, the home() function calls render_template("index.html") which locates and renders the HTML file from the templates folder.
* **`Static File Serving`**: The HTML file referenced towards using paths like static/assets/css/main.css and static/images/avatar.jpg. so all the javascript functionality, css styling and image rendering process happens without any issue, Flask automatically serves any files placed in the static folder when these URLs are requested.
* **HTML Template Structure**: When home function call the index.html file which is located in templates folder/directory it renders the complete HTML5 template that includes a profile avatar image, a name heading ("Asteroid Destroyer"), a professional title, and social media icons with working links to Twitter, Instagram, and Facebook profiles.

## Project Highlights

* learned & successfully implemented flask static file handling where we need to store images, css and javascript in the static folder if we need to work with this file. 
* learned that in order to work with html templates i need to store html template file in a templates name folder because flask don't allow us to work with html file otherwise
* Also learned that I can find and replace the specific path in html file using pycharm in built function.

