from flask import Flask
from backend.routes import init_routes
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)

