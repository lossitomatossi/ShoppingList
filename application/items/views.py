from application import app, db
from flask import render_template, request, redirect, url_for
from application.items.models import Item

@app.route("/items", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new/")
def items_form():
    return render_template("items/new.html")

@app.route("/items/<item_id>/", methods=["POST"])
def items_set_done(item_id):

    i = Item.query.get(item_id)
    i.bought = True
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/", methods=["POST"])
def items_create():
    name = request.form.get("name")
    amount = request.form.get("amount")
    bought = False
    category = "default"
    i = Item(name, amount, category)

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("items_index"))
