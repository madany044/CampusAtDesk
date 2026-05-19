from datetime import datetime

from extensions import db


class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    required_skills = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(200), nullable=True)
    job_type = db.Column(db.String(100), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)
    posted_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    category = db.relationship("Category", backref="jobs", foreign_keys=[category_id])
    poster = db.relationship("User", backref="posted_jobs", foreign_keys=[posted_by])
