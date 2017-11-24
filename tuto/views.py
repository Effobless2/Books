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
        title = "Les Livres",
        books = get_sample()
    )

from flask_bootstrap import Bootstrap

app.config['BOOTSTRAP_SERVE_LOCAL'] = True

Bootstrap(app)
