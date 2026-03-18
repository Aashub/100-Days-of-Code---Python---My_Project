from flask import Flask, render_template
import requests

BLOG_ENDPOINT = "https://api.npoint.io/1937bc8b8e40c31b0db0"

app = Flask(__name__)

blog_response = requests.get(url=BLOG_ENDPOINT)
blog_data = blog_response.json()

@app.route('/')
def home():
    """the decorator and this function will help in render the home page of website."""

    return render_template("index.html", all_blog_post = blog_data)

@app.route('/<string:page>')
def show_page(page):
    """this function will help in render different pages like home, about and contact page. of blog website"""

    if page == "home":
        return render_template("index.html", all_blog_post = blog_data)
    elif page == "about":
        return render_template("about.html")
    elif page == "contact":
        return render_template("contact.html")

@app.route('/<int:num>')
def show_blog(num):
    """this function will help in render the blog post page when user clicks on the title & subtitle."""

    return render_template("post.html", all_blog_post=blog_data, post_num = num)


if __name__ == "__main__":
    app.run(debug=True)

