from app import app,db
from flask import render_template
from .forms import LoginForm
from flask import render_template,redirect,url_for,flash,request,abort
from werkzeug.security import generate_password_hash,check_password_hash #used to hash password to unreadable string
from flask_login import login_required,logout_user,login_user,current_user
from app.models import model

User= model.User
@app.route('/')
def homepage():
    db.create_all()
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and (user.password==form.password.data):
            login_user(user,)
            next_page=request.args.get('next')
            flash('Login Successfully','success')
            return redirect(next_page) if next_page else redirect (url_for('homepage'))
        flash('Invalid email or password','success')
    return render_template('authentication/login.html',form = form)