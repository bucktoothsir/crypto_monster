"""
Flask app.
"""

from flask import Flask
from flask_cors import CORS

from routes import configure_routes
import config


def create_app(config=config):
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['PERMANENT_SESSION_LIFETIME'] = config.PERMANENT_SESSION_LIFETIME
    configure_routes(app)


app = Flask(__name__)
create_app()
CORS(app)

if __name__ == '__main__':
    app.run()
