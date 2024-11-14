from flask import Flask
from services.routes import init_routes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Initialize the routes
init_routes(app)

# Configuration de la connexion à la base de données MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@mysqldb/predictions'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy()

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)