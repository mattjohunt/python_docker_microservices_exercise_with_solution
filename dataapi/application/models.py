from application import db

class Data(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(30), nullable=False)