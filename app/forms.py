from flask_wtf import FlaskForm
from wtforms import FileField, StringField, PasswordField, BooleanField , SubmitField, ValidationError
from flask_wtf.file import FileAllowed, DataRequired
from wtforms.validators import DataRequired, Length, EqualTo
from .models.user import User

class RegistrationFrom(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired(), Length(min=2, max=100)])
    login = StringField('Login', validators=[DataRequired(), Length(min=2, max=200)],render_kw={
        'class': 'form-control',
        'placeholder': 'Login'
    })
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    avatar = FileField('Upload your photo', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Log out')
    
    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('Данное имя пользователя уже занято!')

class LoginForm(FlaskForm):
    """Form to log in"""
    login = StringField('Login', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Log in")