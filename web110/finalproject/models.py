from app import db
from flask_login import UserMixin

class Customer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    orders = db.relationship("Order", backref="customer", lazy=True)

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(10), nullable=False)
    toppings = db.Column(db.String(255))  # comma-separated
    price = db.Column(db.Float, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    pizzas = db.relationship("Pizza", backref="order", lazy=True)
    comments = db.Column(db.String(300))
    total_price = db.Column(db.Float)
    status = db.Column(db.String(50), default="Placed")
