"""
Flask-WTF forms for the Multi-Warehouse Inventory Management System.

This module defines forms for creating and editing
warehouses and items using Flask-WTF.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class WarehouseForm(FlaskForm):
    """
    Form for creating and editing warehouses.

    Fields:
        name: The name of the warehouse (required).
        location: The physical location of the warehouse (required).
        submit: Submit button.
    """
    name = StringField(
        'Name',
        validators=[
            DataRequired(message='Warehouse name is required.'),
            Length(min=1, max=100)
        ]
    )
    location = StringField(
        'Location',
        validators=[
            DataRequired(message='Location is required.'),
            Length(min=1, max=200)
        ]
    )
    submit = SubmitField('Save')


class ItemForm(FlaskForm):
    """
    Form for creating and editing items.

    Fields:
        name: The name of the item (required).
        description: Optional description of the item.
        quantity: The quantity of the item (required, non-negative).
        submit: Submit button.
    """
    name = StringField(
        'Item Name',
        validators=[
            DataRequired(message='Item name is required.'),
            Length(min=1, max=100)
        ]
    )
    description = TextAreaField(
        'Description',
        validators=[
            Optional(),
            Length(max=500)
        ]
    )
    quantity = IntegerField(
        'Quantity',
        validators=[
            DataRequired(message='Quantity is required.'),
            NumberRange(min=0, message='Quantity must be non-negative.')
        ]
    )
    submit = SubmitField('Save')
