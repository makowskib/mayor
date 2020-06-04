from mayors import app, db
from flask import render_template
from mayors.models import Mayors


@app.route("/")
def hello():
    db.create_all()
    return render_template('index.html')

