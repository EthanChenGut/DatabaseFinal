from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import Professor, SchoolExperience, WorkExperience, ClassSchedule, Award, Paper
from datetime import datetime

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("Professor.html", professor=Professor.query.first())

@views.route("/professor/<professor_id>")
def professor(professor_id):
    return render_template("professor.html", professor=Professor.query.filter_by(professor_id=professor_id).first())

@views.route("/professor/<professor_id>/edit-introduction", methods=["GET", "POST"])
def edit_introduction(professor_id):
    professor = Professor.query.filter_by(professor_id = professor_id).first()
    if request.method == "POST":
        self_introduction = request.form.get("introduction")
        professor.self_introduction = self_introduction

        db.session.commit()
        flash("Change saved", category="success")

        return redirect(url_for("views.home"))

    return render_template("edit_self_introduction.html", professor=professor)


@views.route("/professor/<professor_id>/class-schedule")
def class_schedule(professor_id):
    professor = Professor.query.filter_by(professor_id=professor_id).first()
    schedules = professor.class_schedules
    schedules_table = []
    for i in range(8):
        schedules_table.append([" "] * 14)

    for schedule in schedules:
        schedules_table[schedule.week-1][schedule.time-1] = schedule.name

    return render_template("class_schedule.html", professor=professor, schedules_table=schedules_table)

@views.route("/professor/<professor_id>/class-schedule/add-class", methods=['GET', 'POST'])
def add_class_schedule(professor_id):
    if request.method == "POST":
        week = request.form.get("week")
        time = request.form.get("time")
        name = request.form.get("name")

        if ClassSchedule.query.filter_by(week=week, time=time, professor_id=professor_id).first():
            flash("This time is not vacant.", category="error")

            return render_template("add_class.html", professor=Professor.query.filter_by(professor_id=professor_id).first())

        classSchedule = ClassSchedule(week, time, name, professor_id)
        db.session.add(classSchedule)
        db.session.commit()
        flash("Add Class", category="success")
        return redirect(url_for("views.class_schedule", professor_id=professor_id))
    return render_template("add_class.html", professor=Professor.query.filter_by(professor_id=professor_id).first())


# @views.route("/professor/<professor_id>/class-schedule/delete-class", methods=["GET", "POST"])
# def delete_class_schedule(professor_id, schedule_id):
    
#     if request.method == "POST":
#         schedule_id = request.form.get("delete-classID")
#         schedule = db.session.query(ClassSchedule).filter_by(schedule_id=schedule_id).all()

#         for i in schedule:
#             db.session.delete(i)
#         db.session.commit()

#         flash("Delete Class", category="success")
#         return redirect(url_for("views.class_schedule", professor_id=professor_id))
#     return render_template("delete_class.html", professor=Professor.query.filter_by(professor_id=professor_id).first())

@views.route("/professor/<professor_id>/class-schedule/delete-class/", methods=["GET", "POST"])
def delete_class_schedule(professor_id):
    if request.method == "POST":
        name = request.form.get("delete-class-name")

        if name:
            schedule = db.session.query(ClassSchedule).filter_by(name=name).all()

            if schedule:
                for item in schedule:
                    db.session.delete(item)
                db.session.commit()
                flash(f"Deleted all classes with name '{name}'", category="success")
            else:
                flash(f"No classes found with name '{name}'", category="error")
        else:
            flash("Class name not provided", category="error")

        return redirect(url_for("views.class_schedule", professor_id=professor_id))
    return render_template("delete_class.html", professor=Professor.query.filter_by(professor_id=professor_id).first())


@views.route("/professor/<professor_id>/edit-interest", methods=["GET", "POST"])
def edit_interest(professor_id):
    professor = Professor.query.filter_by(professor_id = professor_id).first()
    if request.method == "POST":
        interest = request.form.get("interest")
        professor.interest =interest
        db.session.commit()
        flash("Change saved", category="success")

        return redirect(url_for("views.home"))

    return render_template("edit_interest.html", professor=professor)



@views.route("/add-work-experience/", methods=["GET", "POST"])
def add_work_experience():
    if request.method == "POST":
        company_name = request.form.get("company_name")
        position = request.form.get("position")

        experience = WorkExperience(company_name, position, professor_id=1)

        db.session.add(experience)
        db.session.commit()

        flash("Add Work Experience", category="success")
        return redirect(url_for("views.home"))

    return render_template("add_work_experience.html")

@views.route("/professor/<professor_id>/delete-work-experience/<WorkExperience_id>", methods=["GET", "POST"])
def delete_WorkExperience(professor_id, WorkExperience_id):
    workE = db.session.query(WorkExperience).filter_by(WorkExperience_id=WorkExperience_id).all()
    for item in workE:
        db.session.delete(item)
    db.session.commit()
    flash("Delete WorkExperience", category="success")
    return redirect(url_for("views.home"))


@views.route("/add-school-experience/", methods=["GET", "POST"])
def add_school_experience():
    if request.method == "POST":
        school = request.form.get("school")
        dept = request.form.get("dept")
        degree = request.form.get("degree")

        experience = SchoolExperience(school, dept, degree, professor_id=1)

        db.session.add(experience)
        db.session.commit()

        flash("Add School Experience", category="success")
        return redirect(url_for("views.home"))

    return render_template("add_school_experience.html")

@views.route("/professor/<professor_id>/delete-school-experience/<SchoolExperience_id>", methods=["GET", "POST"])
def delete_SchoolExperience(professor_id, SchoolExperience_id):
    schoolE = db.session.query(SchoolExperience).filter_by(SchoolExperience_id=SchoolExperience_id).all()
    for item in schoolE:
        db.session.delete(item)
    db.session.commit()
    flash("Delete SchoolExperience", category="success")
    return redirect(url_for("views.home"))


@views.route("/add-paper/", methods=["GET", "POST"])
def add_paper():
    if request.method == "POST":
        paper_name = request.form.get("paper_name")
        collaborators = request.form.get("collaborators")
        page_number_of_the_paper = request.form.get("page_number_of_the_paper")
        indexed_website = request.form.get("indexed_website")
        indexed_time = request.form.get("indexed_time")
        date_format = "%Y-%m-%d"
        indexed_time = datetime.strptime(indexed_time, date_format).date()
        paper = Paper(paper_name, collaborators, page_number_of_the_paper, indexed_website, indexed_time)

        if Paper.query.filter_by(paper_name=paper_name).first():
            paper = Paper.query.filter_by(paper_name=paper_name).first()
            if paper.compare(paper):
                # paper.professor.append()
                db.session.commit()

                return redirect(url_for("views.home"))
            else:
                flash("Paper already exists", category="error")
        else:
            db.session.add(paper)
            db.session.commit()

            flash("Add Paper", category="success")
            return redirect(url_for("views.home"))
    return render_template("add_paper.html")


@views.route("/add-award/", methods=["GET", "POST"])
def add_award():
    if request.method == "POST":
        award_name = request.form.get("award_name")
        government = request.form.get("government")
        year = int(request.form.get("year"))
        awardtime = request.form.get("awardtime")
        
        
        if Award.query.filter_by(award_name=award_name, government=government, year=year, awardtime=awardtime).first():
            flash("The award already exists", category="error")
            return render_template("add_award.html")
        else:
            award = Award(award_name, government, year, awardtime, professor_id=1)
            db.session.add(award)
            db.session.commit()

            flash("Add Awards", category="success")
            return redirect(url_for("views.home"))
    return render_template("add_award.html")

@views.route("/professor/<professor_id>/delete-award/<award_id>", methods=["GET", "POST"])
def delete_award(professor_id, award_id):
    awarditem = db.session.query(Award).filter_by(award_id=award_id).all()
    for item in awarditem:
        db.session.delete(item)
    db.session.commit()
    flash("Delete SchoolExperience", category="success")
    return redirect(url_for("views.home"))
