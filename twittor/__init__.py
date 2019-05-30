from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager   # track secure sessions

from twittor.config import Config

db = SQLAlchemy()
migrate = Migrate()
# Finally, in app/__init__.py, an instance of LoginManager is created,
# and the login_view is set to the route login.
login_manager = LoginManager()
login_manager.login_view = 'login'   # 如果没登录则重定向到 login界面

from twittor.route import index, login, logout, register, user, page_not_found, edit_profile


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)  # db initialization
    login_manager.init_app(app)
    # replace the @decorator @app.route('/index')
    # configure route and add http methods
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'] )
    app.add_url_rule('/user/<username>', 'profile', user)
    app.add_url_rule('/edit_profile', 'edit_profile', edit_profile, methods=['GET', 'POST'])
    app.register_error_handler(404, page_not_found)
    return app


