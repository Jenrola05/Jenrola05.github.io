from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza.db"

    db.init_app(app)
    login_manager.init_app(app)

    from .routes import main_routes, auth_routes, order_routes, staff_routes
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(order_routes.bp)
    app.register_blueprint(staff_routes.bp)

    return app
