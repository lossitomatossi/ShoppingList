from application import db
from application.models import Base
from application.items.models import Item
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(30), nullable=False)

    items = db.relationship("Item", backref='account', lazy=True)
    lists = db.relationship("List", backref='account', lazy=True)


    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return self.role


    @staticmethod
    def find_users_with_no_items(bought=True):
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN Item ON Item.account_id = Account.id"
                    " WHERE (Item.bought IS null OR Item.bought = :bought)"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Item.id) = 0").params(bought=bought)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response

    @staticmethod
    def find_password_with_userID(id):
        stmt = text("SELECT password FROM account"
                    " WHERE id = :id").params(id=id)

        res = db.engine.execute(stmt)

        for row in res:
            response = row[0]

        return response

    @staticmethod
    def delete_all_users_items(account_id):
        stmt = text("DELETE FROM Item"
                    " WHERE Item.account_id = :account_id").params(account_id=account_id)

        db.engine.execute(stmt)

    @staticmethod
    def amount_of_users():
        stmt = text("SELECT COUNT(*) FROM Account")

        res = db.engine.execute(stmt)

        for row in res:
            response = row[0]

        return response

    @staticmethod
    def create_admin_account():
        stmt = text("INSERT INTO Account"
                    " (name, username, password, role)"
                    " values ('admin', 'admin', 'admin', 'ADMIN')")

        db.engine.execute(stmt)

    @staticmethod
    def list_all_users():
        stmt = text("SELECT id, username, role from Account")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "username":row[1], "role":row[2]})

        return response
