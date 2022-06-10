from flask import Blueprint, render_template
from datetime import datetime
from ..models import Appointment, RecordTwo

inventory_bp = Blueprint("inventory_bp", __name__, template_folder="templates",
                        static_folder="static")

@inventory_bp.route("/")
def inventory():
    appointments = Appointment.query.all()
    for appointment in appointments:
        appointment.date = datetime.fromtimestamp(float(appointment.date))
    return render_template("inventory/inventory.html", appointments=appointments)

@inventory_bp.route("/stats")
def stats():
    return render_template("inventory/stats.html",)

@inventory_bp.route("/patients")
def patients():
    record2 = RecordTwo.query.all()
    for record in record2:
        record["risk_level"] = get_risk(record)

    return render_template("inventory/patients.html", records=record2)

def get_risk(record):
    pass