# app.py → Flask app aur database ko connect karta hai
from flask import Flask,render_template
from models import db
from config import Config
from models.user import User
from routes.auth import auth_bp
from flask_migrate import Migrate
from routes.user import user_bp
from routes.admin import admin_bp
from models.tasks import Task
from routes.task import task_bp
from flask_wtf.csrf import CSRFProtect
app=Flask(__name__)
app.config.from_object(Config)
csrf=CSRFProtect(app)
db.init_app(app)
migrate=Migrate(app,db)
app.register_blueprint(auth_bp)  #usse main Flask application ke saath connect/register karte hain.
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(task_bp)



@app.route("/")
def home():
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'),500
if __name__=="__main__":
    app.run(debug=True)