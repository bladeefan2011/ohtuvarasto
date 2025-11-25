# ohtuvarasto

Multi-Warehouse Inventory Management System

[![CI](https://github.com/bladeefan2011/ohtuvarasto/actions/workflows/main.yml/badge.svg)](https://github.com/bladeefan2011/ohtuvarasto/actions/workflows/main.yml)
[![codecov](https://codecov.io/github/bladeefan2011/ohtuvarasto/graph/badge.svg?token=WZ93EW60J4)](https://codecov.io/github/bladeefan2011/ohtuvarasto)

## Overview

A web-based inventory management application that allows users to manage multiple warehouses and the stock items within them. Built with Python and Flask.

## Features

- **Warehouse Management**: Create, edit, and delete warehouses
- **Item Management**: Add, edit, and delete items in each warehouse
- **Stock Operations**: Easily increase (+) or decrease (-) item quantities
- **Responsive UI**: Clean, responsive interface using Bootstrap 5

## Technical Stack

- **Language**: Python 3.12+
- **Framework**: Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML templates with Jinja2, Bootstrap 5 (via CDN)
- **Forms**: Flask-WTF for form handling and validation

## Installation

### Using Poetry (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/bladeefan2011/ohtuvarasto.git
   cd ohtuvarasto
   ```

2. Install dependencies:
   ```bash
   pip install poetry
   poetry install
   ```

3. Run the application:
   ```bash
   cd src
   poetry run python run.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

### Using pip

1. Clone the repository:
   ```bash
   git clone https://github.com/bladeefan2011/ohtuvarasto.git
   cd ohtuvarasto
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   cd src
   python run.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Database Initialization

The database is automatically created when you first run the application. The SQLite database file (`inventory.db`) will be created in the `src/app/` directory.

## Project Structure

```
ohtuvarasto/
├── src/
│   ├── app/
│   │   ├── __init__.py      # Flask app factory
│   │   ├── models.py        # Database models (Warehouse, Item)
│   │   ├── forms.py         # Flask-WTF forms
│   │   ├── routes.py        # HTTP route handlers
│   │   └── templates/       # Jinja2 HTML templates
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── warehouse_form.html
│   │       ├── warehouse_detail.html
│   │       └── item_form.html
│   ├── run.py               # Application entry point
│   ├── varasto.py           # Original Varasto class
│   └── tests/               # Test files
├── requirements.txt         # pip dependencies
├── pyproject.toml          # Poetry configuration
└── README.md
```

## Running Tests

```bash
poetry run pytest
```

## Linting

```bash
poetry run pylint src
```
