from flask import Flask

app = Flask(__name__)

# @app.route('/') is a decorator
# app is an instance of the class Flask
# when it runs, it listens for requests, and if the route matches a decorator, it executes the corresponding function.
# then a request object is passed to the method
# the return of the function becomes the response


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
