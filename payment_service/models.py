from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Ödeme modeli
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Payment {self.id}, Amount: {self.amount}, Status: {self.status}>"
