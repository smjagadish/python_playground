import datetime

import pytz
from flask import Flask, render_template , request,redirect,url_for,flash
from flask_bcrypt import Bcrypt
from logging import INFO
from forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy
from models import db , login_manager



app = Flask(__name__)
app.logger.setLevel(INFO)
app.secret_key = b'Ab\x95(?\x9b\x86\xb4'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'  #using sqlite

 #db initialization
db.init_app(app)
login_manager.init_app(app)
with app.app_context():
    db.drop_all()

    db.create_all()

bcrypt = Bcrypt(app)
from flask_playground import  routes