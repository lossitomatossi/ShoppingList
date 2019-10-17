from application import db
from application.models import Base

from sqlalchemy.sql import text

class Category(Base):
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name


    @staticmethod
    def find_all_category_names():
        stmt = text("SELECT Category.name FROM Category")
        res = db.engine.execute(stmt)

        result = []

        for row in res:
            result.append({"name": row[0]})

        return result
