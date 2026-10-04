from flask import Blueprint,render_template,flash,redirect,request,url_for,session
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
from models import db
from models.user import User

auth_bp=Blueprint("auth", __name__)   #Blueprint = Flask application ka ek chhota organized section.

@auth_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")
        confirm_password=request.form.get("confirm_password")

        if password != confirm_password:
            flash ("Password cannot match..")
            return redirect(url_for("auth.register"))
        
        existed_user=User.query.filter_by(email=email).first()
        if existed_user:
            flash("This email is already registerd")
            return redirect(url_for("auth.register"))

        hashed_password=generate_password_hash(password)
        
        new_user=User(
            name=name,
            email=email,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Registration Successfully!.Please Login.")
        return redirect(url_for("auth.register"))
    return render_template("auth/register.html")

@auth_bp.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        user=User.query.filter_by(email=email).first()
        if not user:
            flash("Invalid Email or Password ")
            return redirect(url_for("auth.login"))
        if not user.is_active:
            flash("Your account is inactive..")
            return redirect(url_for("auth.login"))
        if not check_password_hash(user.password,password):
            flash("Invalide Your Password.. Please Try Again.")
            return redirect(url_for("auth.login"))
        
        session["user_id"]=user.id
        session["user_name"]=user.name
        session["user_role"]=user.role

        flash("Login Successfully..")

        if user.role=="admin":
            return redirect(url_for("admin.dashboard"))
        return redirect(url_for("user.dashboard"))


    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logout..")
    return redirect(url_for("auth.login"))

        
