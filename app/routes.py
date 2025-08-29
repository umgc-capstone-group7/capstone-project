from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from . import db
from .models import User
from .forms import RegisterForm, LoginForm

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("main.dashboard"))
    return redirect(url_for("main.login"))

@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data.lower()).first():
            flash("Email already registered")
            return redirect(url_for("main.login"))
        u = User(name=form.name.data.strip(), email=form.email.data.lower())
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash("Account created. Please sign in.")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data.lower()).first()
        if u and u.check_password(form.password.data):
            session["user_id"] = u.id
            session["user_name"] = u.name
            return redirect(url_for("main.dashboard"))
        flash("Invalid email or password")
    return render_template("login.html", form=form)

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.login"))

@bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("main.login"))
    return render_template("dashboard.html", name=session.get("user_name"))
