# Day 57 – Simple Blog Website

## Project Overview

This is a dynamic blog website built using Flask that fetches blog post data from an external API and renders it beautifully on the frontend. The website consists of a home page displaying all blog post titles and subtitles, and individual post pages that show the full content when users click the "Read" link. Built with Flask, the application demonstrates how to integrate external APIs, use Jinja templating for dynamic content rendering, In order to build this project i learend about url building and templating with jinja in your flask application also I learned about how i can write python code inside the html file using jinja.

## What I Have Learned

* **URL Building with url_for()**: Learned how to dynamically generate URLs in Flask using the url_for() function. In the index.html template, {{ url_for('get_post', num=1) }} creates a URL that maps to the get_post view function with the parameter num=1. This is a powerful feature that generates URLs based on function names rather than hardcoding them, making the application more maintainable and flexible.
* **Templating with Jinja in Flask**: Learned Jinja templating syntax to create dynamic HTML pages. Learned to use {{ variables }} to insert dynamic content, {% for %} loops to iterate through blog posts, and {% if %} conditions to display specific content. The post.html template demonstrates complex Jinja usage by looping through all blog posts and conditionally displaying only the one which user has wanted.
* **Data Passing from Flask to Templates**: Learned how to pass Python data structures (like lists of dictionaries) to HTML templates using the syntax render_template("index.html", blog=blog_data). This allows templates to access and display dynamic content.

## How It Works

* **`@app.route('/') & home() function`**: This route handles the home page. The home() function makes a GET request to the blog API using requests.get(), converts the response to JSON, and passes this data to index.html using render_template("index.html", blog=blog_data).
* **`index.html template`**: The home page displays all blog posts by accessing the passed blog data. Each post has a "Read" link that uses {{ url_for('get_post', num=1) }} to dynamically generate the URL for that specific post.
* **`@app.route('/post/<num>') & get_post(num) function`**: This dynamic route captures the post ID from the URL (like 2 from /post/2). When a user clicks "Read" on a post, the get_post() function receives that ID number, fetches all blog data from the API, and sends both the complete blog data and the specific post number to post.html so it can display the correct article.
* **`post.html template`**: This template uses Jinja's {% for %} loop to iterate through all blog posts. Inside the loop, an {% if %} statement checks {% if blog_post["id"] == post_num %} to find and display only the post that matches the requested ID of blog post.
* **`URL Building with url_for()`**: The url_for('get_post', num=1) function generates the correct URL for the get_post view function. This is more maintainable than hardcoding URLs because if the route path ever changes, all links automatically update.

## Project Highlights

* Used Flask's url_for() function to dynamically generate URLs, making the application more maintainable and following Flask best practices.
* Learned how ot use Jinja's template syntax including variable output, for loops, and if conditions to create dynamic, data-driven web pages.




