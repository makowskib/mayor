import urllib
from urllib import parse
from mayors import app, db
from flask import render_template, url_for, redirect, request
from mayors.models import Mayors


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        to = request.form.getlist('checkbox')
        print(to)
        return redirect(url_for('recipients', to=to))
    results = Mayors.query.all()
    return render_template("index.html", results=results)


@app.route("/email/<to>", methods=['GET', 'POST'])
def recipients(to):
    if request.method == "POST":
        body = request.form.get('body')
        subject = request.form.get('subject')
        fr = request.form.get('from')
        name = request.form.get('name')
        return redirect(url_for('mailTo'))
    return render_template("recipients.html", to=to)



