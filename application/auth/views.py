from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import SignupForm
from application.auth.forms import ChangePasswordForm

from application.items.models import Item

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
    form2 = SignupForm(request.form)

    u = User(form2.name.data, form2.username.data, form2.password.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/<username>", methods=["GET"])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = ChangePasswordForm()
    amount = Item.amount_of_items_by_userid(current_user.id)
    return render_template("auth/userprofile.html", user = user, amount=amount, form = form)

@app.route("/auth/<username>/changePassword", methods=["POST"])
def changePassword():
    username = current_user.username
    form = ChangePasswordForm(request.form)

    old = find_password_with_userID(current_user.id)

    if old != form.oldpassword.data:
        return render_template("auth/userprofile.html", user = user, amount=amount, form = form)

    if form.password.data != form.password2.data:
        return render_template("auth/userprofile.html", user = user, amount=amount, form = form)

    u = User.query.get(user.id)
    u.password=form.password.data

    db.session().commit()
