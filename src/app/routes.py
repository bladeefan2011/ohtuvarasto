"""
Flask routes for the Multi-Warehouse Inventory Management System.

This module defines all HTTP routes for managing
warehouses and items in the inventory system.
"""

from flask import Blueprint, render_template, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.models import Warehouse, Item
from app.forms import WarehouseForm, ItemForm

main_bp = Blueprint('main', __name__)


def _handle_db_error(error, operation="operation"):
    """Handle database errors and flash a user-friendly message."""
    db.session.rollback()
    flash(f'Database error during {operation}. Please try again.', 'danger')
    print(f"Database error: {error}")


def _save_warehouse(warehouse, form):
    """Save warehouse data from form and commit to database."""
    warehouse.name = form.name.data
    warehouse.location = form.location.data
    db.session.commit()


def _save_item(item, form):
    """Save item data from form and commit to database."""
    item.name = form.name.data
    item.description = form.description.data
    item.quantity = form.quantity.data
    db.session.commit()


def _create_item_from_form(form, warehouse_id):
    """Create a new Item object from form data."""
    return Item(
        name=form.name.data,
        description=form.description.data,
        quantity=form.quantity.data,
        warehouse_id=warehouse_id
    )


def _update_item_quantity(item, delta):
    """Update item quantity by delta and commit. Returns success."""
    try:
        item.quantity += delta
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        _handle_db_error(e, "quantity update")
        return False


@main_bp.route('/')
def index():
    """Display list of all warehouses."""
    warehouses = Warehouse.query.all()
    return render_template('index.html', warehouses=warehouses)


@main_bp.route('/warehouse/new', methods=['GET', 'POST'])
def create_warehouse():
    """Create a new warehouse."""
    form = WarehouseForm()
    if form.validate_on_submit():
        try:
            warehouse = Warehouse(
                name=form.name.data,
                location=form.location.data
            )
            db.session.add(warehouse)
            db.session.commit()
            flash('Warehouse created successfully!', 'success')
            return redirect(url_for('main.index'))
        except SQLAlchemyError as e:
            _handle_db_error(e, "warehouse creation")
    return render_template(
        'warehouse_form.html',
        form=form,
        title='Create Warehouse'
    )


@main_bp.route('/warehouse/<int:warehouse_id>')
def warehouse_detail(warehouse_id):
    """Display details and items for a specific warehouse."""
    warehouse = Warehouse.query.get_or_404(warehouse_id)
    return render_template('warehouse_detail.html', warehouse=warehouse)


@main_bp.route('/warehouse/<int:warehouse_id>/edit', methods=['GET', 'POST'])
def edit_warehouse(warehouse_id):
    """Edit an existing warehouse."""
    warehouse = Warehouse.query.get_or_404(warehouse_id)
    form = WarehouseForm(obj=warehouse)
    if form.validate_on_submit():
        try:
            _save_warehouse(warehouse, form)
            flash('Warehouse updated successfully!', 'success')
            return redirect(url_for('main.index'))
        except SQLAlchemyError as e:
            _handle_db_error(e, "warehouse update")
    return render_template(
        'warehouse_form.html',
        form=form,
        title='Edit Warehouse'
    )


@main_bp.route('/warehouse/<int:warehouse_id>/delete', methods=['POST'])
def delete_warehouse(warehouse_id):
    """Delete a warehouse and all its items."""
    warehouse = Warehouse.query.get_or_404(warehouse_id)
    try:
        db.session.delete(warehouse)
        db.session.commit()
        flash('Warehouse deleted successfully!', 'success')
    except SQLAlchemyError as e:
        _handle_db_error(e, "warehouse deletion")
    return redirect(url_for('main.index'))


def _add_item_and_redirect(form, wh_id):
    """Add a new item from form and redirect to warehouse detail."""
    try:
        item = _create_item_from_form(form, wh_id)
        db.session.add(item)
        db.session.commit()
        flash('Item added successfully!', 'success')
        return redirect(url_for('main.warehouse_detail', warehouse_id=wh_id))
    except SQLAlchemyError as e:
        _handle_db_error(e, "item creation")
        return None


@main_bp.route('/warehouse/<int:wh_id>/item/new', methods=['GET', 'POST'])
def create_item(wh_id):
    """Add a new item to a warehouse."""
    warehouse = Warehouse.query.get_or_404(wh_id)
    form = ItemForm()
    if form.validate_on_submit():
        result = _add_item_and_redirect(form, warehouse.id)
        if result:
            return result
    return render_template(
        'item_form.html', form=form, warehouse=warehouse, title='Add Item'
    )


@main_bp.route('/item/<int:item_id>/edit', methods=['GET', 'POST'])
def edit_item(item_id):
    """Edit an existing item."""
    item = Item.query.get_or_404(item_id)
    form = ItemForm(obj=item)
    if form.validate_on_submit():
        try:
            _save_item(item, form)
            flash('Item updated successfully!', 'success')
            wh_id = item.warehouse_id
            return redirect(
                url_for('main.warehouse_detail', warehouse_id=wh_id)
            )
        except SQLAlchemyError as e:
            _handle_db_error(e, "item update")
    return render_template(
        'item_form.html',
        form=form,
        warehouse=item.warehouse,
        title='Edit Item'
    )


@main_bp.route('/item/<int:item_id>/delete', methods=['POST'])
def delete_item(item_id):
    """Delete an item from a warehouse."""
    item = Item.query.get_or_404(item_id)
    warehouse_id = item.warehouse_id
    try:
        db.session.delete(item)
        db.session.commit()
        flash('Item deleted successfully!', 'success')
    except SQLAlchemyError as e:
        _handle_db_error(e, "item deletion")
    return redirect(url_for('main.warehouse_detail', warehouse_id=warehouse_id))


@main_bp.route('/item/<int:item_id>/increase', methods=['POST'])
def increase_quantity(item_id):
    """Increase the quantity of an item by 1."""
    item = Item.query.get_or_404(item_id)
    if _update_item_quantity(item, 1):
        msg = f'Increased {item.name} quantity to {item.quantity}.'
        flash(msg, 'success')
    wh_id = item.warehouse_id
    return redirect(url_for('main.warehouse_detail', warehouse_id=wh_id))


@main_bp.route('/item/<int:item_id>/decrease', methods=['POST'])
def decrease_quantity(item_id):
    """Decrease the quantity of an item by 1 (minimum 0)."""
    item = Item.query.get_or_404(item_id)
    if item.quantity > 0:
        if _update_item_quantity(item, -1):
            msg = f'Decreased {item.name} quantity to {item.quantity}.'
            flash(msg, 'success')
    else:
        flash(f'{item.name} quantity is already at 0.', 'warning')
    wh_id = item.warehouse_id
    return redirect(url_for('main.warehouse_detail', warehouse_id=wh_id))


# fortnite
