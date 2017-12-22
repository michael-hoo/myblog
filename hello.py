from flask import Flask, request, make_response, redirect
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
@app.route('/index')
def index():
    return redirect('https://www.baidu.com')


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


# response 返回状态码
@app.route('/400')
def bad_request():
    return '<h1>Bad Request</h1>', 400


# 从 request 中获取信息
@app.route('/user-agent')
def user_agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


# 设置 cookie
@app.route('/set-cookie')
def set_cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


if __name__ == '__main__':
    manager.run()
