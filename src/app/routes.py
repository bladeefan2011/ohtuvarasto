"""
Flask routes for the Multi-Warehouse Inventory Management System.

This module defines all HTTP routes for managing
warehouses and items in the inventory system.
"""

from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import Warehouse, Item
from app.forms import WarehouseForm, ItemForm

main_bp = Blueprint('main', __name__)


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
        warehouse = Warehouse(
            name=form.name.data,
            location=form.location.data
        )
        db.session.add(warehouse)
        db.session.commit()
        flash('Warehouse created successfully!', 'success')
        return redirect(url_for('main.index'))
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
        warehouse.name = form.name.data
        warehouse.location = form.location.data
        db.session.commit()
        flash('Warehouse updated successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template(
        'warehouse_form.html',
        form=form,
        title='Edit Warehouse'
    )


@main_bp.route('/warehouse/<int:warehouse_id>/delete', methods=['POST'])
def delete_warehouse(warehouse_id):
    """Delete a warehouse and all its items."""
    warehouse = Warehouse.query.get_or_404(warehouse_id)
    db.session.delete(warehouse)
    db.session.commit()
    flash('Warehouse deleted successfully!', 'success')
    return redirect(url_for('main.index'))


@main_bp.route('/warehouse/<int:wh_id>/item/new', methods=['GET', 'POST'])
def create_item(wh_id):
    """Add a new item to a warehouse."""
    warehouse = Warehouse.query.get_or_404(wh_id)
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(
            name=form.name.data,
            description=form.description.data,
            quantity=form.quantity.data,
            warehouse_id=warehouse.id
        )
        db.session.add(item)
        db.session.commit()
        flash('Item added successfully!', 'success')
        wh_id = warehouse.id
        return redirect(url_for('main.warehouse_detail', warehouse_id=wh_id))
    return render_template(
        'item_form.html',
        form=form,
        warehouse=warehouse,
        title='Add Item'
    )


@main_bp.route('/item/<int:item_id>/edit', methods=['GET', 'POST'])
def edit_item(item_id):
    """Edit an existing item."""
    item = Item.query.get_or_404(item_id)
    form = ItemForm(obj=item)
    if form.validate_on_submit():
        item.name = form.name.data
        item.description = form.description.data
        item.quantity = form.quantity.data
        db.session.commit()
        flash('Item updated successfully!', 'success')
        return redirect(
            url_for('main.warehouse_detail', warehouse_id=item.warehouse_id)
        )
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
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!', 'success')
    return redirect(url_for('main.warehouse_detail', warehouse_id=warehouse_id))


@main_bp.route('/item/<int:item_id>/increase', methods=['POST'])
def increase_quantity(item_id):
    """Increase the quantity of an item by 1."""
    item = Item.query.get_or_404(item_id)
    item.quantity += 1
    db.session.commit()
    flash(f'Increased {item.name} quantity to {item.quantity}.', 'success')
    wh_id = item.warehouse_id
    return redirect(url_for('main.warehouse_detail', warehouse_id=wh_id))


@main_bp.route('/item/<int:item_id>/decrease', methods=['POST'])
def decrease_quantity(item_id):
    """Decrease the quantity of an item by 1 (minimum 0)."""
    item = Item.query.get_or_404(item_id)
    if item.quantity > 0:
        item.quantity -= 1
        db.session.commit()
        flash(f'Decreased {item.name} quantity to {item.quantity}.', 'success')
    else:
        flash(f'{item.name} quantity is already at 0.', 'warning')
    wh_id = item.warehouse_id
    return redirect(url_for('main.warehouse_detail', warehouse_id=wh_id))
