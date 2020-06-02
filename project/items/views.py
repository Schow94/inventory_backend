from flask import request, flash, Blueprint, jsonify
from flask_restful import Api, Resource, fields, marshal_with
from project.models import Item
from project import db


items_blueprint_bp = Blueprint(
    'items',
    __name__
)

items_blueprint = Api(items_blueprint_bp)

# Items field for Flask Restful
item_fields = {
            'id': fields.Integer,
            'name': fields.String,
            'description': fields.String,
            'quantity': fields.Integer
}


@items_blueprint.resource('/', methods=['GET', 'POST'])
class ItemsAPI(Resource):
    @marshal_with(item_fields)
    def get(self):
        return Item.query.all()

    @marshal_with(item_fields)
    def post(self):
        new_item = Item(
            request.json['name'],
            request.json['description'],
            request.json['quantity']
        )
        db.session.add(new_item)
        db.session.commit()
        return new_item


@items_blueprint.resource('/<int:item_id>', methods=['GET', 'PATCH', 'DELETE'])
class ItemAPI(Resource):
    @marshal_with(item_fields)
    # Looks like you can just pas in parameters to route fxns
    def delete(self, item_id):
        # print('request: ', request)
        found_item = Item.query.get(item_id)
        db.session.delete(found_item)
        db.session.commit()
        # Delete still needs to return something or you get an error
        return found_item

    @marshal_with(item_fields)
    def patch(self, item_id):
        found_item = Item.query.get(item_id)
        found_item.name = request.json['name']
        found_item.description = request.json['description']
        found_item.quantity = request.json['quantity']
        db.session.add(found_item)
        db.session.commit()
        return found_item
    
    def get(self, item_id):
        found_item = Item.query.get(item_id)
        return found_item
