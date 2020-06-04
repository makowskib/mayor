from mayors import app, db
from flask import render_template, url_for
from mayors.models import Mayors


@app.route("/")
def index():
    results = Mayors.query.all()
    return render_template("index.html", results=results)

