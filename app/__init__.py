from flask import Flask
from .config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
db= SQLAlchemy(app)

login_manager= LoginManager(app)

login_manager.login_view='login'

app.config['SECRET_KEY']= "hello"
app.config.from_object(DevConfig)

from app import views