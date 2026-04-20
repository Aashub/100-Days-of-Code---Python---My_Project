# Day 68 – Authentication With Flask

## Project Overview

This is a secure user authentication system built with Flask that allows users to register, log in, and access protected content. The application features a complete authentication workflow including user registration with email validation (prevents duplicate signups), password hashing and salting for secure storage, login with credential verification, session management using Flask-Login, protected routes that only authenticated users can access, logout functionality, and a downloadable file section for logged-in users. The project demonstrates essential security concepts like encryption, hashing, and salting, along with practical implementation of user session management and flash messages for user feedback.

## What I Have Learned

* **What is Authentication**: Authentication is the process of verifying the identity of a user attempting to access a system. It answers the question "Who are you?" by checking credentials like email/username and password against stored records. In this project, authentication happens when users try to log in the system than the system checks if the entered email exists in the database and if the password matches the stored hash. Once verified, the user is granted access to protected routes like /secrets and /download.

* **Encryption**: Encryption is the process of converting readable data (plaintext) into an unreadable format (ciphertext) using an algorithm and a key. Encrypted data can be decrypted back to its original form using the same key. While this project uses hashing rather than encryption for passwords (because passwords don't need to be decrypted), encryption is important for other types of data that need to be reversible, like storing credit card numbers or personal messages.

* **Hashing**: Hashing is a one way mathematical function that converts any input (like a password) into a fixed-length string of characters called a hash. Unlike encryption, hashing cannot be reversed, you cannot get the original password from the hash. When a user registers, their password is hashed using generate_password_hash(), and only the hash is stored in the database. When they log in, the entered password is hashed again and compared to the stored hash using check_password_hash(). This ensures that even if the database is compromised, attackers cannot see the actual passwords.

* **Salting**: Salting is an additional security measure where a random string of characters (called a salt) is added to the password before hashing. This ensures that even if two users have the same password, their stored hashes will be different because each gets a unique salt. In this project, generate_password_hash() automatically generates and adds a random 8-character salt before hashing. Salting protects against rainbow table attacks (precomputed hash tables) because attackers would need to generate unique tables for every possible salt.

* **send_from_directory()**: Learned to use Flask's send_from_directory() function to securely serve files from a specific directory. In the download route, send_from_directory() serves a PDF file from the static/files directory. This function prevents directory traversal attacks by ensuring users can only access files within the specified directory. Setting as_attachment=False displays the file in the browser instead of downloading it.

* **flash()**: Used Flask's flash() method to display one time notification messages to users. Messages are stored in the session and cleared after being displayed. For example, when a user tries to register with an email that already exists, flash("You've have already signed up with that email, log in Instead!") shows an error message. When login fails due to incorrect password, flash("Password Incorrect. Please try again!") provides feedback. Messages are rendered in the template using get_flashed_messages().

* **Flask-Login Extension**: Learned to use Flask-Login for managing user sessions. The extension handles session creation, tracking the currently logged-in user, and protecting routes. Key components include LoginManager() for initialization, login_user() to log a user in, logout_user() to log them out, current_user to access the logged-in user's data in templates, login_required decorator to protect routes, and user_loader callback to reload user objects from the database.

* **UserMixin for Default Implementations**: Added UserMixin to the User model class, which provides default implementations for Flask-Login's required methods like is_authenticated, is_active, is_anonymous, and get_id(). This saves time and ensures compatibility with Flask-Login without writing these methods manually.

## How It Works

### main.py

*  The file imports required modules including Flask, SQLAlchemy, Werkzeug security for password hashing, Flask-Login for session management, and Path for file handling. The Flask app is created with a secret key from environment variables. A Base class is created for SQLAlchemy ORM, and the SQLite database users.db is configured and initialized. Flask-Login is set up with LoginManager() and login_manager.init_app(app). The @login_manager.user_loader decorator defines a callback that reloads the user object from the database using the user ID stored in the session. The User model defines the database table with columns for id, email (unique), password, and name, and inherits from UserMixin for Flask-Login compatibility. The create_database() function checks if the database exists using the Path module and creates tables only if needed.

* **Home Route**: This route renders the home page. It calls create_database() to ensure the database exists, then renders index.html. The home page shows login and register buttons only when no user is logged in (using current_user.name check) if user is logged in than it will hide the login and register button (using current_user.name check) because than this condition become true.

* **Register Route**: This route handles user registration. On GET requests, it renders register.html. On POST requests, it checks if the entered email already exists in the database by checking into the database. If the email exists, it flashes a message "You've have already signed up with that email, log in Instead!" and redirects to the login page. If the email is new, it hashes the password using generate_password_hash() method than it creates a new User object, adds it to the database by committing it, than it calls login_user(new_user) to automatically log the user in, and redirects to the secrets page.

* **Login Route**: This route handles user login. On GET requests, it renders login.html. On POST requests, it gets the email and password from the form, queries the database for a user with that email. If no user is found, it flashes "That Email, does not exist. Please try again!" and re-renders the login page. If the user exists than in this condition it uses check_password_hash() method to verify the entered password. If the password is correct, it calls login_user() to create a session for the user and redirects to the secrets page. If incorrect, it flashes "Password Incorrect. Please try again!" and re-renders the login page.

* **Secrets Route**: This route is protected by the @login_required decorator, meaning only authenticated users can access it. If a user tries to visit this page without logging in, Flask-Login automatically redirects them to the secrets page which will show them a message that they are trying to access the page Unauthorizingly. When accessed by a logged-in user, it renders secrets.html and passes the user's name using current_user.name so that it shows the username in secrets.html page.

* **Logout Route**: This route calls logout_user() method to end the user's session and redirects to the home page.

* **Download Route**: This route is also protected by @login_required. It uses send_from_directory() to serve a PDF file from the static/files directory. The file is displayed in the browser rather than downloaded.

### Supporting Files

* **base.html**: This parent template contains the navigation bar and common structure for all pages. It uses Jinja's {% block content %} for child templates to insert their content. The navigation bar conditionally shows/hides Login and Register links using {% if not current_user.name: %} these links only appear when no user is logged in. The "Log Out" link always appears for logged-in users.

* **index.html**: The home page template extends base.html and displays a box with heading "Flask Authentication". It conditionally shows Login and Register buttons only when no user is logged in using {% if not current_user.name: %} and if user is logged in it hides those login and register button.

* **login.html**: This template extends base.html and displays a login form with email and password fields. It uses {% with messages = get_flashed_messages() %} to display any flash messages (like "Password Incorrect" or "Email does not exist") above the form. The form submits via POST to the login route.

* **register.html**: This template extends base.html and displays a registration form with name, email, and password fields. The form submits via POST to the register route.

* **secrets.html**: This template extends base.html and displays a welcome message with the logged-in user's name ({{ name }}). It includes a link to download the file using {{ url_for('download') }}.

## Project Highlights

* **Secure Password Storage**: Used Werkzeug's generate_password_hash() with salting and check_password_hash() to securely store and verify passwords without storing plain text.

* **Flask-Login Integration**: Implemented complete session management using Flask-Login with login_user(), logout_user(), @login_required, and current_user.

* **User Feedback with Flash Messages**: Used flash() to display meaningful error messages for duplicate emails, incorrect passwords, and non-existent emails.

* **File Serving with send_from_directory**: Used send_from_directory() to securely serve downloadable files while preventing directory traversal attacks.

* **UserMixin**: Added UserMixin to the User model to provide default Flask-Login method implementations without writing extra code.


