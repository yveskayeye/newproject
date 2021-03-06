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


class Appointment(UserMixin, db.Model):

    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    mobile = db.Column(db.String(120),  nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.name

class Record(UserMixin, db.Model):

    __tablename__ = "records"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    address = db.Column(db.String(120),  nullable=False)
    blood_type = db.Column(db.String(120),  nullable=False)
    age = db.Column(db.String(120),  nullable=False)
    allergies = db.Column(db.String(120), nullable=False)
    number_children = db.Column(db.String(120), nullable=False)
    last_birth = db.Column(db.String(120), nullable=False)
    medical_condition = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.name

class RecordTwo(UserMixin, db.Model):

    __tablename__ = "recordsTwo"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    address = db.Column(db.String(120),  nullable=False)
    blood_type = db.Column(db.String(120),  nullable=False)
    age = db.Column(db.String(120),  nullable=False)
    systolic_BP = db.Column(db.String(120),  nullable=False)
    diastolic_BP = db.Column(db.String(120),  nullable=False)
    blood_sugar = db.Column(db.String(120),  nullable=False)
    body_temp = db.Column(db.String(120),  nullable=False)
    heart_rate = db.Column(db.String(120),  nullable=False)
    risk_level = db.Column(db.String(120),  nullable=False)
    allergies = db.Column(db.String(120), nullable=False)
    number_children = db.Column(db.String(120), nullable=False)
    last_birth = db.Column(db.String(120), nullable=False)
    medical_condition = db.Column(db.String(120), nullable=False)
    miscarriage = db.Column(db.String(80),  nullable=False)
    still_birth = db.Column(db.String(120),  nullable=False)
    premature_birth = db.Column(db.String(120),  nullable=False)
    pre_clamsia = db.Column(db.String(120),  nullable=False)
    gestation_diabetes = db.Column(db.String(120), nullable=False)
    hiv_status = db.Column(db.String(120), nullable=False)
    sugar_levels = db.Column(db.String(120), nullable=False)
    weight = db.Column(db.String(120), nullable=False)
    prev_dev = db.Column(db.String(120), nullable=False)
    id_number = db.Column(db.String(120), nullable=False)
    marital_status = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.name
