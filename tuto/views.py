from .app import app
from flask import render_template

@app.route("/")
def home():
    return render_template(
        "home.html",
        title="Hello World!",
        names = ["Pierre", "Paul", "Corinne"])

import yaml, os.path
data = yaml.load(
    open(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data.yml"
        )
    )
)

@app.route("/books/")
def books():
    return render_template(
        "books.html",
        books=data
    )
