from flask_script import Manager, Server
from app import app,db
from flask_migrate import Migrate,MigrateCommand
from app.models.model import User
from app.config import DevConfig

app.config.from_object(DevConfig)

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db)


if __name__ == "__main__":
    manager.run()