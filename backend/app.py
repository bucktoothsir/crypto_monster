"""
Flask app.
"""

from flask import Flask

import config
from routes import configure_routes


def create_app(config=config):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['PERMANENT_SESSION_LIFETIME'] = config.PERMANENT_SESSION_LIFETIME
    configure_routes(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()