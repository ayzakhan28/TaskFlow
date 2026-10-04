from models import db
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False, unique=True )
    password=db.Column(db.String(255),nullable=False)
    role=db.Column(db.String(30),default="user")
    profile_image=db.Column(db.String(255),nullable=True)
    is_active=db.Column(db.Boolean,default=True)
    created_at=db.Column(db.DateTime,  default=datetime.utcnow)