from flask import Flask, render_template

# render_template: flaks use jinja, server side rendering

app = Flask(__name__)

# @app.route('/') is a decorator
# app is an instance of the class Flask
# when it runs, it listens for requests, and if the route matches a decorator, it executes the corresponding function.
# then a request object is passed to the method
# the return of the function becomes the response


@app.route('/index')
def hello_world():
    name = {'username': 'Joey'}
    post = [
        {'author': {'username': 'C'}, 'body': 'hello, my name is C'},
        {'author': {'username': 'Java'}, 'body': 'Today is a good day'},
        {'author': {'username': 'C#'}, 'body': 'I should review my CITS5505'},
        {'author': {'username': 'Ruby'}, 'body': 'cheers'},
        {'author': {'username': 'Python'}, 'body': 'Hello world!'},
    ]
    return render_template('index.html', name=name, post=post)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
