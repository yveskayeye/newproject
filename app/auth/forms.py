from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import User

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="login")


class SignupForm(FlaskForm):
    name = StringField(label="name", validators=[DataRequired()])
    last_name = StringField(label="name", validators=[DataRequired()])
    email = StringField(label="Email Address", validators=[DataRequired(), Email()])
    password = StringField(label="Password", validators=[DataRequired(), EqualTo("repeat_password")])
    repeat_password = PasswordField("Repeat Password")
    submit = SubmitField(label="Register Account")

    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationErr("Email is already in use")