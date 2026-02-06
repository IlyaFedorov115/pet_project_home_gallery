from flask import Blueprint
from ..extensions import db
from ..models.post import Post

post = Blueprint('post', __name__)

@post.route('/post/<subject>')
def create_post(subject):
    post_ = Post(subject=subject)
    db.session.add(post_)
    db.session.commit()
    return 'post Created!'