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
    host = os.environ.get('FLASK_HOST', '127.0.0.1')

    # Security check: refuse to run with debug mode on all interfaces
    if debug_mode and host == '0.0.0.0':
        raise RuntimeError(
            "Refusing to run with debug=True and host='0.0.0.0'. "
            "This is unsafe and can allow arbitrary code execution. "
            "Use FLASK_HOST=127.0.0.1 for debug mode or disable debug."
        )

    app.run(debug=debug_mode, host=host, port=5000)
