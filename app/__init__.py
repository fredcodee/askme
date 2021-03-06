from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
  app = Flask(__name__)

  app.config['SECRET_KEY'] = 'ASpire2begreat'
  app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://dxbiulggscgjps:d7441e3003829355f6dd7672711e13e32cd5acf90e098af2b2bd68c59dd010e8@ec2-52-71-231-180.compute-1.amazonaws.com:5432/d6sv66u1928ne4"

  db.init_app(app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  from app.models import User

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
