from flask_login import UserMixin
from datetime import datetime
from app import db


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True, nullable=False)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(100))
  expert = db.Column(db.Boolean)
  qnas = db.relationship('Questions', backref='qna', lazy=True)

class Questions(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
  expert_id = db.Column(db.Integer)
  dateposted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  question = db.Column(db.String)
  answer = db.Column(db.String)
  expert_name = db.Column(db.String)
