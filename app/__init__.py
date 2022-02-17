from flask import Flask
from .config import DevConfig, Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_uploads import UploadSet,configure_uploads,IMAGES




app = Flask(__name__)

# Configs for profile and db ur
app.config.from_object(DevConfig)
app.config['SECRET_KEY']= Config.SECRET_KEY
app.config['UPLOADED_PHOTOS_DEST']= Config.UPLOADED_PHOTOS_DEST
# End of Configs

db = SQLAlchemy()
Migrate(app,db)
# Profile/account 
photos = UploadSet('photos',IMAGES)
# End of profile/account instantiating

# bootstrap.init_app(app)
db.init_app(app)

# Profile/account 
configure_uploads(app,photos)
login_manager= LoginManager(app)
login_manager.login_view='login'


from app import views, models