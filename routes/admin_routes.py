from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from models.user import User
from models.company import Company
from extensions import db
from utils.role_helpers import require_role


def register_admin_routes(app):

    @app.route("/admin/dashboard")
    @require_role("admin")
    def admin_dashboard():
        users_count = User.query.count()
        recruiters_count = User.query.filter_by(role="recruiter").count()
        students_count = User.query.filter_by(role="student").count()
        return render_template(
            "admin_dashboard.html",
            users_count=users_count,
            recruiters_count=recruiters_count,
            students_count=students_count
        )

    @app.route("/admin/users")
    @require_role("admin")
    def admin_users():
        users = User.query.order_by(User.created_at.desc()).all()
        return render_template("admin_users.html", users=users)

    @app.route("/admin/students")
    @require_role("admin")
    def admin_students():
        branch = request.args.get("branch", "")
        query = User.query.filter_by(role="student")
        if branch:
            query = query.filter_by(branch=branch)
        students = query.order_by(User.created_at.desc()).all()
        branches = ["CSE", "ME", "CE"]
        return render_template("admin_students.html", students=students, branches=branches, selected_branch=branch)

    @app.route("/admin/recruiters")
    @require_role("admin")
    def admin_recruiters():
        recruiters = User.query.filter_by(role="recruiter").order_by(User.created_at.desc()).all()
        return render_template("admin/recruiters.html", recruiters=recruiters)

    @app.route("/admin/recruiters/create", methods=["GET", "POST"])
    @require_role("admin")
    def admin_recruiter_create():
        companies = Company.query.order_by(Company.name).all()
        if request.method == "POST":
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
            company_id = request.form.get("company_id") or None
            if User.query.filter_by(username=username).first():
                flash("Username already exists.", "error")
                return redirect(url_for("admin_recruiter_create"))
            if User.query.filter_by(email=email).first():
                flash("Email already registered.", "error")
                return redirect(url_for("admin_recruiter_create"))
            user = User(
                username=username,
                email=email,
                password=generate_password_hash(password),
                role="recruiter",
                company_id=company_id,
                is_active=True
            )
            db.session.add(user)
            db.session.commit()
            flash("Recruiter created successfully.", "success")
            return redirect(url_for("admin_recruiters"))
        return render_template("admin/recruiter_form.html", recruiter=None, companies=companies)

    @app.route("/admin/recruiters/edit/<int:id>", methods=["GET", "POST"])
    @require_role("admin")
    def admin_recruiter_edit(id):
        recruiter = User.query.get_or_404(id)
        companies = Company.query.order_by(Company.name).all()
        if request.method == "POST":
            recruiter.username = request.form.get("username", recruiter.username)
            recruiter.email = request.form.get("email", recruiter.email)
            recruiter.company_id = request.form.get("company_id") or None
            recruiter.is_active = request.form.get("is_active") == "1"
            db.session.commit()
            flash("Recruiter updated successfully.", "success")
            return redirect(url_for("admin_recruiters"))
        return render_template("admin/recruiter_form.html", recruiter=recruiter, companies=companies)