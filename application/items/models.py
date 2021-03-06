from application import db
from application.models import Base
from application.lists.models import List

from sqlalchemy.sql import text

class Item(Base):
    name = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.Integer, nullable=True)
    bought = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)

    list_id = db.Column(db.Integer, db.ForeignKey('list.id'),
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
        stmt = text("SELECT Item.id, Item.name, Item.bought, Item.amount, Item.list_id, Item.category_id FROM Item"
                    " WHERE (Item.account_id = :id)").params(id=id)
        res = db.engine.execute(stmt)

        result = []
        for row in res:
            result.append({"id": row[0],
                            "name": row[1],
                            "bought": row[2],
                            "amount": row[3],
                            "list_id": row[4],
                            "category_id": row[5]})
        return result

    @staticmethod
    def amount_of_items_by_userid(id):
        stmt = text("SELECT COUNT(id) FROM Item"
                    " WHERE (Item.account_id = :id)").params(id=id)

        res = db.engine.execute(stmt)

        for row in res:
            result = row[0]

        return result

    @staticmethod
    def delete_items_by_userid(id):
        stmt = text("DELETE From Item"
                    " WHERE Item.account_id = :id").params(id=id)
        db.engine.execute(stmt)

    @staticmethod
    def update_item(id, name, amount, bought, list_id, category_id):
        stmt = text("UPDATE Item"
                    " SET name = :name, amount = :amount, bought = :bought, list_id = :list_id, category_id = :category_id"
                    " WHERE id = :id").params(id=id, name=name, amount=amount, bought=bought, list_id=list_id, category_id=category_id)
        db.engine.execute(stmt)
