# imported classes
from app import db
from app import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# our user database table model/architecture
class User(db.Model,UserMixin):
    __tablename__='user' #name of the table in the db
    
    # columns in Our User db table
    id= db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(50),unique = True)
    email=db.Column(db.String(150),unique = True)
    
    #profile photo path
    profile_pic_path = db.Column(db.String())
    #profile photo path end

    password=db.Column(db.String(150))
   
