# Day 59-60 – Upgraded Simple Blog Website with Bootstrap

## Project Overview

This is an upgraded dynamic blog website built using Flask that fetches blog post data from an external API and renders it using a professional Clean Blog template from StartBootstrap. The website features multiple pages including Home, About, Contact, and individual blog post pages. When users click on any blog title or subtitle on the home page, they are taken to a dedicated page displaying the full blog post content including title, subtitle, author, date, and body. The project now includes a fully functional contact form that captures user input (name, email, phone, message) and sends an email notification using Python's smtplib module. The project demonstrates Flask routing, URL building with url_for(), Jinja templating for dynamic content, API integration, template inheritance, and form handling with POST requests.

## What I Have Learned

* **Flask Routing with Multiple Routes**: Revised about how to create different routes in a Flask application including dynamic routes with variable rules. The project uses routes (/) for rendering home page ,& different static pages by using `(/<string:page>)`, and individual blog posts for `(/<int:num>)`.

* **URL Building with url_for()**: Revised about Flask's `url_for()` function to dynamically generate URLs based on function names rather than hardcoding them. Used extensively in navigation links (url_for('show_page', page='home')) and blog post links (url_for('show_blog', num=post.id)). This makes the application more maintainable because if route paths change, all links automatically update.

* **Jinja Templating**: Understood Jinja's powerful templating syntax including `{% include %}` for template reuse, `{% for %}` loops for iterating through blog posts, `{% if %}` conditions for conditional rendering, and `{{ variables }}` for outputting dynamic content. The header and footer are reused across all pages using `{% include "header.html" %}` and `{% include "footer.html" %}`.

* **Static File Management in Flask**: Learned how to properly serve static files (CSS, JavaScript, images) in Flask using the url_for('static', filename='path') function. This ensures correct file paths regardless of the application's root URL and follows Flask conventions.

* **API Integration with requests**: Revised about using the Python requests library. The application makes a GET request to an npoint.io API endpoint at the start, retrieves JSON data containing blog posts, and stores it globally to be used across different routes.

* **Dynamic Routing with Variable Rules**: Implemented dynamic routes using `<string:page>` to handle multiple static pages (home, about, contact) with a single function `show_page()`, and `<int:num>` to capture blog post IDs from URLs like /1, /2, /3 for displaying individual posts.

* **Form Handling with POST Requests**: Learned how to handle form submissions in Flask by adding `methods=["GET", "POST"]` to routes and using `request.method` to check the request type. When a POST request is detected, the form data is extracted using `request.form['field_name']` where the field name matches the name attribute in HTML input fields.

## How It Works

* **`main.py`**: The Flask application starts by importing necessary modules and loading email credentials from environment variables using `os.environ["email"]` and `os.environ["password"]`.Than It fetches blog data from the `npoint.io` API using `requests.get()` and stores the JSON response in the global `blog_data` variable. Than a send_mail() function created  when it gets called it creates a secure connection with Gmail's SMTP server using SMTP(smtp_server, smtp_port), starts TLS encryption with starttls(), logs in using the credentials, and sends an email with the formatted message data. The `@app.route('/')` decorator handles the home page by rendering index.html and passing the complete blog_data. The `@app.route('/<string:page>', methods=["GET","POST"])` route handles both displaying static pages and processing form submissions when a POST request is received from the contact form, it extracts name, email, phone, and message from `request.form[]`, formats them into a string, Than it calls `send_mail()` to email the data, and re-renders `contact.html` with a successful_msg variable set to "successful" to show confirmation. The `@app.route('//<int:num>')` route handles individual blog posts by capturing the `post ID` from the URL and passing both `blog_data` and the specific post number to `post.html`.

* **`header.html`**: This file contains the website's head section with all meta tags, Font Awesome icons via CDN, Google Fonts (Lora and Open Sans), and the core Bootstrap theme CSS linked using `{{ url_for('static', filename='css/styles.css') }}`. The navigation bar is built with Bootstrap classes and uses `url_for()` method for all navigation links like Home, About, Contact menu items all call show_page with appropriate page parameters. This ensures consistent navigation across the entire site.

* **'`index.html`'**: The home page template includes the header and footer using Jinja's `{% include %}` statements. The main content area uses a Jinja for loop `({% for post in all_blog_post %})` to iterate through all blog posts fetched from the API. For each post, it displays the title and subtitle wrapped in an anchor tag that uses `{{ url_for('show_blog', num=post.id) }}` to create a link to the individual post page. Below each post, it shows the author name and publication date using `{{ post.author }}` and `{{ post.date }}` variables.

* **`post.html`**: This template renders individual blog posts and includes both header and footer. It uses a nested Jinja structure, a for loop iterates through all blog posts, but an inner if statement `({% if post.id == post_num %})` checks if the current blog_post ID matches the `post_num` variable passed from the route when `show_blog(num)` function get called. When a match is found, it displays the blog post title in an h1 tag, subtitle in an h2 tag, author and date in the meta section, and the full blog body in a paragraph tag. This conditional rendering ensures only the requested post is displayed when user clicks on the title and subtitle.

* **`about.html`**:  This static page includes header and footer, has its own masthead image (about-bg.jpg), and contains static lorem ipsum text about the blog author.

* **`contact.html`**: the contact.html file includes dynamic heading behavior using Jinja conditional statements this condition came out true than`{% if successful_msg == "successful" %}` it displays "Successfully sent message" as the heading when an email is successfully sent, while `{% elif successful_msg != "successful" %}` came true than it  displays "Contact Me" as the default heading. In this file their is a form section where form uses `action="{{url_for('show_page', page='contact')}}"` `method="post"` to submit data back to the same route. Each input field has a name attribute (name, email, phone, message) that matches the keys used in `request.form[]` in main.py. when user clicks on the submit button after filling all the details it sends the message to the person.

* **`footer.html`**: The footer is included at the bottom of every page and contains social media icons (Twitter, Facebook, GitHub) using Font Awesome, a copyright notice, and all the JavaScript bundle and the core theme JavaScript file linked using `{{ url_for('static', filename='js/scripts.js') }}`. By placing all these script links in one footer file, we centralize them in a single place instead of repeating them on every page.

## Project Highlights

* **Multiple Route Handling**: Created different routes for home page, static pages, and dynamic blog posts, demonstrating Flask's flexible routing system.
* **URL Building with url_for()**: Used Flask's `url_for()` function throughout the project for all links, making the application more maintainable and robust. 
* **Jinja Templating**: Learned to use Jinja's tags like `{% include %}` to reuse headers and footers, `{% for %}` loops to display multiple blog posts automatically, `{% if %}` conditions to show content selectively, and `{{ variables }}` to insert dynamic data like post titles from Python into HTML.
* **Template Reusability**: Implemented reusable header and footer components using `{% include %}` to avoid code duplication across multiple pages.
* **Dynamic Routing**: Used variable rules to capture string page names and integer post IDs from URLs for flexible content delivery.
* **Static File Management**: Properly organized and served CSS, JavaScript, and images using Flask's static folder with url_for() for correct path resolution.
* **Functional Contact Form**: Added a fully working contact form that captures user input and sends email notifications using smtplib module.
* **POST Request Handling**: Added POST method handling to the contact route to process form submissions and extract data using request.form[].






