from flask_script import Manager
from flask_migrate import MigrateCommand
from twittor import create_app


app = create_app()
manager = Manager()
manager.add_command('db', MigrateCommand)  # add migrate command 'db'

if __name__ == "__main__":
    manager.run()