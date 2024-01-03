from main import db, login_manager, bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    surname = db.Column(db.String(length=50), nullable=True)
    email = db.Column(db.String(length=50), nullable=False)
    message = db.Column(db.String(),nullable=False)

class Articles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    text = db.Column(db.String(), nullable=False)

class Projects(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    link = db.Column(db.String(), nullable=False)
    text = db.Column(db.String(), nullable=False)

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def chech_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
