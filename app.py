from flask import Flask
from services.routes import init_routes

app = Flask(__name__)

# Initialize the routes
init_routes(app)

if __name__ == "__main__":
    app.run()