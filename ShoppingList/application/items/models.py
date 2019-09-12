from application import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.Integer, nullable=True)
    bought = db.Column(db.Boolean, nullable=False)
    category = db.Column(db.String(40), nullable=False)

    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.bought = False
        self.category = "default"
