from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from sqlalchemy.sql import text
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import SignupForm
from application.auth.forms import ChangePasswordForm

from application.items.models import Item
from application.lists.models import List
from application.utils.errormessages import msg_admin_feature, msg_other_user

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")
    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/signup/")
def auth_signupform():
    return render_template("auth/signupform.html", form = SignupForm())

@app.route("/auth/", methods=["POST"])
def users_create():
    form = SignupForm(request.form)

    if not form.validate():
        return render_template("auth/signupform.html", form = form)

    u = User(form.name.data, form.username.data, form.password.data)
    u.role = "USER"

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/<username>", methods=["GET"])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    if current_user.id != user.id:
        return render_template("index.html", msg=msg_other_user)
    form = ChangePasswordForm()
    amount = Item.amount_of_items_by_userid(current_user.id)
    return render_template("auth/userprofile.html", user = user, amount=amount, form = form, username = username)


@app.route("/auth/changePassword", methods=["POST"])
@login_required
def changePassword():
    username = current_user.username
    form = ChangePasswordForm(request.form)

    if not form.validate():
        amount = Item.amount_of_items_by_userid(current_user.id)
        return render_template("auth/userprofile.html", user = user, amount=amount, form = form, username = username)

    u = User.query.get(current_user.id)
    u.password=form.password.data
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/auth/deleteAll", methods=["POST"])
@login_required
def deletemyitems():
    account_id = current_user.id

    stmt = text("DELETE FROM Item"
                " WHERE Item.account_id = :account_id").params(account_id=account_id)

    db.engine.execute(stmt)
    return redirect(url_for("items_index"))

@app.route("/users", methods=["GET"])
@login_required
def list_users():
    if current_user.role != "ADMIN":
        return render_template("index.html", msg=msg_admin_feature)
    users = User.list_all_users()
    empty_shoppinglist=User.find_users_with_no_items()
    return render_template("auth/users.html", users = users, empty_shoppinglist = empty_shoppinglist)

@app.route("/users/<user_id>/", methods=["POST"])
@login_required
def users_make_admin(user_id):
    if current_user.role != "ADMIN":
        return render_template("index.html", msg=msg_admin_feature)

    u = User.query.get(user_id)
    if u.role =='ADMIN':
        u.role = 'USER'
    else:
        u.role = 'ADMIN'

    db.session().commit()

    return redirect(url_for("list_users"))

@app.route("/users/amounts", methods=["GET"])
@login_required
def list_users_with_item_amounts():
    if current_user.role != "ADMIN":
        return render_template("index.html", msg=msg_admin_feature)
    users = User.item_amounts_for_everyone()
    return render_template("auth/amounts.html", users = users)

@app.route("/users/amounts/<user_id>/", methods=["POST"])
@login_required
def admin_delete_user(user_id):
    if current_user.role != "ADMIN":
        return render_template("index.html", msg=msg_admin_feature)
    Item.delete_items_by_userid(user_id)
    List.delete_lists_by_userid(user_id)
    User.delete_user_by_userid(user_id)
    return redirect(url_for("list_users_with_item_amounts"))
