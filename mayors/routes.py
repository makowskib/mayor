import smtplib, email, sendgrid, os
from mayors import app, db
from flask import render_template, url_for
from mayors.models import Mayors
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipients")
def recipients():
    results = Mayors.query.all()
    return render_template("recipients.html", results=results)

@app.route("/mailtest")
def mailtest():
    message = Mail(
        from_email='cushmanalex@gmail.com',
        to_emails='to@example.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    sg = SendGridAPIClient(app.config.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return render_template('index.html')

