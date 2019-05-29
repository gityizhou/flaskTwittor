from flask import render_template, redirect, url_for
from twittor.forms import LoginForm


def index():
    name = {'username': 'Joey'}
    post = [
        {'author': {'username': 'C'}, 'body': 'hello, my name is C'},
        {'author': {'username': 'Java'}, 'body': 'Today is a good day'},
        {'author': {'username': 'C#'}, 'body': 'I should review my CITS5505'},
        {'author': {'username': 'Ruby'}, 'body': 'cheers'},
        {'author': {'username': 'Python'}, 'body': 'Hello world!'},
    ]
    return render_template('index.html', name=name, post=post)


def login():
    # set csrf -> False
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        # redirect 重定向
        # url_for: find the url which is bind with index function
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)