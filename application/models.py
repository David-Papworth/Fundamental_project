from application import db

class Figure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    number_of_models = db.Column(db.Integer, nullable=False)
    faction = db.Column(db.String(120), nullable=False)
    army_id = db.Column(db.Integer, db.ForeignKey('army.id'), default="")

class Army(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), default="")
    figure = db.relationship('Figure', backref='army') 