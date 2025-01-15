from flask import Blueprint, request, jsonify
from models import Payment, db

payment_routes = Blueprint('payment_routes', __name__)

@payment_routes.route('', methods=['POST'])
def create_payment():
    data = request.json
    user_id = data.get('user_id')
    amount = data.get('amount')
    status = data.get('status')

    if not user_id or not amount or not status:
        return jsonify({"error": "Missing fields"}), 400

    payment = Payment(user_id=user_id, amount=amount, status=status)
    db.session.add(payment)
    db.session.commit()
    return jsonify({"message": "Payment created successfully!"}), 201

@payment_routes.route('/history', methods=['GET'])
def get_payment_history():
    payments = Payment.query.all()
    payment_list = [{
        "id": payment.id,
        "user_id": payment.user_id,
        "amount": payment.amount,
        "status": payment.status
    } for payment in payments]

    return jsonify(payment_list)
