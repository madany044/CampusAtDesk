from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash

from extensions import db
from models.user import User


def register_recruiter_routes(app):

    @app.route("/recruiter/register", methods=["GET", "POST"])
    def recruiter_register():

        if request.method == "POST":

            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
            company_id = request.form.get("company_id")

            existing_user = User.query.filter_by(email=email).first()

            if existing_user:
                flash("Email already exists", "danger")
                return redirect(url_for("recruiter_register"))

            hashed_password = generate_password_hash(password)

            user = User(
                username=username,
                email=email,
                password=hashed_password,
                role="recruiter",
                company_id=company_id,
                is_active=True
            )

            db.session.add(user)
            db.session.commit()

            flash("Recruiter registered successfully", "success")
            return redirect(url_for("login"))

        return render_template("recruiter_register.html")