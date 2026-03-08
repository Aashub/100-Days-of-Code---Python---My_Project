from flask import Flask, render_template
import requests


BLOG_URL = " https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

@app.route('/') # to render home page
def home():

    blog_response = requests.get(url= BLOG_URL)
    blog_data = blog_response.json()

    return render_template("index.html", blog = blog_data)

@app.route('/post/<int:num>') # to render clicked post page
def get_post(num):
    """when this function get called when user clicks on the read link in home page, it will load that post page."""

    blog_response = requests.get(url= BLOG_URL)
    blog_data = blog_response.json()

    return render_template("post.html", blog = blog_data, post_num = num)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
