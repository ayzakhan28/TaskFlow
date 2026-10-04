from flask import Blueprint, render_template, redirect, session, url_for, request, flash
from models.user import User
from models import db
from models.tasks import Task


admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("user_role") != "admin":
        return redirect(url_for("user.dashboard"))

    search = request.args.get("search", "")

    page = request.args.get(
        "page",
        1,
        type=int
    )

    per_page = 5

    query = User.query.filter(
        User.name.ilike(f"%{search}%")
    )

    users = query.paginate(
        page=page,
        per_page=per_page
    )

    total_users = User.query.count()

    return render_template(
        "admin/dashboard.html",
        total_users=total_users,
        users=users,
        search=search
    )


@admin_bp.route(
    "/admin/user/edit/<int:user_id>",
    methods=["GET", "POST"]
)
def edit_user(user_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("user_role") != "admin":
        return redirect(url_for("user.dashboard"))

    user = User.query.get_or_404(user_id)

    if user.id == session["user_id"]:
        flash("You cannot edit your own account from Admin Panel.")
        return redirect(url_for("admin.dashboard"))

    if request.method == "POST":

        user.name = request.form.get("name")
        user.email = request.form.get("email")

        role = request.form.get("role")

        if role not in ["user", "admin"]:
            flash("Invalid role selected.")
            return redirect(
                url_for(
                    "admin.edit_user",
                    user_id=user_id
                )
            )

        user.role = role

        db.session.commit()

        flash("User updated successfully!")

        return redirect(url_for("admin.dashboard"))

    return render_template(
        "admin/edit_user.html",
        user=user
    )


@admin_bp.route(
    "/admin/user/toggle-status/<int:user_id>",
    methods=["POST"]
)
def toggle_user_status(user_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("user_role") != "admin":
        return redirect(url_for("user.dashboard"))

    user = User.query.get_or_404(user_id)

    # Admin apna account deactivate nahi kar sakta
    if user.id == session["user_id"]:
        flash("You cannot deactivate your own account.")
        return redirect(url_for("admin.dashboard"))

    # Active ko inactive aur inactive ko active karo
    user.is_active = not user.is_active

    db.session.commit()

    if user.is_active:
        flash("User activated successfully!")
    else:
        flash("User deactivated successfully!")

    return redirect(url_for("admin.dashboard"))


@admin_bp.route(
    "/admin/user/delete/<int:user_id>",
    methods=["POST"]
)
def delete_user(user_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("user_role") != "admin":
        return redirect(url_for("user.dashboard"))

    user = User.query.get_or_404(user_id)

    # Admin apna account delete nahi kar sakta
    if user.id == session["user_id"]:
        flash("You cannot delete your own account.")
        return redirect(url_for("admin.dashboard"))

    # User ke tamam tasks pehle delete karo
    Task.query.filter_by(
        user_id=user.id
    ).delete()

    # Ab user delete karo
    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully!")

    return redirect(url_for("admin.dashboard"))