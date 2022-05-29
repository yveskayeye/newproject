from flask import Blueprint, render_template, session

home_bp = Blueprint("home_bp", __name__, template_folder="templates",
                    static_folder="static")



@home_bp.route("/", methods=["GET", "POST"])
def home():
    name = session.get("name")
    last_name = session.get("last_name")
    return render_template("home/index.html", name=name, last_name=last_name)

@home_bp.route("/patient", methods=["GET", "POST"])
def patient():
    name = session.get("name")
    last_name = session.get("last_name")
    return render_template("home/patient_settings.html" , name=name, last_name=last_name)

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