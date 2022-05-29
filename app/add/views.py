from crypt import methods
from operator import methodcaller
from flask import Blueprint, flash,render_template
from flask_login import login_required
from ..models import Asset, db
from .forms import AddForm

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
    return render_template("add/add_med.html")

@add_bp.route("/checkup", methods=["GET", "POST"])
def checkup():
    return render_template("add/checkup.html")

@add_bp.route("/doctor", methods=["GET", "POST"])
def doctor():
    return render_template("add/doctor.html")

@add_bp.route("/new_med", methods=["GET", "POST"])
def new_med():
    return render_template("add/new_med.html")

@add_bp.route("/scan", methods=["GET", "POST"])
def scan():
    return render_template("add/scan.html")