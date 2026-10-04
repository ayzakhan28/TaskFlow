from models import db
from datetime import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    description = db.Column(db.Text, nullable=True)

    status = db.Column(db.String(30), default="pending")

    priority = db.Column(db.String(30), default="medium")

    due_date = db.Column(db.Date, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)