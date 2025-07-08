# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="templates")

    # Register your blueprint
    from app.routes import routes
    app.register_blueprint(routes)

    return app
