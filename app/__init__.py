from flask import Flask
from .config import DevConfig

app = Flask(__name__)
app.config['SECRET_KEY']= "hello"
app.config.from_object(DevConfig)

from app import views