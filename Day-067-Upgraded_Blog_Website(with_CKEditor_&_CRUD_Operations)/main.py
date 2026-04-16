from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import URLField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from pathlib import Path
from smtplib import SMTP
import os

EMAIL = os.environ["email"]
PASSWORD = os.environ["password"]


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["secret_key"]
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Defines a WTForm for creating/editing blog posts with validation for title, subtitle, author, image URL, and CKEditor-powered body content.
class BlogForm(FlaskForm):
    title = StringField('Blog Post Title', render_kw={"class": "form-label"},
                        validators=[DataRequired(message="Please fill out this field.")])
    subtitle = StringField('Subtitle', render_kw={"class": "form-label"},
                           validators=[DataRequired(message="Please fill out this field.")])

    author = StringField('Your Name', render_kw={"class": "form-label"},
                         validators=[DataRequired(message="Please fill out this field.")])

    img_url = URLField('Blog Image URL', render_kw={"class": "form-label"},
                       validators=[DataRequired(message="Please fill out this field."),
                                   Length(min=8, max=255)])
    body = CKEditorField('Blog Content', render_kw={"class": "form-label"})

    submit = SubmitField('SUBMIT POST', render_kw={"class": "submit_button"})


# Represents a blog post entity in the database with fields for title, subtitle, publication date, content, author, and image URL.
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# Getting the instance folder path
instance_path = Path(app.instance_path)
db_path = instance_path / 'posts.db'


def send_mail(message_data) :
    """this function will create the secure connection between sender and receiver using smtp module and take input of weather condition and send the mail."""

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    with SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg=f"Subject: New Message! \n\n{message_data}")


def create_database():

    # Checking if the database file exist or not as per that new database will be created
    if not db_path.exists():
        with app.app_context():
            db.create_all()

        print(f'Database created successfully!')

    else:
        try:
            print(f'Database already exists at:, {db_path}')
            print(f'Skipping creation.')

        except OSError:
            pass


def read_blogs_data():
    """this function will read the old data from database of posts and return the blogs obj"""

    blog_data = db.session.execute(
        db.select(BlogPost).order_by(BlogPost.id))  # here we are reading the old movies data so we can use them.
    blogs = blog_data.scalars()

    return blogs

@app.route('/')
def get_all_posts():
    """this route is responsible for rendering the all blog posts in the home page."""

    create_database()
    blog_obj = read_blogs_data()
    posts = [blog for blog in blog_obj]

    return render_template("index.html", all_posts=posts)


@app.route('/show_post/<int:post_id>')
def show_post(post_id):
    """this route is responsible for rendering the blog on which user has clicked on it."""

    requested_blog_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_blog_post)


@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    """this route is responsible for creating a new blog post in the blog website."""

    form = BlogForm()

    # here it will render the mak-post page
    if request.method == "GET":
        return render_template("make-post.html", form=form)

    # here it will render the home page with the new post added in the database and also renders that new post in the home page.
    elif request.method == "POST":
        if form.validate_on_submit() and form.submit.data == True:
            dt = date.today()
            current_date = dt.strftime("%A %d, %Y")

            new_blog = BlogPost(
                title=request.form.get("title"),
                subtitle=request.form.get("subtitle"),
                img_url=request.form.get("img_url"),
                body=request.form.get("body"),
                author=request.form.get("author"),
                date=current_date,
            )

            db.session.add(new_blog)
            db.session.commit()
            print("new blog added in the database successfully")

            return redirect(url_for('get_all_posts'))


@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    """this route is responsible for rendering the blog post which we want to edit with pre populate all the things and update the blog post when user clicks on submit button."""

    blog_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    if request.method == 'GET':       # this will render the eidt-post page with pre popluate blog details.

        edit_form = BlogForm(
            title=blog_post.title,
            subtitle=blog_post.subtitle,
            img_url=blog_post.img_url,
            author=blog_post.author,
            body=blog_post.body,
        )
        return render_template("make-post.html", id=post_id, form=edit_form)

    elif request.method == 'POST':    # this will render the show post page with the updated blog post details.

        blog_post.title = request.form['title']
        blog_post.subtitle = request.form['subtitle']
        blog_post.img_url = request.form['img_url']
        blog_post.author = request.form['author']
        blog_post.body = request.form['body']

        db.session.commit()

        print("Edited blog details successfully updated in the database")
        return redirect(url_for('show_post', post_id=blog_post.id))



@app.route("/delete/<int:post_id>")
def delete_blog(post_id):
    """this route is responsible for deleting the blog post when user clicks on the X in the blog post."""

    blog_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(blog_post)
    db.session.commit()

    print("The requested blog post is being successfully deleted.")
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    """this route is responsible for rendering the about page."""

    return render_template("about.html")


@app.route("/contact" , methods = ["GET","POST"])
def contact():
    """this route is responsible for rendering the contact page."""

    if request.method == 'GET':
        return render_template("contact.html")

    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_no = request.form['phone']
        message = request.form['message']

        message_data = f'Name: {name}\nEmail: {email}\nPhone_no: {phone_no}\nMessage: {message}'

        send_mail(message_data)

        msg = "successful"
        return render_template("contact.html",
                               successful_msg=msg)  # once the message sent successful this will render contact.html page and show succesful sent message


if __name__ == "__main__":
    app.run(debug=True, port=5003)
