# config.py → Database ki settings rakhti hai
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY="Ayza_Task_Flow"
    SQLALCHEMY_DATABASE_URI="sqlite:///taskflow.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    