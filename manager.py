from datetime import datetime

from flask_login import current_user
from flask_script import Manager
from flask_migrate import MigrateCommand
from twittor import create_app, db

app = create_app()
manager = Manager()
manager.add_command('db', MigrateCommand)  # add migrate command 'db'

from twittor.models import User, Tweet, followers


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Tweet': Tweet, 'followers': followers}


@app.before_request    # 记录用户最后查看时间
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


if __name__ == "__main__":
    manager.run()
