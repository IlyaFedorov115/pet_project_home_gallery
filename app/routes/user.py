from flask import Blueprint
from ..extensions import db
from ..models.user import User

user = Blueprint('user', __name__)

@user.route('/user/<name>')
def create_user(name):
    user_ = User(name=name)
    db.session.add(user_)
    db.session.commit()
    return 'USER Created!'