from flask import Blueprint, render_template, request, redirect
import re
from ..extensions import db
from ..models.post import Post

post = Blueprint('post', __name__)

@post.route('/post/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        teacher = request.form['teacher']
        subject = request.form['subject']
        student = request.form['student']

        post = Post(teacher=teacher, subject=subject, student=student)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(str(e))

        return "some"
    else:
        return render_template('post/create.html')