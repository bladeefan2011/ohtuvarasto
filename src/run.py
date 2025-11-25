"""
Main entry point for the Multi-Warehouse Inventory Management System.

This script creates and runs the Flask application.
Run this file directly to start the development server.

Usage:
    python run.py
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    # Run the development server
    app.run(debug=True, host='0.0.0.0', port=5000)
