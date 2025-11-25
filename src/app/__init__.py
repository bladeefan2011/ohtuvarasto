"""
Flask Multi-Warehouse Inventory Management Application.

This module initializes and configures the Flask application
with SQLAlchemy database and all necessary routes.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def _get_database_uri(config_name, basedir):
    """Return the database URI based on configuration."""
    if config_name == 'testing':
        return 'sqlite:///:memory:'
    return 'sqlite:///' + os.path.join(basedir, 'inventory.db')


def _configure_app(app, config_name):
    """Configure Flask application settings."""
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        _get_database_uri(config_name, basedir)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')


def create_app(config_name='development'):
    """
    Create and configure the Flask application.

    Args:
        config_name: Configuration mode ('development', 'testing', etc.)

    Returns:
        Configured Flask application instance.
    """
    app = Flask(__name__)
    _configure_app(app, config_name)
    db.init_app(app)

    # Import and register routes (inside function to avoid circular imports)
    from app.routes import main_bp  # pylint: disable=import-outside-toplevel
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app
