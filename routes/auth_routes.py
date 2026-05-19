from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db
from models.user import User


def register_auth_routes(app):

    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":

            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
            confirm_password = request.form.get("confirm_password")
            branch = request.form.get("branch")

            if password != confirm_password:
                flash("Passwords do not match", "danger")
                return redirect(url_for("register"))

            existing_user = User.query.filter_by(email=email).first()

            if existing_user:
                flash("Email already exists", "danger")
                return redirect(url_for("register"))

            hashed_password = generate_password_hash(password)

            user = User(
                username=username,
                email=email,
                password=hashed_password,
                role="student",
                branch=branch,
                is_active=True
            )

            db.session.add(user)
            db.session.commit()

            flash("Registration successful", "success")
            return redirect(url_for("login"))

        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():

        if request.method == "POST":

            email = request.form.get("email")
            password = request.form.get("password")

            user = User.query.filter_by(email=email).first()

            if user and check_password_hash(user.password, password):

                session["user_id"] = user.id
                session["user_role"] = user.role

                if user.role == "student":
                    return redirect("/student/dashboard")

                elif user.role == "recruiter":
                    return redirect("/recruiter/dashboard")

                elif user.role == "admin":
                    return redirect("/admin/dashboard")

                return redirect("/")

            flash("Invalid email or password", "danger")

        return render_template("login.html")

    @app.route("/logout")
    def logout():

        session.clear()
        flash("Logged out successfully", "success")

        return redirect(url_for("login"))