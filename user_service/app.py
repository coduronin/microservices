"""from flask import Flask
from routes import user_routes

app = Flask(__name__)

# Veritabanı yapılandırması (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Blueprint'i kaydet
app.register_blueprint(user_routes, url_prefix='/users')

if __name__ == "__main__":
    app.run(debug=True)

"""
from flask import Flask
from routes import user_routes
from models import db

app = Flask(__name__)

# Veritabanı yapılandırması (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Veritabanı bağlantısını başlat
db.init_app(app)

# Blueprint'i kaydet
app.register_blueprint(user_routes, url_prefix='/users')

# Veritabanını oluştur
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
