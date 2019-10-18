from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.items.models import Item
from application.items.forms import ItemForm, AmountForm, CategoryForm, ListForm
from application.categories.models import Category
from application.lists.models import List
from application.utils.errormessages import msg_admin_feature, msg_other_user


from sqlalchemy.sql import text

@app.route("/items", methods=["GET"])
@login_required
def items_index():
    categoryNames = Category.find_all_category_names()
    listnames = List.find_all_lists_by_id_dictionary(current_user.id)
    items = Item.find_all_items_by_id(current_user.id)
    return render_template("items/list.html", items = items, categoryNames = categoryNames, listnames = listnames)

@app.route("/items/all", methods=["GET"])
@login_required
def items_all():
    if current_user.role != "ADMIN":
        return render_template("index.html", msg=msg_admin_feature)
    categoryNames = Category.find_all_category_names()
    listnames = List.find_all_list_names()
    items = Item.query.all()
    return render_template("items/all.html", items = items, categoryNames = categoryNames, listnames = listnames)

@app.route("/items/new/")
@login_required
def items_form():
    default = List.user_has_default_list(current_user.id)
    if default != "default":
        List.create_default_list_for_user(current_user.id)
    return render_template("items/new.html", form = ItemForm(), categories = Category.query.all())

@app.route("/items/<item_id>/", methods=["POST"])
@login_required
def items_set_done(item_id):

    i = Item.query.get(item_id)
    if i.bought == False:
        i.bought = True
    elif i.bought == True:
        i.bought = False
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/<item_id>", methods=["GET"])
@login_required
def item(item_id):
    item = Item.query.get_or_404(item_id)
    if current_user.id != item.account_id:
        return render_template("index.html", msg=msg_other_user)

    lists = List.find_all_lists_by_id(current_user.id)
    categories = Category.query.all()
    categoryNames = Category.find_all_category_names()
    listnames = List.find_all_lists_by_id_dictionary(current_user.id)
    return render_template("items/edit.html", item = item, lists = lists, categories = categories, categoryNames = categoryNames, listnames = listnames, aform = AmountForm())

@app.route("/items/<item_id>/amount", methods=["POST"])
@login_required
def item_amount(item_id):
    item = Item.query.get_or_404(item_id)
    form = AmountForm(request.form)
    item.amount = form.amount.data
    db.session.commit()
    return redirect(url_for("item", item_id = item.id))

@app.route("/items/<item_id>/category", methods=["POST"])
@login_required
def item_category(item_id):
    item = Item.query.get_or_404(item_id)
    form = CategoryForm(request.form)
    item.category_id = form.category.data
    db.session.commit()
    return redirect(url_for("item", item_id = item.id))

@app.route("/items/<item_id>/list", methods=["POST"])
@login_required
def item_list(item_id):
    item = Item.query.get_or_404(item_id)
    form = ListForm(request.form)
    item.list_id = form.list.data
    db.session.commit()
    return redirect(url_for("item", item_id = item.id))

@app.route("/items/<item_id>/delete", methods=["POST"])
@login_required
def items_delete(item_id):
    stmt = text("DELETE FROM ITEM WHERE Item.id = :id").params(id=item_id)
    db.engine.execute(stmt)
    return redirect(url_for("items_index"))

@app.route("/items/all/<item_id>/delete", methods=["POST"])
@login_required
def items_all_delete(item_id):
    if current_user.role != "ADMIN":
        return render_template("index.html", msg=msg_admin_feature)
    stmt = text("DELETE FROM ITEM WHERE Item.id = :id").params(id=item_id)
    db.engine.execute(stmt)
    return redirect(url_for("items_all"))


@app.route("/items/", methods=["POST"])
@login_required
def items_create():
    form = ItemForm(request.form)
    list = Category.query.all()

    if not form.validate():
        return render_template("items/new.html", form = form, categories = list)

    i = Item(form.name.data, form.amount.data)
    i.bought = form.bought.data
    i.account_id = current_user.id
    i.category_id = form.category.data
    i.list_id = List.find_users_defaultlist_id(current_user.id)

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("items_index"))
