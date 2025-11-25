"""
Database models for the Multi-Warehouse Inventory Management System.

This module defines the Warehouse and Item models with their
relationships and database schema.
"""

from app import db


class Warehouse(db.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a warehouse that can store multiple items.

    Attributes:
        id: Unique identifier for the warehouse.
        name: Name of the warehouse.
        location: Physical location of the warehouse.
        items: List of items stored in this warehouse.
    """
    __tablename__ = 'warehouses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)

    # Relationship: One Warehouse has many Items
    items = db.relationship(
        'Item',
        backref='warehouse',
        lazy=True,
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        """Return string representation of the warehouse."""
        return f'<Warehouse {self.name}>'


class Item(db.Model):  # pylint: disable=too-few-public-methods
    """
    Represents an item stored in a warehouse.

    Attributes:
        id: Unique identifier for the item.
        name: Name of the item.
        description: Description of the item.
        quantity: Current quantity of the item in stock.
        warehouse_id: Foreign key linking to the parent warehouse.
    """
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    warehouse_id = db.Column(
        db.Integer,
        db.ForeignKey('warehouses.id'),
        nullable=False
    )

    def __repr__(self):
        """Return string representation of the item."""
        return f'<Item {self.name}>'
