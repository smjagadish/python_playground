from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError
from models import User
from flask import flash

class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),length(min=2,max=20)])
    email = StringField('email',validators=[Email(),DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('sign up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            flash("User already registered, try with a different username")
            raise ValidationError()

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            flash("email already used,try with a different email")
            raise ValidationError()

class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    remember = BooleanField('remember_me')
    submit = SubmitField('login')