from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    type = StringField(label="Type", validators=[DataRequired()])
    item_discription = StringField(label="Discription", validators=[DataRequired()])
    condition = StringField(label="Condition", validators=[DataRequired()])
    serial = StringField(label="Serial Number", validators=[DataRequired()])
    date_manufactured = StringField(label="Date Manufactured", validators=[DataRequired()])
    cost = StringField(label="Cost", validators=[DataRequired()])
    purchase_date = StringField(label="Purchase Date", validators=[DataRequired()])
    submit = SubmitField(label="Save")

class AppointForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    mobile = StringField(label="Name", validators=[DataRequired()])
    email = StringField(label="Name", validators=[DataRequired()])
    submit = SubmitField(label="Confirm")

class RecordForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    age = StringField(label="Age", validators=[DataRequired()])
    address = StringField(label="Address", validators=[DataRequired()])
    blood_type = StringField(label="Blood type", validators=[DataRequired()])
    systolic_BP = StringField(label="Systolic BP", validators=[DataRequired()])
    diastolic_BP = StringField(label="Diastolic BP", validators=[DataRequired()])
    blood_sugar = StringField(label="Blood sugar", validators=[DataRequired()])
    body_temp = StringField(label="Body temperature", validators=[DataRequired()])
    heart_rate = StringField(label="Heart rate", validators=[DataRequired()])
    number_children = StringField(label="Number of children", validators=[DataRequired()])
    last_birth = StringField(label="Last birth", validators=[DataRequired()])
    allergies = StringField(label="Allergies", validators=[DataRequired()])
    medical_condition = StringField(label="Medical conditions", validators=[DataRequired()])
    miscarriage = StringField(label="Miscarriages", validators=[DataRequired()])
    still_birth = StringField(label="Still Births", validators=[DataRequired()])
    premature_birth = StringField(label="Premature Births", validators=[DataRequired()])
    pre_clamsia = StringField(label="Pre clamsia", validators=[DataRequired()])
    gestation_diabetes = StringField(label="Gestation Diabetes", validators=[DataRequired()])
    hiv_status = StringField(label="HIV Status", validators=[DataRequired()])
    sugar_levels = StringField(label="Sugar Levels", validators=[DataRequired()])
    weight = StringField(label="Weight", validators=[DataRequired()])
    prev_dev = StringField(label="Previous Delivery Mode ", validators=[DataRequired()])
    id_number = StringField(label="ID Number", validators=[DataRequired()])
    marital_status = StringField(label="Marital Status", validators=[DataRequired()])
    submit = SubmitField(label="Add record")