from flask import Flask
from routes import payment_routes
from models import db  # db'yi içe aktar

app = Flask(__name__)

# Veritabanı yapılandırması (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db'yi uygulamaya bağla
db.init_app(app)

# Blueprint'i kaydet
app.register_blueprint(payment_routes, url_prefix='/payments')

# Veritabanını oluştur (app_context ile)
with app.app_context():
    db.create_all()  # Veritabanını oluştur

if __name__ == "__main__":
    app.run(debug=True)

