from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User, Classlist
from .forms import RegisterForm, LoginForm

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    if current_user.is_authenticated:
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
            login_user(u)
            return redirect(url_for("main.dashboard"))
        flash("Invalid email or password")
    return render_template("login.html", form=form)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))

@bp.route("/dashboard")
@login_required
def dashboard():
    classes = Classlist.query.order_by(Classlist.year.desc()).limit(10).all()
    return render_template("dashboard.html", user=current_user, classes=classes)


@bp.route("/classes")
@login_required
def classes():
    classes = Classlist.query.order_by(Classlist.year.desc(), Classlist.semester.desc()).all()
    return render_template("classes.html", user=current_user, classes=classes)


@bp.route("/class-selection")
@login_required
def class_selection():
    classes = Classlist.query.order_by(Classlist.year.desc(), Classlist.semester.desc()).all()
    return render_template("class_selection.html", user=current_user, classes=classes)


@bp.route("/gpa")
@login_required
def gpa():
    return render_template("gpa.html")


@bp.route("/wellness")
@login_required
def wellness():
    return render_template("wellness.html")


@bp.route("/resume-builder")
@login_required
def resume_builder():
    return render_template("resume_builder.html")


@bp.route("/timetable")
@login_required
def timetable():
    return render_template("timetable.html")
