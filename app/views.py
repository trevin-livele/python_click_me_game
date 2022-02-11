from app import app
from flask import render_template
from .forms import LoginForm

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('authentication/login.html',form=form)

@app.route('/signup')
def register():
    return render_template('authentication/register.html')