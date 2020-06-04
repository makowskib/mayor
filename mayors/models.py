from mayors import db


class Mayors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
