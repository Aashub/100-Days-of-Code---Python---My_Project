# Day 66 – Upgraded Blog Website with CKEditor & Full CRUD Operations

## Project Overview

This is a fully upgraded dynamic blog website built with Flask that now supports complete CRUD (Create, Read, Update, Delete) functionality along with a working contact form that sends email notifications. The website allows users to view all blog posts on the home page, read individual posts in detail, create new posts using a rich text editor (CKEditor), edit existing posts with pre-populated form fields, delete posts they no longer want, and send messages through the contact form which are automatically emailed to the site owner. The project demonstrates advanced Flask concepts including WTForms with custom validation, CKEditor integration for rich text editing, SQLAlchemy ORM for database operations, Bootstrap-Flask for styling, email integration with smtplib, environment variables for secure credential storage, and template inheritance.

## What I Have Learned

* **CKEditor Integration**: Learned to integrate CKEditor, a powerful WYSIWYG (What You See Is What You Get) rich text editor, into Flask forms. Using flask_ckeditor extension, I added CKEditorField to my form which provides users with a word processor like interface for writing blog posts including formatting options like bold, italic, headings, lists, links, and image embedding. The editor stores content as HTML, which is rendered safely.

* **HTML Safe Rendering for Blog Content:**: Learned how to use the |safe filter in Jinja templates ({{ post.body|safe }}) to render HTML content from CKEditor properly. Without this filter, Jinja would escape HTML tags and display them as plain text instead of formatted content.

## How It Works

### main.py

*  The file imports required modules and initializes the Flask app with Bootstrap5 and CKEditor extensions. A Base class is created for SQLAlchemy ORM, and the SQLite database posts.db is configured and initialized. The BlogForm class defines WTForm fields for title, subtitle, author, image URL (with validation), and CKEditorField for rich text blog content. The BlogPost model defines the database table with columns for id, title, subtitle, date, body, author, and img_url. The send_mail() function is used for sending the email to the owner when someone fills the contact form in contact form page and click send button, The create_database() function checks if the database exists using Path module and creates tables only if needed. The read_blogs_data() function queries and returns all blog posts ordered by ID for reuse across routes.

* **@app.route('/') Home Route**: This route renders the home page displaying all blog posts. It calls create_database() to ensure the database exists, then calls read_blogs_data() to fetch all posts ordered by ID, converts the result to a list, and passes it to index.html where each post is displayed with title, subtitle, author, date, and delete icon.

* **@app.route('/show_post') Show Individual Post Route**: This route handles displaying a single blog post when clicked from the home page. It captures the post ID from the URL, queries the database for the specific post, and passes the post object to post.html for full display including title, subtitle, author, date, and formatted body content

* **@app.route('/new-post') Create New Post Route**: This route handles both displaying the new post form and processing form submissions. On GET requests, it creates an empty BlogForm instance and renders make-post.html. On POST requests, it validates the form, creates a new BlogPost object using request.form.get() for each field, adds it to the database session, commits the change, and redirects to the home page.

* **@app.route('/delete') Delete Post Route**: This route handles deleting blog posts. It captures the post ID from the URL, queries the database for that specific post, calls db.session.delete(blog_post), commits the deletion, and redirects to the home page where the deleted post no longer appears.

* **@app.route('/about') About Page Route**: This simple route renders the about.html template containing static information about the blog author.

* **@app.route('/contact') Contact  Page Route**: This route handles both displaying the contact form and processing form submissions. On GET requests, it simply renders contact.html. On POST requests, it extracts the user's name, email, phone number, and message from request.form[], formats them into a readable string, calls send_mail() to email the data to the owner, and re-renders contact.html with "successful" to show a user that email is being sent successfully.

### Supporting Files

* **index.html**: The home page template extends header.html and footer.html. It loops through all_posts and displays each post's title, subtitle, author, date, and includes a delete link (✘) next to each post. It also includes a "Create New Post" button that links to the add new post route.

* **post.html**: The individual post page template displays the full blog post including title, subtitle, author, date, and formatted body content using {{ post.body|safe }} to render HTML from CKEditor. It also includes an "Edit Post" button that links to the edit route with the post ID.

* **make-post.html**: This reusable template handles both creating new posts and editing existing posts. It uses jinja template for if-else conditional statement to display "Edit Post" or "New Post" as the heading. and It renders the WTForm using Bootstrap-Flask's using render_form() and loads CKEditor using {{ ckeditor.load() }}.

* **contact.html**: The contact page template displays a contact form where users can enter their name, email, phone number, and message. It uses jinja template if-else conditional logic to display "Successfully sent message" as the heading when an email is successfully sent, otherwise it displays "Contact Me".

* **header.html & footer.html**: These reusable components contain the navigation bar, meta tags, CSS imports, and footer content. The header includes links to home, about, and contact pages using url_for().

* **about.html**: This static page template includes the header and footer using Jinja's statements. It features a masthead with a background image (about-bg.jpg), a heading and subheading. The main content contains three paragraphs.

## Project Highlights

* **CKEditor Integration**: Added rich text editing capabilities to blog posts using CKEditor, allowing users to format content like a word processor.

* **Complete CRUD Operations**: Implemented full Create, Read, Update, Delete functionality for blog posts without touching the database directly.

* **Pre-Populated Edit Forms**: Edit forms automatically populate with existing blog post data, making updates intuitive and user-friendly.

* **HTML Safe Rendering**: Used Jinja's |safe filter to properly render HTML content from CKEditor without escaping tags.

