# This Python file uses the following encoding: utf-8


# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
# Käytetään tasks.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Login functionality

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            unauthorized = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# Import models and views

from application import views

from application.items import models
from application.items import views

from application.auth import models
from application.auth import views

from application.categories import models
from application.categories import views

from application.lists import models
from application.lists import views


# login functionality part 2

from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# database creation
try:
    db.create_all()
except:
    pass

# If there are no accounts create admin account
users_amount = User.amount_of_users()

if users_amount == 0:
    User.create_admin_account()

# If there are no categories, create default category
# (default category is needed for adding items)
from application.categories.models import Category

categories_amount = Category.amount_of_categories()

if categories_amount == 0:
    Category.create_default_category()
