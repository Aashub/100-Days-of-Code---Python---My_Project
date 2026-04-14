# Day 66 – Cafe & Wifi API with RESTful Endpoints

## Project Overview

This is a RESTful API built with Flask and SQLAlchemy that serves cafe data for a coffee shop finding application. The API allows users to retrieve random cafe information, get all cafes, search for cafes by location, add new cafes, update coffee prices using PATCH requests, and delete cafes from the database using DELETE requests with API key authentication. Unlike traditional web applications that return HTML pages, this API returns data in JSON format, making it consumable by frontend applications, mobile apps, or third-party services. The project demonstrates REST API design principles, different HTTP request methods (GET, POST, PATCH, DELETE), query parameters, request form data, API key authentication, and database CRUD operations using SQLAlchemy. I also used Postman application extensively to test all API endpoints before publishing the documentation.

## API Documentation link

* https://documenter.getpostman.com/view/53952896/2sBXqCP3nP#405d4cd5-3a29-489f-83a4-882e71fd2b4b

## What I Have Learned

* **What is REST API**: REST (Representational State Transfer) API is an architectural style for building web services that use HTTP requests to access and manipulate data. REST APIs follow standard HTTP methods—GET to retrieve data, POST to create new data, PATCH/PUT to update existing data, and DELETE to remove data. Unlike regular websites that return HTML pages for humans to read, REST APIs return data in JSON format that other programs can easily understand and use. This allows different applications (like a mobile app, a website, or another server) to communicate with the same backend.

* **PUT vs PATCH Request and How to Work with Them**: PUT and PATCH are both HTTP methods used for updating resources, but they work differently. PUT replaces the entire resource with new data for example if we only send one field, all other fields get erased. PATCH is used for partial updates only for example we only send the fields we want to change or update, and other fields remain untouched. In this project, I used PATCH request to update only the coffee price of a cafe without affecting other fields like name, location, or wifi availability. To work with PATCH requests, I used the /update-price route, which has extracted the new price from query parameters using request.args.get('new_price'), found the cafe by ID, updated only the price field, and committed the change.

* **How to Use Postman to Test API Requests**: Postman is a tool that allows developers to test API endpoints without building a frontend. I learned to create different types of requests in Postman for example GET requests to retrieve data, POST requests to add new cafes with form data, PATCH requests to update prices with query parameters, and DELETE requests to remove cafes with API key authentication. Using Postman, I could see the JSON response, check status codes (200 for success, 404 for not found, 403 for unauthorized), and debug issues.

* **Converting Database Records to JSON**: Learned to create a to_dict() method in the Cafe model that converts a database record into a Python dictionary. The method loops through all column names in the table using self.__table__.columns, uses getattr() to retrieve each column's value, and builds a dictionary. This dictionary is then passed to jsonify() which converts it to proper JSON format for API responses.

* **Query Parameters for Filtering Data**: Used query parameters in URLs to filter and customize responses. For example, /search?loc=London passes "London" as a location filter, accessible via request.args.get('loc')

* **HTTP Status Codes for API Responses**: Learned to return appropriate HTTP status codes along with JSON responses for examle 200 for successful requests, 404 when a requested resource isn't found, and 403 when authentication fails. Status codes help API clients understand what happened without parsing the response body.

* **Form Data Extraction for POST Requests**: For the adding of new cafe data in the database, extracted data from POST requests using `request.form.get('field_name')` to retrieve values submitted from HTML forms or Postman form-data.

## How It Works

* **main.py**: The Flask application sets up SQLAlchemy with SQLite database and defines the Cafe model with columns for id, name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, and coffee_price. The model includes a to_dict() method that converts a record into a JSON-serializable dictionary

* **home Route**: This route renders a simple HTML page that welcomes users to the Cafe & Wifi API and provides a clickable link to the Postman API documentation. It also calls create_database() to ensure the database and tables exist before any API requests are made.

* **get_random_cafe Route**: This route handles GET requests and returns a randomly selected cafe from the database. It calls read_cafe_data() to fetch all cafes, converts them into a list, and uses Python's random.choice() to pick one cafe randomly, converts that cafe object to a dictionary using the to_dict() method, and returns it as JSON using jsonify().

* **all Route**: This route handles GET requests and returns every cafe stored in the database. first It fetches all cafe records, than it uses list comprehension to convert each cafe object into a dictionary, and returns the complete list as a JSON dictionary. This endpoint is useful for applications that want to display all cafes in a list view.

* **search Route**: This route handles GET requests and filters cafes based on the location provided as a query parameter. It reads the loc parameter using request.args.get('loc'), loops through all cafes and keeps only those where cafe.location == location, and converts the matching cafes to dictionaries, and returns them as JSON. If no cafes match the location, it returns a 404 error with a message "Sorry, we don't have a cafe at that location".

* **add_new_cafe Route**: This route only accepts POST requests and adds a new cafe to the database. It extracts all form data using request.form.get() for each field (name, map_url, img_url, location, seats, sockets, toilet, wifi, calls, coffee_price), converts the boolean fields like (sockets, toilet, wifi, calls) from string to boolean using Python's bool() function, and creates a new Cafe object with all the extracted data, and adds that data to the database session, commits the transaction, and returns a JSON success message.

* **update_cafe_price Route**: This route accepts PATCH requests and updates only the coffee price of a specific cafe. It captures the cafe ID from the URL using `<int:cafe_id>`, reads the new_price from query parameters using request.args.get('new_price'), queries the database to find the cafe with that ID. If the cafe exists, it updates the coffee_price field, commits the change, and returns a success response with status code 200. If no cafe is found with that ID, it returns a 404 error with a message "Sorry a cafe with that id was not found".

* **delete_cafe_store Route**: This route accepts DELETE requests and removes a cafe from the database, but only if the user provides a valid API key. It captures the cafe ID from the URL, reads the api-key from query parameters, compares it with the stored API_KEY from environment variables. If the API key doesn't match, it returns a 403 Forbidden error with message "Sorry, that's not allowed. If the API key matches, it searches for the cafe by ID if found, it deletes it, commits the change, and returns a success response with status code 200. If the cafe is not found, it returns a 404 error.

* **to_dict()**: This helper method is defined inside the Cafe model class. It creates an empty dictionary, loops through every column name in the table using self.__table__.columns, and uses Python's getattr() function to retrieve the value of each column from the current record. The column name becomes the dictionary key, and the value becomes the dictionary value. This dynamic approach means if new columns are added later, the method automatically includes them.

* **create_database()**: This function Checks if the database file already exists using the Path module. If it doesn't exist, it creates all tables. If it already exists, it skips creation to prevent accidental data loss.

## Postman Testing Workflow

* I used Postman to test every API endpoint. For GET requests like /random and /all, I simply entered the URL and clicked Send to see JSON responses. For POST requests to /add, I selected form-data in the body tab and added fields like name, map_url, and location. For PATCH requests to /update-price/1, I added query parameters in Postman's Params tab. For DELETE requests, I added the api-key as a query parameter and confirmed the cafe was removed from the database. Postman showed me status codes and response bodies, helping me debug issues like incorrect query parameter names or missing form fields.

## Project Highlights

* **REST API Design**: Built a fully functional REST API following RESTful conventions with proper HTTP methods and status codes.

* **PUT vs PATCH Understanding**: Learned the difference between PUT (full replacement) and PATCH (partial update) and implemented PATCH for price updates.

* **Postman Testing**: Used Postman extensively to test all API endpoints for example GET, POST, PATCH, and DELETE requests

* **JSON Response Formatting**: Implemented to_dict() method to convert database records to JSON-serializable dictionaries dynamically

* **Query Parameters**: learned how to use query parameter for example search filtering, price updates, and API key authentication

* **Form Data Extraction**: Handled POST requests by extracting data from request.form.get() for adding new cafes.
