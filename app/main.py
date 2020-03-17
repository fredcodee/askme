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

