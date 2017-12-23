from flask import Flask, request, make_response, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# response 返回状态码
@app.route('/400')
def bad_request():
    return '<h1>Bad Request</h1>', 400


# 自定义错误处理页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


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


@app.route('/macros')
def test_macros():
    a_list = ['Michael', 'Nathan', 'John', 'Susan']
    return render_template('test_macros.html', a_list=a_list)


if __name__ == '__main__':
    manager.run()
