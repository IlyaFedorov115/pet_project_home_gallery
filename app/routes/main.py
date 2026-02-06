from flask import Blueprint, render_template


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def create_post():
    return render_template('main/index.html')