# Day 69 – Upgraded Blog Website(with Flask User Authentication)


## Project Overview

This is a fully upgraded dynamic blog website built with Flask that now supports user authentication, comment functionality, relational databases, admin-only features, and rich text editing. The website allows users to register and log in securely, leave comments on blog posts with profile images using Gravatar, and view all blog content. Admin users (user ID 1) have special privileges including creating new posts, editing existing posts, and deleting posts. The project demonstrates advanced Flask concepts including one-to-many database relationships, custom decorators for admin authorization, Flask-Login for session management, password hashing with salting, CKEditor for rich text editing, Gravatar integration for user avatars, and flash messages for user feedback.

## What I Have Learned

* **Revised & Used Python Decorators**: Created a custom @admin_only decorator to restrict access to certain routes based on user privileges. The decorator checks if the currently logged-in user has an ID of 1 (admin) using if current_user.id != 1: return abort(403). If not, it returns a 403 Forbidden error. This is applied to routes like adding new posts, editing posts, and deleting posts. The @wraps(func) decorator from functools preserves the original function's name and metadata, which is important for debugging.

* **Creating Relational Databases**: Learned how to create relationships between database tables using SQLAlchemy's relationship() function and foreign keys. Instead of storing redundant data, relational databases link tables together using IDs. For example, instead of storing the author's name in every blog post, the BlogPost table stores an author_id that references the id column in the User table. This prevents data duplication and ensures consistency.

* **Creating One-to-Many Database**: Implemented one to many relationships where one user can have many blog posts and many comments, but each blog post belongs to one user and each comment belongs to one user and one post. The User table has posts = relationship("BlogPost", back_populates="author") which means one user can be linked to multiple BlogPost records. Similarly, BlogPost has author_id = mapped_column(ForeignKey("users.id")) and author = relationship("User", back_populates="posts"). The back_populates parameter creates a bidirectional relationship so changes in one direction reflect in the other. The cascade="all, delete-orphan" ensures that when a blog post is deleted, all its associated comments are also deleted automatically.

* **Flask-Gravatar Integration**: Used Flask-Gravatar extension to display user profile images (avatars) in the comments section. Gravatar (Globally Recognized Avatar) associates an email address with an image. In the post.html template, It converts the commenter's email into a Gravatar URL. The Gravatar is configured with size=100, rating='g' (safe for all audiences), default='retro' (fallback if no avatar exists), and other customization options.

* **Admin Authorization with abort()**: Used Flask's abort(403) function to return a 403 Forbidden HTTP status code when non-admin users try to access restricted routes. This prevents unauthorized users from creating, editing, or deleting blog posts by manually typing URLs like /new-post or /delete/1.


## How It Works

### main.py

*  The file imports required modules including Flask, SQLAlchemy with relationship() for database relations, Flask-Login for session management, Flask-Gravatar for user avatars, and custom forms from forms.py. The Flask app is created with secret key from environment variables, CKEditor and Bootstrap5 are initialized. The SQLite database posts.db is configured. Flask-Login is set up with login_manager.init_app(app) and @login_manager.user_loader callback. Three database models are defined—User (id, email, password, name) with posts and comments relationships, BlogPost (id, title, subtitle, date, body, img_url, author_id foreign key to users.id, author relationship back to User, and comments relationship with cascade delete), and Comment (id, text, author_id foreign key to users.id, post_id foreign key to blog_posts.id, with relationships to both User and BlogPost). Gravatar is configured with size, rating, and default image settings. The admin_only decorator checks if current_user_id ise equal to 1 or not, otherwise returns abort(403). The create_database() function ensures the database exists before operations.

* **Home Route**: Renders the home page displaying all blog posts. It calls create_database() to ensure the database exists, fetches all posts using read_blogs_data(), and passes them to index.html. The template shows author names using {{post.author.name}} (accessing the related User object).

* **Register Route**: This route handles user registration. On POST, it checks if the email already exists. If yes, it flashes "You've already signed up, log in instead!" and redirects to login. If the email is new, it hashes the password, creates a new user, saves to database, logs the user in automatically, and redirects to home page.

* **Login Route**: Handles user login using LoginForm. On POST, it queries for the user by email. If user doesn't exist, flashes "That Email, does not exist. Please try again!" and redirects to login. If user exists, it verifies the password using check_password_hash(). If correct, calls login_user(user_obj) and redirects to home. If incorrect, flashes "Password Incorrect" and redirects to login.

* **Logout Route**: Calls logout_user() to end the user's session and redirects to the home page.

* **Show Post Route**: Displays an individual blog post with comment form. When a comment is submitted, it checks current_user.is_authenticated or not. If logged in, it creates a new Comment object linking comment_author=current_user and parent_post=requested_blog_post, adds to database, and redirects. If not logged in, it flashes "You need to login or register to comment!" and redirects to login page.

* **Edit Post Route**: This route is protected by @admin_only so only admin can access it. When admin first visits the page (GET request), the form is already filled with the post's current information so they can just change what they want. When admin submits the edit form (POST request), it updates the existing post with the new form data and saves it to the database.

* **Delete Post Route**: This route is protected by @admin_only so only admin can access it. It finds the post by its ID, deletes it from the database, and redirects to home page. All comments on that post are deleted automatically because of the cascade delete setting.

* **About Route**: This route renders the about page with static content.

* **Contact Route**: When someone submits the contact form (POST request), it grabs their name, email, phone number, and message, sends an email to the site owner, and shows a success message. On GET request, it just shows the contact form.

### forms.py

*  Contains four WTForm classes. `BlogForm` is used for creating and editing posts with title, subtitle, author, image URL, body with CKEditor, and submit button. `RegisterForm` is used for sign up with email, password, username, and submit. `LoginForm` is used for login with email, password, and submit. `CommentForm` is used for leaving comments with comment field using CKEditor and submit button.

### Supporting Files

* **index.html**: Home page template. It loops through all posts and shows each post's title, subtitle, author name, and date. It shows the delete button (✘) only if the logged-in user is admin. It also shows the "Create New Post" button only if admin is logged in.

* **post.html**: Single post page template. It shows the full post with title, subtitle, body, author name, and date. It shows the "Edit Post" button only if admin is logged in. It shows all comments with Gravatar profile pictures and commenter names below the post. It shows the comment form for logged-in users to write comments. if someone try to comment without logging in it will redirect them to login page with flash message by saying log in first if you want to make a comment. 

* **make-post.html**: Reusable template for both creating new posts and editing existing posts. It uses {% if id %} to show "Edit Post" or "New Post" as the heading. It loads CKEditor for rich text editing and renders the form using Bootstrap-Flask.

* **login.html & register.html**: Authentication templates that render their respective WTForms using render_form(). Both include flash message handling using get_flashed_messages() to display error alerts for duplicate registrations or incorrect credentials.

* **header.html**: Navigation bar template that appears on every page. It shows different links based on login status. If user is logged out, it shows "Login" and "Register". If user is logged in, it shows "Log Out". It always shows "Home", "About", and "Contact" links for everyone.

* **contact.html**: Contact page template. It shows a form where visitors can enter their name, email, phone, and message. After the form is submitted successfully, the heading changes from "Contact Me" to "Successfully sent message" to show the user that their message is being sent successfully.

* **about.html**: Static about page with placeholder text about the blog author. It includes the header and footer.

* **footer.html**: Footer template that appears at the bottom of every page. It contains social media links (Twitter, Facebook, GitHub) and a copyright notice.

## Project Highlights

* **One-to-Many Relationships**: Learned how to create one to many relationship schema where one admin user can have many posts, and posts can have many comments.
* **Admin Decorator**: Created a custom guard that only lets the admin user (ID=1) create, edit, or delete posts.
* **Comment System**: Logged-in users can leave comments on posts. Their profile picture from Gravatar shows up next to their comment.
* **Cascade Delete**: Used cascade delete so When a post is deleted, all its comments are automatically deleted too from the database.
* **Gravatar Integration**: Profile pictures appear automatically. No need to upload images. Just enter your email and Gravatar gives you a picture

