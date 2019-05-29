from datetime import datetime
# generate password hash, check password hash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin  # 提供一些用户session管理的基本方法

from twittor import db, login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    tweets = db.relationship('Tweet', backref='author', lazy='dynamic')

    def __repr__(self):
        return 'id={}, username={}, email={}, password_hash={}'.format(
            self.id, self.username, self.email, self.password_hash
        )

    # set the password hash
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # check the password hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader     # this decorator maps an id to a user
def load_user(id):
    return User.query.get(int(id))


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "id={}, body={}, create_time={}, user_id={}".format(
            self.id, self.body, self.create_time, self.user_id
        )
