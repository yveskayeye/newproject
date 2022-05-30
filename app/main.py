from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
import os


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
mail = Mail()

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_name)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["MAIL_SERVER"] = 'smtp.gmail.com'
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USERNAME"] = 'singleodin234@gmail.com'
    app.config["MAIL_PASSWORD"] = 'qw12dx$%'
    app.config["MAIL_TLS"] = False
    app.config["MAIL_SSL"] = True
    db.init_app(app)
    mail.init_app(app)
    

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page"
    login_manager.login_view = "auth_bp.login"

    

    # with app.app_context():
    #     db.create_all()
    migrate.init_app(app, db)
    from app import models
    
    

    from .auth.views import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/")
    
    from .vendor.view import vendor_bp
    app.register_blueprint(vendor_bp, url_prefix="/vendor")

    from .add.views import add_bp
    app.register_blueprint(add_bp, url_prefix="/add")

    from .inventory.views import inventory_bp
    app.register_blueprint(inventory_bp, url_prefix="/view")

    from .home.views import home_bp
    app.register_blueprint(home_bp, url_prefix="/dashboard")

    
    return app