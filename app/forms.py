from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import Length, DataRequired, EqualTo, ValidationError,Email
from app.models.model import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()],render_kw={"placeholder": "Username"})
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=50)],render_kw={"placeholder": "Password"})
    submit = SubmitField("Log In")
    
class RegisterForm(FlaskForm):
    '''
    class to create forms for registration and its input   
    '''
    
    # fields that are to be displayed in the register form
    
    username= StringField('Username',validators=[DataRequired()],render_kw={"placeholder": "Username"})
    email=StringField(' Email',validators=[DataRequired(),Email(),Length(min=5,max=30)],render_kw={"placeholder": "Email"})
    password=PasswordField('Password',validators=[DataRequired(),Length(min=5,max=50)],render_kw={"placeholder": "Password"})
    submit=SubmitField('Sign Up')
    
# a function to check if a email exist to prompt user to enter another one
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username already taken!')

 # a function to check if a username exist to prompt user to enter another one
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email already taken!')