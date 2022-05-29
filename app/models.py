from flask_login import UserMixin

from app.main import db, login_manager


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    name = db.Column(db.String(80),nullable=False, default="user")
    last_name = db.Column(db.String(80), nullable=False, default="new")
    
    def __repr__(self):
        return '<User %r>' % self.email


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Asset(db.Model):

    __tablename__ = "patients"

    patient_tag = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    item_discription = db.Column(db.String(80), nullable=False)
    condition = db.Column(db.String(80), nullable=False)
    serial = db.Column(db.String(80), unique=True, nullable=False)
    date_manufactured = db.Column(db.String(80), nullable=False)
    cost = db.Column(db.String(80), nullable=False)
    purchase_date = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class Flag(UserMixin, db.Model):

    __tablename__ = "info"

    id = db.Column(db.Integer, primary_key=True)
    flag = db.Column(db.String(80), unique=True, nullable=False)
    detail = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.flag
