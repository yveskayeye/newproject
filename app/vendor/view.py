from flask import Blueprint

vendor_bp = Blueprint("vendor_bp", __name__, template_folder="templates",
                    static_folder="static")