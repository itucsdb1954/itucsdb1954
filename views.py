from flask import render_template,current_app,request,redirect,url_for
from datetime import datetime
from database import Database
from course import Course
from forms import LoginForm
from user import User

def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data["username"]
        user = get_user(username)
        if user is not None:
            password = form.data["password"]
            if hasher.verify(password, user.password):
                login_user(user)
                flash("You have logged in.")
                next_page = request.args.get("next", url_for("home_page"))
                return redirect(next_page)
        flash("Invalid credentials.")
    return render_template("login.html", form=form)


def logout_page():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("home_page"))

def home_page():
    today=datetime.today()
    day_name=today.strftime("%A")
    return render_template("homepage.html",day=day_name)

def courses_page():
    db = current_app.config["db"]
    if request.method =="GET":
        courses=db.get_courses()
        return render_template("coursespage.html", courses=sorted(courses))
    else:
        if not current_user.is_admin:
            abort(401)
        form_course_keys=request.form.getlist("course_keys")
        for form_course_key in form_course_keys:
            db.delete_course(int(form_course_key))
        return redirect(url_for("courses_page"))

def course_page(course_key):
    db = current_app.config["db"]
    course=db.get_course(course_key)
    return render_template("coursepage.html", course=course)


def course_add_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == "GET":
        values={"name":"","department":"","description":"","lecturerName":"","VF_conditions":""}
        return render_template("course_edit.html",values=values)
    else:
        valid=validate_course_form(request.form)
        if not valid:
            return render_template("course_edit.html",values=request.form)
        form_name = request.form["name"]
        form_department = request.form["department"]
        form_description = request.form["description"]
        form_lecturerName = request.form["lecturerName"]
        form_VF_conditions = request.form["VF_conditions"]
        course = Course(form_name,form_department,form_description,form_lecturerName,form_VF_conditions)
        db = current_app.config["db"]
        course_key = db.add_course(course)
        return redirect(url_for("course_page",course_key=course_key))


def course_edit_page(course_key):
    if request.method == "GET":
        db = current_app.config["db"]
        course =db.get_course(course_key)
        if course is None:
            abort(404)
        values={"name":"","department":"","description":"","lecturerName":"","VF_conditions":""}
        return render_template("course_edit.html",values=values)
    else:
        valid=validate_course_form(request.form)
        if not valid:
            return render_template("course_edit.html",values=request.form)
        name = request.form.data["name"]
        department = request.form.data["department"]
        description = request.form.data["description"]
        lecturerName = request.form.data["lecturerName"]
        VF_conditions = request.form.data["VF_conditions"]
        course = Course(name,department,description,lecturerName,VF_conditions)
        db = current_app.config["db"]
        db.update_course(course_key,course)
        return redirect(url_for("course_page",course_key=course_key))


def validate_course_form(form):
    form.data={}
    form.errors={}

    form_name=form.get("name","").strip()
    if len(form_name)==0:
        form.errors["name"]="Name can not be blank."
    else:
        form.data["name"]=form_name

    form_department=form.get("department","").strip()
    if len(form_department)==0:
        form.errors["department"]="Department can not be blank."
    else:
        form.data["department"]=form_department

    form_description=form.get("description","").strip()
    if len(form_description)==0:
        form.errors["description"]="Description can not be blank."
    else:
        form.data["description"]=form_description

    form_lecturerName=form.get("lecturerName","").strip()
    if len(form_lecturerName)==0:
        form.errors["lecturerName"]="LecturerName can not be blank."
    else:
        form.data["lecturerName"]=form_lecturerName

    form_VF_conditions=form.get("VF_conditions","").strip()
    if len(form_VF_conditions)==0:
        form.errors["VF_conditions"]="VF Conditions can not be blank."
    else:
        form.data["VF_conditions"]=form_VF_conditions

    return len(form.errors)==0
