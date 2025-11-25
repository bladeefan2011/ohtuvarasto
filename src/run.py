"""
Main entry point for the Multi-Warehouse Inventory Management System.

This script creates and runs the Flask application.
Run this file directly to start the development server.

Usage:
    python run.py
"""

import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Debug mode should only be enabled in development environment
    # via the FLASK_DEBUG environment variable
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
