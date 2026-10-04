from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import db
from models.tasks import Task
from datetime import datetime


task_bp = Blueprint("task", __name__)





@task_bp.route("/task/create", methods=["GET", "POST"])
def create_task():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        title = request.form.get("title")
        description = request.form.get("description")
        status = request.form.get("status")
        priority = request.form.get("priority")
        due_date = request.form.get("due_date")

        if not due_date:
            flash("Please select your date...")
            return redirect(url_for("task.create_task"))



        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

        new_task = Task(
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date,
            user_id=session["user_id"]
        )

        db.session.add(new_task)
        db.session.commit()

        flash("Task created successfully!")

        return redirect(url_for("user.dashboard"))

    return render_template("tasks/create.html")

@task_bp.route("/task/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    task = Task.query.get_or_404(task_id)

    if task.user_id != session["user_id"]:
        flash("You are not allowed to edit this task.")
        return redirect(url_for("user.dashboard"))

    if request.method == "POST":

        task.title = request.form.get("title")
        task.description = request.form.get("description")
        task.status = request.form.get("status")
        task.priority = request.form.get("priority")

        due_date = request.form.get("due_date")

        if  not due_date:
            flash("Please Select your date..")
            return render_template("tasks/edit.html",task=task,due_date="")
        
        due_date = datetime.strptime(
                due_date,
                "%Y-%m-%d"
            ).date()

        task.due_date = due_date

        db.session.commit()

        flash("Task updated successfully!")

        return redirect(url_for("user.dashboard"))

    return render_template(
        "tasks/edit.html",
        task=task
    )

@task_bp.route("/task/delete/<int:task_id>",methods=["GET","POST"])
def delete_task(task_id):
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    task=Task.query.get_or_404(task_id)

    if task.user_id != session["user_id"]:
        flash("You are not elgible for delete this task..")
        return redirect(url_for("user.dashboard"))

    db.session.delete(task)
    db.session.commit()
    flash("You are successfuly delete this task")
    return redirect(url_for("user.dashboard"))

