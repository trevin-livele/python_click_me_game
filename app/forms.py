from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField,BooleanField,Email
from wtforms.validators import Length, DataRequired, EqualTo, ValidationError,InputRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=50)])
    submit = SubmitField("Log In")

class SignupForm(FlaskForm):
    First_name = StringField(' first name',validators=[InputRequired(),Length(min=8 , max=15)])
    Last_name = StringField('last name',validators=[InputRequired(),Length(min=8 , max=15)])
    username = StringField('username',validators=[InputRequired(),Length(min=8 ,max=15)])
    email= StringField('email',validators=[InputRequired(),Email(message ='invalid email'),Length(min=8 ,max=15)])
    password =PasswordField('password',validators=[InputRequired(),Length(min=4 , max=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign Up')