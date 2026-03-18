# Day 59 – Upgraded Simple Blog Website with Bootstrap

## Project Overview

This is a dynamic blog website built using Flask that fetches blog post data from an external API and renders it using a professional Clean Blog template from StartBootstrap. The website features multiple pages including Home, About, Contact, and individual blog post pages. When users click on any blog title or subtitle on the home page, they are taken to a dedicated page displaying the full blog post content including title, subtitle, author, date, and body. The project demonstrates Flask routing, URL building with url_for(), Jinja templating for dynamic content, API integration, and template inheritance using reusable components like header and footer.

## What I Have Learned

* **Flask Routing with Multiple Routes**: Revised about how to create different routes in a Flask application including dynamic routes with variable rules. The project uses routes (/) for rendering home page ,& different static pages by using `(/<string:page>)`, and individual blog posts for `(/<int:num>)`.

* **URL Building with url_for()**: Revised about Flask's `url_for()` function to dynamically generate URLs based on function names rather than hardcoding them. Used extensively in navigation links (url_for('show_page', page='home')) and blog post links (url_for('show_blog', num=post.id)). This makes the application more maintainable because if route paths change, all links automatically update.

* **Jinja Templating**: Understood Jinja's powerful templating syntax including `{% include %}` for template reuse, `{% for %}` loops for iterating through blog posts, `{% if %}` conditions for conditional rendering, and `{{ variables }}` for outputting dynamic content. The header and footer are reused across all pages using `{% include "header.html" %}` and `{% include "footer.html" %}`.

* **Static File Management in Flask**: Learned how to properly serve static files (CSS, JavaScript, images) in Flask using the url_for('static', filename='path') function. This ensures correct file paths regardless of the application's root URL and follows Flask conventions.

* **API Integration with requests**: Revised about using the Python requests library. The application makes a GET request to an npoint.io API endpoint at the start, retrieves JSON data containing blog posts, and stores it globally to be used across different routes.

* **Dynamic Routing with Variable Rules**: Implemented dynamic routes using `<string:page>` to handle multiple static pages (home, about, contact) with a single function `show_page()`, and `<int:num>` to capture blog post IDs from URLs like /1, /2, /3 for displaying individual posts.

## How It Works

* **`main.py`**: The Flask application starts by creating a Flask instance and fetching blog data from the `npoint.io` API using `requests.get()`, storing the JSON response in the global `blog_data` variable. The `@app.route('/')` decorator handles the home page by rendering `index.html` and passing the complete `blog_data` variable so that in index.html file it get used by jinja template to show blog title & other things. The `@app.route('/<string:page>')` route handles static pages by checking the `page` parameter if `home` is passed, it renders `index.html` with `blog data`; if `about` or `contact` is passed, it renders `about.html` or `contact.html` respectively. The `@app.route('/<int:num>')` route handles individual blog posts by capturing the `post ID` from the URL and passing both the complete `blog_data` and the specific post number to `post.html` for rendering the correct article.

* **`header.html`**: This file contains the website's head section with all meta tags, Font Awesome icons via CDN, Google Fonts (Lora and Open Sans), and the core Bootstrap theme CSS linked using `{{ url_for('static', filename='css/styles.css') }}`. The navigation bar is built with Bootstrap classes and uses `url_for()` method for all navigation links like Home, About, Contact menu items all call show_page with appropriate page parameters. This ensures consistent navigation across the entire site.

* **'`index.html`'**: The home page template includes the header and footer using Jinja's {% include %} statements. The main content area uses a Jinja for loop ({% for post in all_blog_post %}) to iterate through all blog posts fetched from the API. For each post, it displays the title and subtitle wrapped in an anchor tag that uses {{ url_for('show_blog', num=post.id) }} to create a link to the individual post page. Below each post, it shows the author name and publication date using {{ post.author }} and {{ post.date }} variables.

* **`post.html`**: This template renders individual blog posts and includes both header and footer. It uses a nested Jinja structure, a for loop iterates through all blog posts, but an inner if statement `({% if post.id == post_num %})` checks if the current blog_post ID matches the `post_num` variable passed from the route when show_blog(`num`) function get called. When a match is found, it displays the blog post title in an h1 tag, subtitle in an h2 tag, author and date in the meta section, and the full blog body in a paragraph tag. This conditional rendering ensures only the requested post is displayed when user clicks on the title and subtitle.

* **`about.html & contact.html`**: These static pages follow a similar structure they include header and footer, have their own masthead images (about-bg.jpg and contact-bg.jpg), and contain static content. The contact page includes a comprehensive contact form with fields for name, email, phone, and message, though the form is currently pre-integrated with SB Forms and requires an API token to function.

* **`footer.html`**: The footer is included at the bottom of every page and contains social media icons (Twitter, Facebook, GitHub) using Font Awesome, a copyright notice, and all the JavaScript files that make the website work, including the Bootstrap javascript bundle and the core theme JavaScript file linked using `{{ url_for('static', filename='/js/scripts.js') }}`. By placing all these script links in one footer file, we centralize them in a single place instead of repeating them on every page.

## Project Highlights

* **Multiple Route Handling**: Created different routes for home page, static pages, and dynamic blog posts, demonstrating Flask's flexible routing system.
* **URL Building with url_for()**: Used Flask's `url_for()` function throughout the project for all links, making the application more maintainable and robust. 
* **Jinja Templating**: MasteredLearned to use Jinja's tags like {% include %} to reuse headers and footers, {% for %} loops to display multiple blog posts automatically, {% if %} conditions to show content selectively, and {{ variables }} to insert dynamic data like post titles from Python into HTML.
* **Template Reusability**: Implemented reusable header and footer components using {% include %} to avoid code duplication across multiple pages.
* **Dynamic Routing**: Used variable rules to capture string page names and integer post IDs from URLs for flexible content delivery.
* **Static File Management**: Properly organized and served CSS, JavaScript, and images using Flask's static folder with url_for() for correct path resolution.




