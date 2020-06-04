from mayors import app, db
from flask import render_template, url_for, redirect
from mayors.models import Mayors


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recipients")
def recipients():
    results = Mayors.query.all()
    return render_template("recipients.html", results=results)

