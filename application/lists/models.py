from application import db
from application.models import Base

from sqlalchemy.sql import text

class List(Base):
    name = db.Column(db.String(144), nullable=False)
    info = db.Column(db.String(144), nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

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
    def amount_of_lists_by_userid(id):
        stmt = text("SELECT COUNT(id) FROM List"
                    " WHERE (List.account_id = :id)").params(id=id)

        res = db.engine.execute(stmt)

        for row in res:
            result = row[0]

        return result
