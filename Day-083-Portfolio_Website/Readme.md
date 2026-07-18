# Day 83 – Portfolio Website

## Project Overview

This is a personal portfolio website built with Flask that showcases my skills, projects, and professional journey. The website features a dynamic hero section with an animated binary background, a projects page displaying my work with technology badges and GitHub links, an about me page with my professional experience and education, and a contact page with a working form that sends emails directly to me. The site also integrates with GitHub's GraphQL API to display my contribution graph, total stars, forks, repositories, and total contributions in real-time.

## What I Have Learned

* **GitHub GraphQL API Integration**: Learned how to use GraphQL queries to fetch specific data from GitHub. The query retrieves repository count, total stars, total forks, total contributions, and detailed contribution calendar data including daily contribution counts and colors.

* **Contact Form with Email Sending**: Built a working contact form that captures user name, email, subject, and message. Used Python's smtplib and EmailMessage to send emails securely. Implemented session-based success messages to show users their message was sent.

* **Data Processing with Python**: Used Python to process GitHub API responses - summing total stars and forks, extracting contribution data for the graph, and generating month labels dynamically from the contribution calendar.

* **Dynamic Contribution Graph**: Built a visual contribution graph similar to GitHub's using CSS grid. Each cell represents a day and is color-coded based on contribution count. The graph automatically updates based on real GitHub data.
 
* **Responsive Web Design**: Built the entire website to work on all screen sizes - from mobile phones to desktops - using Bootstrap grid system and custom CSS media queries.
 
* **CSS Styling and Animations**: Created custom CSS with hover effects, animations, and transitions. The binary background animation is generated using JavaScript with optimized rendering for performance for this i have taken help of chat gpt to create it because i dont know how to write javascript code.
 
* **Session Management**: Used Flask sessions to store temporary data like email sent status, allowing the contact page to show success messages after form submission.


## How It Works

### main.py

* **Imports and Setup**: The file imports Flask, requests, os, smtplib, and custom modules. It loads environment variables for email credentials, GitHub API token, and secret key. The GithubData class from `github_graph.py` is instantiated to fetch GitHub data.

* **GithubData Class Integration**: The class makes a POST request to GitHub's GraphQL API with a predefined query. It retrieves repository count, total stars, total forks, total contributions, and weekly contribution data. The checking_response() method verifies the API call was successful.
 
* **send_mail()**: This function creates an EmailMessage object with subject, sender, recipient, reply-to, and message content. It connects to Gmail's SMTP server using smtplib, logs in with environment variables, and sends the email. This handles contact form submissions.

* **Home Route**: Renders the home page (index.html). Passes GitHub contribution data including contribution_highlights (repository count, stars, forks, contributions), contribution_graph (weekly contribution data), num_of_weeks, months_label.

* **Projects Route**: Renders the projects page (projects.html) showing my work with technology badges and GitHub links.

* **About Me Route**: Renders the about page (about.html) with my professional experience, education, and skills.

* **Contact Route**: Handles both GET and POST requests. On POST, it extracts form data (name, email, subject, message), creates a dictionary, calls send_mail(), sets a session flag mail_sent = True, and redirects to the same page. On GET, it checks if the session flag exists using session.pop('mail_sent', False) and passes show_success to the template.


### github_graph.py

* **GraphQL Query**: Defines a GraphQL query that requests viewer information including repositories (total count, stargazer count, fork count) and contribution calendar (total contributions and weekly data with dates, colors, and contribution counts).

* **GithubData Class**: Creates a class to handle GitHub API calls. The __init__ method sends the POST request with the query and headers from environment variables. checking_response() verifies the response status code. fetching_required_data() extracts repository count, total stars, total forks, and total contributions using list comprehensions and sums. fetch_month_labels() processes weekly data to generate month labels for the contribution graph and returns both the graph data and month labels.
 
### CSS (style.css)

* **Color Scheme**: Uses a clean light theme with #F7F7F7 page background and white cards. Dark #333333 for text and cards. Yellow #FFD43B is used as the primary accent color for highlights, buttons, and icons. The hero section uses a dark #111111 background with the animated binary canvas.

* **Binary Background**: Custom styling for the animated binary canvas with proper positioning and z-index layering.

* **Responsive Design**: Extensive media queries for all screen sizes (1200px, 992px, 768px, 575px, 440px, 404px, 353px). Adjusts font sizes, image sizes, padding, margins, and grid layouts for optimal viewing on all devices.

* **GitHub Contribution Graph**: Custom styling for contribution cells with color mapping (none, low, medium, high, max). Grid layout with 54 columns representing weeks and 7 rows for days. Includes tooltips for contribution counts.

* **Card Animations**: Hover effects on project cards, tech stack cards, and buttons with smooth transitions and transform properties.

* **About Me Section**: Styled professional timeline with icons, job details, education, and responsive layout adjustments.


### JavaScript (script.js)

* **Binary Animation**: Creates an animated matrix-style binary code background  with the help of `Chat GPT`. The code generates particles (0s and 1s) and moves them diagonally.

* **Responsive Canvas**: Automatically resizes the canvas when the window size changes and recreates the binary field.

* **Dynamic Updates**: Randomly flips binary values and shifts the wave pattern to create continuous movement.



## Project Highlights

* **Flask Web Framework**: Built a multi-page portfolio website using Flask with dynamic routing and template rendering.

* **GitHub API Integration**: Used GraphQL to fetch real-time GitHub data including contributions, stars, forks, and repositories.

* **Dynamic Contribution Graph**: Created a GitHub-style contribution calendar that automatically updates based on API data.

* **Working Contact Form**: Implemented a functional contact form that sends emails using SMTP with session-based success messaging.

* **Animated Binary Background**: Created a smooth, optimized binary animation using HTML5 Canvas for visual appeal.

* **Responsive Design**: Made the entire website responsive using Bootstrap and custom CSS media queries.

* **Professional Timeline**: Built a clean, well-organized timeline for professional experience and education.

* **Project Showcase**: Designed an attractive project gallery with technology badges and GitHub integration.

* **Environment Variable Security**: Stored all sensitive credentials in environment variables for security.

* **Clean Code Structure**: Organized code with separate files for Python, HTML, CSS, and JavaScript following best practices.


