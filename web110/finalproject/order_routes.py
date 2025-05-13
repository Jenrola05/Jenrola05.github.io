from flask import Blueprint, request, jsonify
from app import db
from app.models.models import Order, Pizza
import requests

bp = Blueprint("order_routes", __name__)

@bp.route("/submit-order", methods=["POST"])
def submit_order():
    data = request.json
    new_order = Order(customer_id=data["customer_id"], comments=data["comments"], total_price=0)
    db.session.add(new_order)
    db.session.commit()

    total_price = 0
    for p in data["pizzas"]:
        pizza = Pizza(size=p["size"], toppings=",".join(p["toppings"]),
                      price=p["price"], order_id=new_order.id)
        db.session.add(pizza)
        total_price += p["price"]

    tax_rate = get_tax_rate(data["zip"])
    total_price *= (1 + tax_rate)
    new_order.total_price = round(total_price, 2)
    db.session.commit()
    return jsonify({"status": "success", "total_price": new_order.total_price})

def get_tax_rate(zip_code):
    # Simulated tax API
    zip_tax = {"60010": 0.10, "60616": 0.0925}
    return zip_tax.get(zip_code, 0.08)
