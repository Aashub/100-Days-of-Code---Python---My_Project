# Day 71 – Deployed My Blog Website Live on Render

## Website Overview

This is my fully functional blog website that I built with Flask and successfully deployed live on the internet using Render (a cloud hosting platform). Anyone can now visit my website, sign up, log in, leave comments on blog posts, and read all my content. The admin (me) can create, edit, and delete posts from anywhere in the world. This project taught me how to take a Flask application from my local computer and put it online so others can access it. I learned about deployment, cloud hosting, WSGI servers, PostgreSQL databases, environment variables, and how to keep my secret keys safe.

## My Blog Website URL
* https://my-peronal-blog-website.onrender.com/

## What I Have Learned

* **Deployment using Render, Git, and GitHub**: Deployment means taking my code from my local computer and putting it on a cloud server so anyone with internet can access it. I used Render as my hosting provider because it's free and easy to use with GitHub account. I pushed my code to GitHub, connected my GitHub repository to Render and after making certain configuration in render for creating new workspace for deploying my website and database creation via postgresql and every configuration gets executed successfully,Render automatically deployed my website. Now whenever I push changes to GitHub, Render automatically updates the live website.

* **Gunicorn(WSGI Server)**: Gunicorn (Green Unicorn) is a WSGI server. WSGI (Web Server Gateway Interface) is a standard that helps web servers talk to Python web applications. When I run my Flask app locally, I use app.run() which is Flask's built-in server. But that server is slow and not safe for real world use. Gunicorn acts as a middleman between the internet and my Flask app. It handles multiple users at the same time, manages requests efficiently, and keeps my app running smoothly. I set it up by creating a Procfile (a file that tells Render how to run my app) with the line web: gunicorn main:app - which means "use gunicorn to run the app variable from the main.py file".

* **Why Create a Procfile**: A Procfile (Process File) is a special file that tells cloud hosting platforms like Render what command to run to start my application. Without a Procfile, Render wouldn't know how to launch my website. The format is simple: web: gunicorn main:app where web is the process type, gunicorn is the server, main is my Python filename (main.py), and app is the Flask instance inside that file.

* **Updated .gitignore File**: Before pushing my code I have updated my .gitignore file to make sure unnecessary files don't get uploaded to GitHub or Render. I added things like __pycache__/ (Python cache files), .env (my secret keys and passwords), *.db (local database files since I'm switching to PostgreSQL), and instance/ (folder where local databases are stored). This keeps my secrets safe and reduces clutter.

* **Creating a New Web Service**: On Render dashboard, I clicked "New +" and selected "Web Service". I connected my GitHub account, selected my blog repository also i make sure that my which Project Directory should be used in render so only that Directory used by render to deploy or run my website after that Render automatically detected it was a Python app. I kept all default settings and clicked "Create Web Service". Render then cloned my code from GitHub, installed dependencies from requirements.txt, and started my app.

* **Adding Env Variables on Render**: My web app uses secret keys and email passwords that I stored in environment variables locally (using os.environ). On Render, I had to add these same variables in the dashboard under "Environment Variables". I added: SECRET_KEY (my Flask secret key), email (my Gmail for contact form), password (my Gmail app password), and db (database URL). This keeps my secrets safe and not visible in my code.

* **Creating a New PostgreSQL Database**: Previously, my blog used SQLite (a file-based database) which doesn't work well on cloud hosting. Render provides a free PostgreSQL database. PostgreSQL is a powerful, production-ready database that handles multiple users and connections better than SQLite. I created a new PostgreSQL database from Render dashboard, and Render gave me an "Internal Database URL" (a special link my app uses to connect to the database).

* **Setting SQLALCHEMY_DATABASE_URI Env Variable**:  I took the Internal Database URL from Render and added it as an environment variable named db (which my code reads as os.environ.get("db")). Now my app uses PostgreSQL instead of SQLite. The database is hosted on Render's servers, not on my computer, so it works even when my computer is off.

* **PostgreSQL vs SQLite**: SQLite works great for local development because it's simple and file-based. But for live deployment, PostgreSQL is better because it handles multiple users, has better security, works well with cloud platforms, and supports more advanced features. Both databases use the same SQLAlchemy code - I just had to change the SQLALCHEMY_DATABASE_URI from sqlite:///posts.db to the PostgreSQL URL.

## How It Works/Deployment Process

* **Prepare Code for Deployment**: I made sure my main.py reads database URL from environment variable using os.environ["db"] instead of a hardcoded SQLite path. I created a requirements.txt file with all my Python packages (Flask, SQLAlchemy, Flask-Login, gunicorn, psycopg2-binary, etc.). I updated my .gitignore to exclude local database files and secret files.

* **Push Code to GitHub**: I committed and pushed my project to remote repository of all my changes using git commands. Now My code is now on GitHub.

* **Create PostgreSQL Database on Render**: I went to Render dashboard, clicked "New +" → "PostgreSQL". Render created a free database and gave me a "Internal Database URL" which looks like postgresql://username:password@host:port/database. I copied this URL.

* **Create Web Service on Render**: I clicked "New +" → "Web Service", connected my GitHub, selected my blog repository. Render showed me a configuration page. I made sure all the configuration is correct including environment variable and project file path and clicked "Create Web Service.

* **Trigger Deploy**: After adding environment variables, I manually triggered a new deployment by clicking Deploy latest commit and restart service. Render pulled my code, installed dependencies, and started my app with gunicorn.

* **Access Live Website**: After deployment succeeded, Render gave me a URL: https://my-peronal-blog-website.onrender.com. Anyone in the world can now visit my blog website!


## Highlights

* **Live Deployment**: Successfully deployed my blog website to Render.com so anyone can access it online.
* **WSGI with Gunicorn**: Learned to use Gunicorn as a production WSGI server instead of Flask's built-in server.
* **PostgreSQL Database**: Switched from SQLite to PostgreSQL for better performance and reliability in production.
* **.gitignore Updated**: Added __pycache__, .env, *.db, instance/ to keep secrets and local files out of GitHub.
* **Render Platform**: Learned to use Render as a hosting provider connecting GitHub, creating web services, managing environment variables, and deploying website.

