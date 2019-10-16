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

    default = List.user_has_default_list(current_user.id)
    if default != "default":
        List.create_default_list_for_user(current_user.id)

    lists = List.find_all_lists_by_id(current_user.id)
    return render_template("lists/list.html", lists = lists)

@app.route("/lists/all", methods=["GET"])
def lists_all():
    return render_template("lists/list.html", lists = List.query.all())

@app.route("/lists/new/")
@login_required
def lists_form():
    return render_template("lists/new.html", form = ListForm())


@app.route("/lists/", methods=["POST"])
@login_required
def lists_create():
    form = ListForm(request.form)

    if not form.validate():
        return render_template("lists/new.html", form = form)

    l = List(form.name.data, form.info.data)
    l.account_id = current_user.id

    db.session().add(l)
    db.session().commit()

    return redirect(url_for("lists_index"))

@app.route("/lists/<list_id>", methods=["GET"])
@login_required
def list_page(list_id):
    return render_template("/lists/info.html", list = List.query.get(list_id))
