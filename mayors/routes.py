import urllib
from urllib import parse
from mayors import app
from flask import render_template, url_for, redirect, request, flash
from mayors.models import Mayors


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        to = request.form.getlist('checkbox')
        if len(to) == 0:
            results = Mayors.query.all()
            flash('Please select at least one recipient')
            return redirect(url_for('index', results=results))
        body = request.form.get('body')
        subject = request.form.get('subject')
        link = "mailto:" + to[0] + "?BCC="
        for address in to[1:]:
            if address is not None:
                link += address + ","
        link = link[:-1] + "&Subject=" + urllib.parse.quote(subject) + "&Body=" + urllib.parse.quote(body)
        return redirect(url_for('mailto', link=link))
    results = Mayors.query.all()
    return render_template("index.html", results=results)


@app.route("/mailto/<link>", methods=['GET', 'POST'])
def mailto(link):
    return render_template("mailto.html", link=link)




