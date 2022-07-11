from flask import Blueprint, render_template, session
from flask_login import login_required
from ..models import Appointment, Record

home_bp = Blueprint("home_bp", __name__, template_folder="templates",
                    static_folder="static")


@login_required
@home_bp.route("/", methods=["GET", "POST"])
def home():
    name = session.get("name")
    last_name = session.get("last_name")
    is_admin = session.get("is_admin")
    appoint = Appointment.query.filter_by(name=name)
    count = 0
    for _ in appoint:
        count += 1
    total_appoint = count
    return render_template("home/index.html", name=name, last_name=last_name, admin=is_admin, appoint_total=total_appoint)

@login_required
@home_bp.route("/admin", methods=["GET", "POST"])
def home_admin():
    name = session.get("name")
    last_name = session.get("last_name")
    return render_template("home/index2.html", name=name, last_name=last_name, admin=True)

@home_bp.route("/patient", methods=["GET", "POST"])
def patient():
    name = session.get("name")
    is_admin = session.get("is_admin")
    last_name = session.get("last_name")
    return render_template("home/patient_settings.html" , name=name, last_name=last_name, admin=is_admin)

@home_bp.route("/appoint", methods=["GET", "POST"])
def appoint():
    return render_template("home/appoint_settings.html")

@home_bp.route("/email", methods=["GET", "POST"])
def email():
    return render_template("home/email.html")

@home_bp.route("/profile", methods=["GET", "POST"])
def profile():
    return render_template("home/profile.html")

@home_bp.route("/preferences", methods=["GET", "POST"])
def preferences():
    return render_template("home/preferences.html")