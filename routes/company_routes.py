from flask import render_template, request, redirect, url_for, flash

from extensions import db
from models.company import Company
from utils.role_helpers import require_role


def register_company_routes(app):

    @app.route("/admin/companies")
    @require_role("admin")
    def admin_companies():
        companies = Company.query.order_by(Company.name).all()
        return render_template("admin/companies.html", companies=companies)

    @app.route("/admin/companies/create", methods=["GET", "POST"])
    @require_role("admin")
    def admin_company_create():
        if request.method == "POST":
            name = request.form.get("name", "").strip()
            location = request.form.get("location", "").strip() or None
            if not name:
                flash("Company name is required.", "error")
                return redirect(url_for("admin_company_create"))
            company = Company(name=name, location=location)
            db.session.add(company)
            db.session.commit()
            flash("Company created successfully.", "success")
            return redirect(url_for("admin_companies"))
        return render_template("admin/company_form.html", company=None)

    @app.route("/admin/companies/edit/<int:id>", methods=["GET", "POST"])
    @require_role("admin")
    def admin_company_edit(id):
        company = Company.query.get_or_404(id)
        if request.method == "POST":
            name = request.form.get("name", "").strip()
            location = request.form.get("location", "").strip() or None
            if not name:
                flash("Company name is required.", "error")
                return redirect(url_for("admin_company_edit", id=id))
            company.name = name
            company.location = location
            db.session.commit()
            flash("Company updated successfully.", "success")
            return redirect(url_for("admin_companies"))
        return render_template("admin/company_form.html", company=company)
