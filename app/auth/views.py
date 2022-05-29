from flask import Blueprint, redirect, render_template, flash, session, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from ..main import db
from .forms import LoginForm, SignupForm


auth_bp = Blueprint("auth_bp", __name__, template_folder="templates",
                    static_folder="static")



@auth_bp.route("/", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        
        user = User.query.filter_by(email=login_form.email.data).first()
        session["name"] = user.name
        session["last_name"] = user.last_name
       
        if user.is_admin:
            login_user(user)
            return redirect(url_for("home_bp.home"))
        if user is not None:
            if check_password_hash(user.password, login_form.password.data):
                login_user(user)

            return redirect(url_for("home_bp.home"))
        else:
            flash("Invalid email or password", "error") 
                   
    return render_template("auth/login.html", form=login_form)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    signup_form = SignupForm()
    # print(signup_form.validate_on_submit())
    if signup_form.validate_on_submit():
        # print("here")
        user = User(
            email=signup_form.email.data, 
            password=generate_password_hash(signup_form.password.data, method="sha256"),
            name=signup_form.name.data,
            last_name=signup_form.last_name.data
            )

        db.session.add(user)
        db.session.commit()

        flash("Registered successfully! You may now login.", category="success")
        return redirect(url_for("auth_bp.login"))

    return render_template("auth/register.html", form=signup_form)


@auth_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot():
    return render_template("auth/forgot-password.html")

@auth_bp.route("/404", methods=["GET", "POST"])
def f404():
    return render_template("auth/404.html")

@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()
    flash("You have successfully been logged out")

    return redirect(url_for("auth.login"))