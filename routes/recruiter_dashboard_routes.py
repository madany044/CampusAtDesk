from flask import render_template, session
from models.job import Job
from models.application import Application
from utils.role_helpers import require_role


def register_recruiter_dashboard_routes(app):

    @app.route("/recruiter/dashboard")
    @require_role("recruiter")
    def recruiter_dashboard():
        user_id = session.get("user_id")
        jobs = Job.query.filter_by(posted_by=user_id).order_by(Job.created_at.desc()).all()
        applications = Application.query.join(Job).filter(Job.posted_by == user_id).order_by(Application.created_at.desc()).all()
        return render_template(
            "recruiter/dashboard.html",
            jobs=jobs,
            applications=applications
        )

    @app.route("/recruiter/applications")
    @require_role("recruiter")
    def recruiter_applications():
        user_id = session.get("user_id")
        applications = Application.query.join(Job).filter(Job.posted_by == user_id).order_by(Application.created_at.desc()).all()
        return render_template("recruiter/applications.html", applications=applications)