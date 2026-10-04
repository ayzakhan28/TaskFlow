from flask import Blueprint, render_template, session, redirect, url_for, request
from models.tasks import Task


user_bp = Blueprint("user", __name__)


@user_bp.route("/user/dashboard")
def dashboard():

    # Check karo user login hai ya nahi
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    search = request.args.get("search", "")
    status = request.args.get("status", "")
    page= request.args.get("page",1,type=int)
    due_date =request.form.get("due_date")
    per_page=10
    # Base query
    query = Task.query.filter(
        Task.user_id == session["user_id"],
        Task.title.ilike(f"%{search}%")
    )

    # Status filter
    if status:
        query = query.filter(
            Task.status == status
        )

    

    tasks=query.paginate(
        page=page,
        per_page=per_page
    )    

    # Query execute
    # tasks = query.all()


    return render_template(
        "user/dashboard.html",
        tasks=tasks,
        search=search,
        status=status
    )