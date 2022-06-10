from flask import Blueprint, flash,render_template, session
from flask_login import login_required
from ..models import Asset, db, Appointment, Record, RecordTwo
from .forms import AddForm, AppointForm, RecordForm
from datetime import datetime
from .email import send_email

add_bp = Blueprint("add_bp", __name__, template_folder="templates",
                    static_folder="static")


@add_bp.route("/", methods=["POST", "GET"])
@login_required
def add():
    add_form = AddForm()
    
    if add_form.validate_on_submit():
        asset = Asset(asset_tag=1234, name=add_form.name.data, type=add_form.type.data,
                        item_discription=add_form.item_discription.data, condition=add_form.condition.data,
                        serial=add_form.serial.data, date_manufactured=add_form.date_manufactured.data,
                        cost=add_form.cost.data, purchase_date=add_form.purchase_date.data)
        
        db.session.add(asset)
        db.session.commit()

        flash("Asset added succesfully", category="success")
        
    return render_template("add/add.html", form=add_form)


@add_bp.route("/add_med", methods=["GET", "POST"])
def add_med():
    form = RecordForm()
    name = session.get("name")
    last_name = session.get("last_name")

    if form.validate_on_submit():
        record = Record(
            name = form.name.data,
            age = form.age.data,
            address = form.address.data,
            blood_type = form.blood_type.data,
            number_children = form.number_children.data,
            last_birth = form.last_birth.data,
            allergies = form.allergies.data,
            medical_condition = form.medical_condition.data
        )

        db.session.add(record)
        db.session.commit()

        flash("Record added", category="success")
        
    return render_template("add/add_med.html", form=form, name=name, last_name=last_name)

@add_bp.route("/checkup", methods=["GET", "POST"])
def checkup():
    form = AppointForm()
    name = session.get("name")
    last_name = session.get("last_name")

    if form.validate_on_submit():
        tyme = get_date()
        appointment = Appointment(
            name = form.name.data,
            mobile = form.mobile.data,
            email = form.email.data,
            date = tyme
        )

        db.session.add(appointment)
        db.session.commit()

        flash("appointment will be booked and emailed to you shortly", category="success")
        send_email(tyme, form.email.data)

    return render_template("add/checkup.html", form=form, name=name, last_name=last_name)

@add_bp.route("/doctor", methods=["GET", "POST"])
def doctor():
    form = AppointForm()
    name = session.get("name")
    last_name = session.get("last_name")

    if form.validate_on_submit():
        tyme = get_date()
        appointment = Appointment(
            name = form.name.data,
            mobile = form.mobile.data,
            email = form.email.data,
            date = tyme
        )

        db.session.add(appointment)
        db.session.commit()

        flash("appointment will be booked and emailed to you shortly", category="success")
        send_email(tyme, form.email.data)

    return render_template("add/doctor.html", form=form, name=name, last_name=last_name)

@add_bp.route("/new_med", methods=["GET", "POST"])
def new_med():
    form = RecordForm()
    name = session.get("name")
    last_name = session.get("last_name")

    if form.validate_on_submit():
        record = Record(
            name = form.name.data,
            age = form.age.data,
            address = form.address.data,
            blood_type = form.blood_type.data,
            number_children = form.number_children.data,
            last_birth = form.last_birth.data,
            allergies = form.allergies.data,
            medical_condition = form.medical_condition.data
        )
        record2 = RecordTwo(
            name = form.name.data,
            age = form.age.data,
            address = form.address.data,
            blood_type = form.blood_type.data,
            number_children = form.number_children.data,
            last_birth = form.last_birth.data,
            allergies = form.allergies.data,
            medical_condition = form.medical_condition.data,
            miscarriage = form.miscarriage.data,
            still_birth = form.still_birth.data,
            premature_birth = form.premature_birth.data,
            pre_clamsia = form.pre_clamsia.data,
            gestation_diabetes = form.gestation_diabetes.data,
            hiv_status = form.hiv_status.data,
            sugar_levels = form.sugar_levels.data,
            weight = form.weight.data,
            prev_dev = form.prev_dev.data,
            id_number = form.id_number.data,
            marital_status =form.marital_status.data,
        )

        db.session.add(record)
        db.session.commit()
        db.session.add(record2)
        db.session.commit()

        flash("Record added", category="success")
    return render_template("add/new_med.html", form=form, name=name, last_name=last_name)

@add_bp.route("/scan", methods=["GET", "POST"])
def scan():
    name = session.get("name")
    last_name = session.get("last_name")
    form = AppointForm()

    if form.validate_on_submit():
        tyme = get_date()
        appointment = Appointment(
            name = form.name.data,
            mobile = form.mobile.data,
            email = form.email.data,
            date = tyme
        )

        db.session.add(appointment)
        db.session.commit()

        send_email(tyme, form.email.data)
        flash("appointment will be booked and emailed to you shortly", category="success")


    return render_template("add/scan.html", form=form, name=name, last_name=last_name)

def get_date():
    time = datetime.now()
    timestamp = datetime.timestamp(time)
    
    return timestamp + 5
