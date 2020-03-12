from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
  app = Flask(__name__)

  app.config['SECRET_KEY'] = 'ASpire2begreat'
  app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://eeogiqesireozj:0db4a21e73d16f98aed54b24533ff8ef045c126bd307e86969d2a2e62ca08bb4@ec2-3-91-112-166.compute-1.amazonaws.com:5432/da2nhc74op3ghg"

  db.init_app(app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  from .models import User

  @login_manager.user_loader
  def load_user(user_id):
    return(User.query.get(int(user_id)))

  # blueprint for auth routes in our app
  from app.auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  # blueprint for non-auth parts of app
  from app.main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return(app)
