from flask import Flask, session, redirect, url_for, flash
from flask import render_template, request, make_response
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


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


class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    manager.run()
