from flask import Flask, make_response
from flask_script import Manager

app = Flask(__name__)
# +3
manager = Manager(app)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'


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


if __name__ == '__main__':
    manager.run()