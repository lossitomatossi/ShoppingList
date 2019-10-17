from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.categories.models import Category
from application.categories.forms import CategoryForm
from application.utils.errormessages import msg_admin_feature

@app.route("/categories", methods=["GET"])
def categories_index():
    return render_template("categories/list.html", categories = Category.query.all())

@app.route("/categories/new/")
@login_required
def categories_form():
    if current_user.role != "ADMIN":
        return render_template("index.html", msg=msg_admin_feature)
    return render_template("categories/new.html", form = CategoryForm())


@app.route("/categories/", methods=["POST"])
@login_required
def categories_create():
    if current_user.role != "ADMIN":
        return render_template("index.html", msg=msg_admin_feature)
    form = CategoryForm(request.form)

    if not form.validate():
        return render_template("categories/new.html", form = form)

    c = Category(form.name.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("categories_index"))
