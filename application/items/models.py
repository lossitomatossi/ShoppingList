from application import db
from application.models import Base

from sqlalchemy.sql import text

class Item(Base):
    name = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.Integer, nullable=True)
    bought = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.bought = False
        self.category = "default"

    def delete_item_by_id(id):
        stmt = text("DELETE FROM ITEM WHERE Item.id = :id").params(id=id)
        db.engine.execute(stmt)

    @staticmethod
    def find_all_items_by_id(id):
        stmt = text("SELECT Item.id, Item.name, Item.bought FROM Item"
                    " WHERE (Item.account_id = :id)").params(id=id)
        res = db.engine.execute(stmt)

        result = []
        for row in res:
            result.append({"id": row[0],
                            "name": row[1],
                            "bought": row[2]})
        return result
