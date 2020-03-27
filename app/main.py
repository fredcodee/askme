from flask import Flask, Blueprint, redirect, render_template, request, flash, jsonify, url_for, abort
from flask_login import LoginManager, login_required, current_user
from app.models import User, Questions
from app import db


main = Blueprint('main', __name__)


@main.route("/", methods=['POST','GET'])
def home():
  unans=[]
  if current_user.expert:
    questions=Questions.query.filter_by(expert_id=current_user.id).all()
    for question in questions:
      if question.answer == " ":
        unans.append(question)
    badge=len(unans)
      
  if request.method == 'POST':
    selection = request.form.get("selection")
    #show questions
    if selection == "UQ":
      questions= Questions.query.filter_by(answer=" ").all()
    elif selection == "AQ":
      #get the  anwsered questions
      questions= Questions.query.filter(Questions.answer != " ").all()
    elif selection == "ALQ" or selection == "SL":
      questions=Questions.query.all()

    return(render_template("home.html", questions=questions,badge=badge))
  else:
    questions= Questions.query.all()
    return(render_template("home.html",questions=questions, badge=badge))

@main.route("/ask", methods=['POST','GET'])
@login_required
def ask():
  experts= User.query.filter_by(expert=True)
  if request.method == "POST":
    user_question = request.form.get("question")
    expert = request.form.get("experts")

    #get expert username
    name = User.query.get(int(expert))

    #add to database
    new_question = Questions(expert_id=int(expert),question=user_question,answer=" ",expert_name=name.username, qna=current_user)

    db.session.add(new_question)
    db.session.commit()

    flash("Question uploaded successfully")
    return(redirect(url_for("main.ask")))
  else:
    return(render_template("ask.html", experts=experts))

@main.route("/questions", methods=['POST','GET'])
@login_required
def questions():
  unanswered=[]
  if current_user.expert:
    questions=Questions.query.filter_by(expert_id=current_user.id).all()
    for question in questions:
      if question.answer == " ":
        unanswered.append(question)
    unanswered.reverse()
    return(render_template("question.html", logs=unanswered))
  else:
    abort(404)

@main.route("/answer/<idd>",methods=['POST','GET'])
@login_required
def answer(idd):
  if current_user.expert:
    if request.method== "POST":
      get_q= Questions.query.get(idd)
      get_a = request.form.get("answer")

      get_q.answer= get_a
      db.session.commit()
      return(redirect(url_for('main.questions')))
    else:
      get_q= Questions.query.get(idd)
      return(render_template("answer.html",get_q=get_q))
  else:
    abort(404)


@main.route("/profile", methods=['POST','GET'])
@login_required
def profile():
  if current_user.expert:
    get_log = Questions.query.filter_by(expert_id = current_user.id).all()
    ll=[]
    for log in get_log:
      if log.answer != " ":
        ll.append(log)
    get_log=ll
  else:
    get_log = Questions.query.filter_by(user_id = current_user.id).all()

  return(render_template("profile.html", get_log=get_log))

@main.route("/delete/<idd>")
@login_required
def delete(idd):
  get_details = Questions.query.get(idd)
  if current_user.expert:
    get_details.answer = " "
    db.session.commit()
    return(redirect(url_for('main.profile')))
  else:
    db.session.delete(get_details)
    db.session.commit()
    return(redirect(url_for('main.profile')))


@main.route("/admin", methods=['POST','GET'])
@login_required
def admin():
  users= User.query.all()
  questions=Questions.query.all()
  return(render_template("admin.html", users=users, questions=questions))
