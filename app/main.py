from flask import Flask, Blueprint, redirect, render_template, request, flash, jsonify, url_for, abort
from flask_login import LoginManager, login_required, current_user
from app.models import User
from app import db


main = Blueprint('main', __name__)
