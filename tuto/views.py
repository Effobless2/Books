from .app import app
from flask import render_template
from .models import get_sample

@app.route("/")
def home():
    return render_template(
        "home.html",
        title="Hello World!",
        names = ["Pierre", "Paul", "Corinne"])

@app.route("/books/")
def books():
    return render_template(
        "books.html",
        books = get_sample()
    )
