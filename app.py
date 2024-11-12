from flask import Flask
from services.routes import init_routes

app = Flask(__name__)

# Initialize the routes
init_routes(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)