from application import db

class Figure(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Amry(db.Model):
    id = db.Column(db.Integer, primary_key=True)