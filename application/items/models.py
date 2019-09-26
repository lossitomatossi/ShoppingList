from application import db
from application.models import Base

class Item(Base):
    name = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.Integer, nullable=True)
    bought = db.Column(db.Boolean, nullable=False)
    category = db.Column(db.String(40), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.bought = False
        self.category = "default"
