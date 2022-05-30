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
    number_children = StringField(label="Number of children", validators=[DataRequired()])
    last_birth = StringField(label="Last birth", validators=[DataRequired()])
    allergies = StringField(label="Allergies", validators=[DataRequired()])
    medical_condition = StringField(label="Medical conditions", validators=[DataRequired()])
    submit = SubmitField(label="Add record")