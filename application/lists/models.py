from application import db
from application.models import Base

from sqlalchemy.sql import text

class List(Base):
    name = db.Column(db.String(144), nullable=False)
    info = db.Column(db.String(144), nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    items = db.relationship("Item", backref='list', lazy=True)

    def __init__(self, name, info):
        self.name = name
        self.info = info

    @staticmethod
    def find_all_lists_by_id(id):
        stmt = text("SELECT List.id, List.name, List.info FROM List"
                    " WHERE (List.account_id = :id)").params(id=id)
        res = db.engine.execute(stmt)

        result = []
        for row in res:
            result.append({"id": row[0],
                            "name": row[1],
                            "info": row[2]})
        return result

    @staticmethod
    def find_all_lists_by_id_dictionary(id):
        stmt = text("SELECT List.id, List.name FROM List"
                    " WHERE (List.account_id = :id)").params(id=id)
        res = db.engine.execute(stmt)

        result = {}
        for row in res:
            result[row[0]] = row[1]

        return result

    @staticmethod
    def amount_of_lists_by_userid(id):
        stmt = text("SELECT COUNT(id) FROM List"
                    " WHERE (List.account_id = :id)").params(id=id)

        res = db.engine.execute(stmt)

        for row in res:
            result = row[0]

        return result

    @staticmethod
    def user_has_default_list(id):
        stmt = text("SELECT name FROM List"
        " WHERE (List.account_id = :id)"
        " AND name = 'default'").params(id=id)
        res = db.engine.execute(stmt)

        result = []
        for row in res:
                result = row[0]

        return result

    @staticmethod
    def find_users_defaultlist_id(id):
        stmt = text("SELECT id FROM List"
        " WHERE (List.account_id = :id)"
        " AND name = 'default'").params(id=id)
        res = db.engine.execute(stmt)

        result = []
        for row in res:
                result = row[0]

        return result

    @staticmethod
    def create_default_list_for_user(id):
        l = List("default", "default list to ensure proper functioning")
        l.account_id = id

        db.session.add(l)
        db.session.commit()

    @staticmethod
    def find_items_by_list(id):
        stmt = text("SELECT Item.id, Item.name, Item.bought, Item.amount, Item.category_id FROM Item"
        " WHERE (Item.list_id = :id)").params(id=id)

        res = db.engine.execute(stmt)
        result = []

        for row in res:
            result.append({"id": row[0],
                            "name": row[1],
                            "bought": row[2],
                            "amount": row[3],
                            "category_id": row[4]})
        return result

    @staticmethod
    def delete_lists_by_userid(id):
        stmt = text("DELETE From List"
                    " WHERE (List.account_id = :id)").params(id=id)

        db.engine.execute(stmt)
