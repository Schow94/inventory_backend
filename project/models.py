from project import db


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer)
    
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity

    def __repr__(self):
        return f'The name of this item is {self.name}'