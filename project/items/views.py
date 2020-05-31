from flask import request, flash, Blueprint, jsonify
from project.models import Item
from project import db


items_blueprint = Blueprint(
    'items',
    __name__
)


@items_blueprint.route('/', methods=['GET', 'POST'])
def index():
    all_items = Item.query.all()
    # Can do this, but flask-restful will probably make it easier
    item_list = [{
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'quantity': item.quantity
        }
        for item in all_items
        ]

    if request.method == 'POST':
        new_item = Item(
            request.json['name'],
            request.json['description'],
            request.json['quantity']
        )
        print('new_item: ', new_item)
        db.session.add(new_item)
        db.session.commit()
        return jsonify({
            'id': new_item.id,
            'name': new_item.name,
            'description': new_item.description,
            'quantity': new_item.quantity
        })
    return jsonify(item_list)


@items_blueprint.route('/<int:item_id>', methods=['GET', 'PATCH', 'DELETE'])
def item(item_id):
    found_item = Item.query.get(item_id)
    if request.method == 'DELETE':
        print(found_item)
        db.session.delete(found_item)
        db.session.commit()
        # Delete still needs to return something or you get an error
        return jsonify({
            'id': found_item.id,
            'name': found_item.name,
            'description': found_item.description,
            'quantity': found_item.quantity
        })
    if request.method == 'PATCH':
        found_item.name = request.json['name']
        found_item.description = request.json['description']
        found_item.quantity = request.json['quantity']
        db.session.add(found_item)
        db.session.commit()
        return jsonify({
            'id': found_item.id,
            'name': found_item.name,
            'description': found_item.description,
            'quantity': found_item.quantity
        })
    return found_item
