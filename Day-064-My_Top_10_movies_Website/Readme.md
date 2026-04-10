# Day 64 – My Top 10 Movies Website

## Project Overview

This is a dynamic movie ranking website built using Flask, SQLAlchemy, and The Movie Database (TMDB) API. The application allows users to build and manage their personal top 10 movies list by searching for movies through an external API, adding them to a database, and then rating, reviewing, and ranking their favorites. The website features a home page displaying all saved movies as stylish cards with rankings, ratings, reviews, and poster images. Users can add new movies by searching TMDB, select from search results, edit ratings and reviews for existing movies, delete movies from their collection, and automatically update rankings based on ratings. The project demonstrates API integration, complex database operations, CRUD functionality, automatic ranking logic, and advanced form handling with Flask-WTF and Bootstrap-Flask.

## What I Have Learned

* **External API Integration with TMDB**: Revised about how to use api to integrate The Movie Database (TMDB) API to search for movies and fetch detailed information like title, release date, overview, and poster path.

* **Dynamic Database Updates from API**: Learned to fetch movie details from TMDB using a movie ID and automatically populate the database with title, year, description, and poster URL. This demonstrates how external data can be seamlessly integrated into local storage.

* **Conditional Database Creation**: Used Path module to check if the database file already exists before creating it. The create_database() function checks the instance folder path and only calls db.create_all() if the database doesn't exist, preventing accidental data loss.

## How It Works

* **main.py**: The Flask application sets up SQLAlchemy with SQLite database and defines the Movie model with columns for id, title, year, description, rating, ranking, review, and img_url. Two WTForm classes are defined, EditMovieForm for updating ratings and reviews, and AddMovieForm for searching movies. The home route checks if a movie_id is passed in the URL (from movie selection), calls update_movie_data_in_database() to fetch and save the selected movie from TMDB to the databse and then it, redirects to the edit page for rating/review so that user can update the rating and review of the movie, then queries all movies, calls update_ranking() to calculate rankings, and renders index.html with all movies. The edit route captures the movie ID from the URL, finds the movie in the database, and calls update_rating_review() to save the new rating and review when the form is submitted. The delete route removes a movie by its ID and redirects home. The add route displays a form to search for movies, then renders select.html with search results from TMDB.

* **update_movie_data_in_database()**: This function takes a movie ID from TMDB, makes an API request to fetch detailed movie information including title, release date, overview, and poster path, creates a new Movie object with this data, adds it to the database, commits the transaction, and returns the new movie's ID so the user can immediately add their rating and review.

* **update_ranking()**: This function Fetches all movies from the database, temporarily sets every movie's ranking to None and commits, than it creates a list of all ratings, sorts them from highest to lowest, then loops through the sorted ratings and assigns ranking numbers (1 for highest rating, 2 for second highest, etc.) to the corresponding movies. This ensures rankings always reflect the current ratings.

* **fetch_themoviedb_url_and_headers()**: Constructs the search URL using the movie name entered by the user and returns both the URL and authentication headers needed for making TMDB API requests.

* **index.html**: Displays all saved movies as cards. Each card shows the movie poster in the front with its ranking number, and the back shows title, release year, rating (with star icon), review text, description, and two buttons Update (opens edit page) and Delete (removes the movie). Movies are automatically ordered by ranking.

* **add.html & select.html**: The add page displays a form where users enter a movie title. When submitted, it searches TMDB and displays results in select.html, where each matching movie appears as a clickable link. Clicking a movie passes its TMDB ID back to the home route via URL parameter, triggering the database addition

* **edit.html**: Displays the movie title and provides a form with two fields rating (float) and review (text). When submitted, it updates the database and redirects home, where rankings automatically recalculate and shown in the home page.

* **Database Operations**: The application uses SQLAlchemy ORM for all database interactions for example db.session.execute(db.select(Movie)) for queries, db.session.add() for new records, direct attribute assignment for updates, db.session.delete() for removals, and db.session.commit() to save all changes.

## Project Highlights

* **External API Integration**: Successfully integrated TMDB API to search for movies and fetch detailed information automatically also TMDB website not works in india because it get blocked so i have figured out by using VPN i can still use TMDB api.

* **Complete CRUD Operations**: Built full Create, Read, Update, Delete functionality for managing movie collections.

* **Conditional Database Creation**: Used file path checking to create database only when needed, preserving existing data


