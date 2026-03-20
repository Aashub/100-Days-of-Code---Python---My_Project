# Day 61 – Secure Login System with Flask-WTF and Bootstrap-Flask

## Project Overview

This is a secure login system built using Flask with Flask-WTF extension for form handling and validation, and Bootstrap-Flask for easy styling. The website features a home page with a login button, a login page with a form that validates user input (email format and password length), and success or denied pages based on credentials. The project demonstrates how to create forms using Flask-WTF, add validation rules to form fields, protect against CSRF attacks, render forms with Bootstrap styling using Bootstrap-Flask, and inherit templates using Jinja2's extends and blocks functionality.

## What I Have Learned

* **Flask-WTF Extension**: Flask-WTF is a Flask extension that integrates the WTForms library, making it easier to create and handle web forms in Flask applications. It provides a simple way to define form classes, add validation rules, and automatically handle CSRF protection.

* **Easy Form Validation**: Learned how Flask-WTF makes form validation simple by using built-in validators like `DataRequired()` and `Length()`. For example, the Email field automatically checks if the input contains an "@" symbol and a domain, while the Password field ensures the user enters at least 8 characters all of this without writing any custom validation code.

* **Less Code**: Understood that using WTForms reduces the amount of code needed to create forms. Instead of manually writing HTML for each input field and handling validation errors with if-else statements, WTForms handles all the heavy lifting with just a few lines of Python code.

* **Built-in CSRF Protection**: Learned that Flask-WTF provides automatic CSRF (Cross Site Request Forgery) protection for all forms. CSRF is a security attack where malicious websites trick users into performing unintended actions. Flask-WTF generates a unique token for each form and validates it when the form is submitted, ensuring the request actually came from your website.

* **Creating Forms with Flask-WTF**: Created LoginForm class by inheriting from `FlaskForm` and defining form fields using WTForms field types like `StringField`, `PasswordField`, and `SubmitField`. Each field can have validation rules attached to it using the `validators` parameter.

* **csrf_token**: Learned that Flask-WTF automatically adds a hidden csrf_token field to every form. This token is required for security and must be included in the form template. Bootstrap-Flask handles this automatically when using render_form(), but when we use manually built forms it needs to include {{ form.csrf_token }}.

* **Adding Validation to Forms with Flask-WTF**: Added validation to form fields using validators like `DataRequired(message="Error message")` to make fields mandatory, and Length(min=8, max=64) to enforce minimum and maximum character limits. When validation fails, Flask-WTF automatically populates error messages that can be displayed to the user.

* **Receiving Form Data with WTForms**: After form submission, accessed the submitted data using `form.Email.data` and `form.Password.data`. This provides a clean, object-oriented way to retrieve user input without manually parsing `request.form[]`.

* **Inheriting Templates Using Jinja2**: Used Jinja2 template inheritance to create a base template (base.html) containing the common structure like meta tags, CSS imports, and navigation. Other templates like index.html, login.html, success.html, and denied.html inherit from this base using `{% extends "base.html" %}` and then fill in their own title and content inside the `{% block title %}` and `{% block content %}` sections.

* **Super Blocks**: Learned about super() in Jinja templates which allows child templates to add content to a block without completely replacing the parent block's content. This is useful when you want to extend the parent's CSS or JavaScript while adding your own.

* **Bootstrap-Flask Supports WTForms**: Learned about Bootstrap-Flask, a Flask extension that makes Bootstrap work nicely with Flask-WTF forms. Instead of writing lots of HTML code for each input field, labels, error messages, and CSRF token manually, I used `{{ render_form(form) }}` in my login.html file. This one line automatically generates the entire Bootstrap styled form with all fields, proper labels, validation error messages, and hidden CSRF token—turning what could have been 30-40 lines of HTML into just 3 lines of code.

## How It Works

* **`main.py`**: The Flask application starts by importing necessary modules Flask, Flask-WTF components, WTForms fields and validators, Bootstrap-Flask, and os for environment variables. Email and password credentials are loaded from environment variables using `os.environ[]` for security. After that The LoginForm class inherits from `FlaskForm` and defines three fields, `Email` (StringField) with DataRequired and Length validators, `Password` (PasswordField) with DataRequired and Length validators, and a SubmitField for the `login` button. After that The Flask app instance is created and than Bootstrap4 is initialized with `Bootstrap4(app)`, and a secret key is set for CSRF protection. The home route `@app.route('/')` renders index.html. The login route `@app.route('/login', methods=['GET', 'POST'])` creates an instance of `LoginForm`, and that if checks if the request.method condition is equal to `GET` if this condition come out true than it will render login page after user fills the details and click on login button elif condition of request.method of comes out true `POST`. On POST, it calls `form.validate_on_submit()` which automatically runs all validators—if validation passes, it checks if the entered email and password match the stored environment variables, if the email id and password does matches than it rendering success.html if correct or if it is incorrect than it renders denied.html. If validation fails, it re-renders the login page with error messages displayed.

* **`base.html`**: This is the parent template that all other templates inherit from. It contains the basic HTML structure with head and body tags. The `{% block styling %}` block includes `{{ bootstrap.load_css() }}` which loads Bootstrap CSS from Bootstrap-Flask. and The `{% block title %}` and `{% block content %}` blocks are placeholders that child templates will fill with their specific content.

* **`index.html`'**: The home page template extends `base.html` and overrides the `title` block with "Secrets" and the `content` block with a welcome message. It includes a Bootstrap jumbotron with a heading, description, and a Login button that links to the login page using `{{ url_for('login') }}`.

* **`login.html`**: This template extends `base.html` and uses Bootstrap-Flask's `render_form()` function to render the login form. The `{% from 'bootstrap4/form.html' import render_form %}` line imports the render_form macro. Inside the content block, it creates a Bootstrap container and calls `{{ render_form(login_form) }}`, which automatically generates all form fields, labels, validation error messages, CSRF token, and styling—reducing the entire login form to just a few lines.

* **`success.html and denied.html`**:  These templates extend base.html and override the title and content blocks. Success.html displays a celebratory GIF (Rick Astley) with a "Top Secret" heading, while denied.html displays a funny dog GIF with an "Access Denied" heading. Both demonstrate how to embed external content from GIPHY using iframe tags.

* **`Form Validation Process`**: When a user submits the login form, Flask-WTF automatically validates all fields based on the rules defined in LoginForm class. If the Email field doesn't contain proper email format (missing "@" or domain), or if the Password field has less than 8 characters, the form fails validation. Error messages defined in validators (message="Invalid email address." and message="Field must be 8 characters long.") are passed to the template and displayed automatically by `render_form()`. Only when all validators passes than only `form.validate_on_submit()` return True and proceed to check credentials.

## Project Highlights

* **Easy Form Validation**: Used built-in validators like DataRequired and Length to enforce input rules without writing custom validation code.
* **Bootstrap-Flask Styling**: Used Bootstrap-Flask with render_form() to generate fully styled Bootstrap forms with minimal code.
* **Template Inheritance**: Created reusable base template using Jinja2 extends and blocks for consistent layout across all pages.
* **Form Data Extraction**: Retrieved form data using form.Email.data and form.Password.data for clean, object-oriented access.




