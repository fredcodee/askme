from flask import Flask, Blueprint, redirect, render_template, request, flash, jsonify, url_for, abort
from flask_login import LoginManager, login_required, current_user
from app.models import User, Questions
from app import db


main = Blueprint('main', __name__)


@main.route("/", methods=['POST','GET'])
def home():
  if request.method == 'POST':
    selection = request.form.get("selection")
    #show questions
    if selection == "UQ":
      questions= Questions.query.filter_by(answer=" ").all()
    elif selection == "AQ":
      pass
    elif selection == "ALQ":
      questions= Questions.query.all()

    return(render_template("home.html", questions=questions))
  else:
    questions= Questions.query.all()
    return(render_template("home.html",questions=questions))

@main.route("/ask", methods=['POST','GET'])
#@login_required
def ask():
  experts= User.query.filter_by(expert=True)
  if request.method == "POST":
    user_question = request.form.get("question")
    expert = request.form.get("experts")

    return(render_template("ask.html", experts=experts))
  else:
    return(render_template("ask.html"))
  

@main.route("/answer", methods=['POST','GET'])
@login_required
def answer():
  pass

