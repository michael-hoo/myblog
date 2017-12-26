from flask import Flask, make_response, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
# +3
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
@app.route('/index')
def index():
    name = 'nathan hu'
    dict = {'age': 25, 'gender': '男', 'salary': 8000}
    return render_template('index.html', name=name, dict=dict,
                           current_time=datetime.utcnow())


# +1
@app.route('/user/<name>')
def user(name):
    return 'Hello, %s' % name


# +2
@app.route('/cookie')
def test_make_response():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('hunan', '25')
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    manager.run()
