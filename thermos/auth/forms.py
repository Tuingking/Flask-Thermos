from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length, Regexp, Email

from ..models import User

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')

class SignupForm(Form):
    username = StringField('Username',
                           validators=[
                               DataRequired(),
                               Length(3, 80),
                               Regexp('^[A-Za-z0-9_]{3,}$',
                                      message="Username consist of numbers, letters and underscores.")])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password2',
                                         message="Password must match.")])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(1, 120), Email()])

    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError("There already is a user with this email address.")

    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError("This Username is already taken.")
