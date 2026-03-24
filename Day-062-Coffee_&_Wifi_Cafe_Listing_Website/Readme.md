# Day 62 – Coffee & Wifi Cafe Listing Website

## Project Overview

This is a dynamic cafe listing website built using Flask where users can view a list of cafes with details like location, opening hours, coffee rating, wifi strength, and power outlet availability. The website features a home page with a call-to-action button, an "Add Cafe" form where users can submit new cafe information, and a cafes page that displays all entries from a CSV file in a styled Bootstrap table. The project demonstrates form handling with Flask-WTF and Bootstrap-Flask, CSV file operations for data storage, dynamic table rendering with Jinja2, and conditional logic in templates.

## What I Have Learned

* **Working with CSV Files**: Learned how to read from and write to CSV files in Flask applications. Used Python's built-in csv module to open a CSV file, read its contents using `csv.reader()`, and append new entries using `csv.DictWriter()`. This provided a simple way to store data without setting up a database.

* **Form Fields with Choices**: Learned to create form fields with predefined choices using SelectField in WTForms. Created dropdown menus for coffee rating, wifi strength, and power outlet availability with emoji-based ratings (like ☕ for coffee, 💪 for wifi, 🔌 for power) to make the form visually engaging and user-friendly.

* **Field Validation with URL Validator**: Used WTForms' built-in URL() validator to ensure users enter valid URLs for Google Maps locations. This automatically checks if the input starts with "http://" or "https://" and has a proper domain format without writing custom validation code.

* **CSV Data Management**: Revised about `with()` method append new cafe entries to an existing CSV file while preserving the header row. Used `csv.DictWriter()` with fieldnames parameter to ensure only specific form fields are written to the CSV, and used `extrasaction='ignore'` to skip unwanted fields like submit and csrf_token

## How It Works

* **`main.py`**: The Flask application starts by importing necessary modules Flask, Bootstrap5, Flask-WTF components, csv module, and os. The CafeForm class inherits from FlaskForm and defines fields for cafe name (StringField), location URL (URLField with URL validator), opening and closing times (StringField), and three SelectFields for coffee, wifi, and power ratings—each with emoji-based choices. The home route `@app.route('/')` renders index.html. The add cafe route `@app.route('/add', methods=['GET', 'POST'])` creates a form instance on `GET` request it renders the `add.html` template with the form; on `POST` request it validates the form, uses list comprehension to extract field names excluding submit and csrf_token, opens the CSV file in append mode, writes the form data using `csv.DictWriter()`, and redirects to the cafes page. The cafes route `@app.route('/cafes')` reads the CSV file using `csv.reader()`, converts it to a list of rows, and passes it to the `cafes.html` template for rendering.

* **`base.html`**: This parent template contains the basic HTML structure with Bootstrap-Flask CSS loaded using `{{ bootstrap.load_css() }}` and an additional custom CSS file (styles.css) linked for extra styling. It defines {% block styles %}, {% block title %}, and {% block content %} blocks that child templates can override.

* **`index.html`'**: The home page template extends `base.html` and overrides the title block with "Coffee and Wifi" and the content block with a Bootstrap jumbotron. It includes a heading, description, and a "Show Me!" button that links to the cafes page using `{{ url_for('cafes') }}`

* **`add.html`**: `add.html` template extends `base.html` and imports `render_form` from Bootstrap-Flask and It creates a container with a heading "Add a new cafe into the database" and uses `{{ render_form(form) }}` to automatically generate the entire Bootstrap-styled form with all fields, labels, validation messages, and CSRF token. Below the form, also it includes a link to return to the cafes page.

* **`cafes.html`**:  This template extends `base.html` and renders all cafe data in a Bootstrap table with dark styling. It uses nested Jinja loops—an outer `{% for rows_data in cafes %}` loop iterates through each row of CSV data, and an inner `{% for value in rows_data %}` loop iterates through each column value in that row. Inside the inner loop, it uses conditional logic if the value equals "Location" it renders the column header; if the loop index is 2 (the location URL column), it renders the value as a clickable "Map link" anchor tag; otherwise it simply outputs the value in a table cell.

* **`CSV Data Storage`**: When a user submits the add cafe form, the data is appended to `cafe-data.csv` using `csv.DictWriter()`. The fieldnames parameter ensures only the defined form fields are written, while `extrasaction='ignore'` skips the submit and csrf_token fields. The CSV file maintains a header row with column names, and each new cafe entry is added as a new row.

## Project Highlights

* **CSV File Operations**: Revised about read & write to CSV files and created a simple database for storing the form data.
* **Dynamic Table Rendering**: Rendered CSV data as an HTML table using nested Jinja template using for loops with conditional formatting for specific columns.
* **Data Storage**: Successfully stored and displayed CSV files data using UTF-8 encoding.
