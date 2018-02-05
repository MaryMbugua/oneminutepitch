from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    pitchcontent = db.Column(db.String(255))
    pitchcategory = db.Column(db.String(255))

    def __repr__(self):
        return f' pitch {self.title}'

    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()