from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.lists.models import List
from application.lists.forms import ListForm

from application.items.models import Item
from application.categories.models import Category

from sqlalchemy.sql import text

@app.route("/lists", methods=["GET"])
@login_required
def lists_index():
    return render_template("lists/list.html", lists = List.find_all_lists_by_id(current_user.id))

@app.route("/lists/all", methods=["GET"])
def lists_all():
    return render_template("lists/list.html", lists = List.query.all())

@app.route("/lists/new/")
@login_required
def lists_form():
    return render_template("lists/new.html", form = ListForm())
