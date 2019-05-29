from flask import render_template, redirect, url_for, request
# login_user will set current user to the _specified user model
# current_user has a method is_authenticated to check if they have provided login credentials.
# and a method is_anonymous to check if this user is not log-in
from flask_login import login_user, current_user, logout_user, login_required
from twittor.forms import LoginForm, RegisterForm
from twittor.models import User, Tweet
from twittor import db


# use a decorator @login_required from Flask_Login to label the routes that require a login.
@login_required
def index():
    post = [
        {'author': {'username': 'C'}, 'body': 'hello, my name is C'},
        {'author': {'username': 'Java'}, 'body': 'Today is a good day'},
        {'author': {'username': 'C#'}, 'body': 'I should review my CITS5505'},
        {'author': {'username': 'Ruby'}, 'body': 'cheers'},
        {'author': {'username': 'Python'}, 'body': 'Hello world!'},
    ]
    return render_template('index.html', post=post)


def login():
    if current_user.is_authenticated:    # 如果当前用户已经登录
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():     # validate_on_submit() 如果能通过所有验证
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):  # check the username and password
            print('invalid username or password')
            return redirect(url_for('login'))
        login_user(u, remember=form.remember_me.data)
        next_page = request.args.get('next')  # 导入了flask中的request，获取下一页的重定向
        if next_page:
            return redirect(next_page)
        # redirect 重定向
        # url_for: find the url which is bind with index function
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)


def logout():
    logout_user()
    return redirect(url_for('login'))


def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        u = User(username=form.username.data, email=form.email.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)
