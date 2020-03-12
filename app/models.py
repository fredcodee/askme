from flask_login import UserMixin
from datetime import datetime
from hashlib import md5
from app import db


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True, nullable=False)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(100))
  reviews = db.relationship('Review', backref='feedback', lazy=True)

  def avatar(self, size):
    digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    return('https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size))
