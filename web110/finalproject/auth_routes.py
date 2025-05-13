from flask import Blueprint, request, redirect, render_template, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.models import Customer
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("auth_routes", __name__)

@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Customer.query.filter_by(email=request.form["email"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("main_routes.home"))
        flash("Invalid credentials")
    return render_template("login.html")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main_routes.home"))
