from app import app,db,photos
from flask import render_template
from .forms import LoginForm,RegisterForm
from flask import render_template,redirect,url_for,flash,request,abort
from werkzeug.security import generate_password_hash,check_password_hash #used to hash password to unreadable string
from flask_login import login_required,logout_user,login_user,current_user
from app.models import model

User= model.User

@app.route('/')
def homepage():
    db.create_all()
    return render_template('index.html')

# login route
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next') # request.args.get('next')
            flash(f"{ user.username } Logged successfull!", 'success')

            return redirect(next_page) if next_page else redirect(url_for('homepage'))
       
    return render_template('authentication/login.html',form = form)

# register route
@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
        username = form.username.data,
        email = form.email.data,
        password = generate_password_hash(form.password.data))

        db.session.add(user)
        db.session.commit()
        flash('Account created successfully', 'Success')

        return redirect(url_for('register'))

    return render_template('authentication/register.html',form = form)


#account/profile route
@app.route('/account/user/<uname>',methods=['POST', 'GET'])
def account(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/account.html', user = user)


@app.route('/account/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('account',uname=uname))

#account/profile route ending


# logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))
    