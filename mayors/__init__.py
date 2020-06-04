from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
app.static_folder = 'static'

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from mayors import routes
