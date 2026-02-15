from flask import Blueprint, redirect, render_template, flash, url_for
from ..extensions import db, bcrypt
from ..models.user import User
from ..forms import RegistrationFrom, LoginForm
from ..functions import save_picture

user = Blueprint('user', __name__)

@user.route('/user/register')
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        avatar_filename = save_picture(form.avatar.data)
        user = User(name=form.name.data, login=form.login.data, avatar=avatar_filename, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Добро пожаловать, {form.login.data}! Вы зарегистрированы!", "success")
        return redirect(url_for('user.login'))
    else:
        flash(f"При регистрации произошла ошибка", "danger")
        print('Error while registration')
    return render_template('user/register.html', form=form)


@user.route('/user/login')
def login():
    form = LoginForm()
 
    return render_template('user/login.html', form=form)