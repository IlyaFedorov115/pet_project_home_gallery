from ..extensions import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), default='user')
    avatar = db.Column(db.String(200))
    name = db.Column(db.String(50))
    login = db.Column(db.String(50))
    password = db.Column(db.String(50))
    date = db.Column(db.DateTime, default=datetime.utcnow)