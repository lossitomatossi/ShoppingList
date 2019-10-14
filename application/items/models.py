from application import db
from application.models import Base

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
        stmt = ("SELECT * FROM Item WHERE Item.account_id = :id").params(id=id)
        res = db.engine.execute(stmt)

        result = []
        for row in res:
            result.append({"item_id": row[0],
                            "item_name": row[1],
                            "item_bought": row[2],
                            "item_account_id": row[3]})


        return result
