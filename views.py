from flask import render_template,current_app,request,redirect,url_for,flash,abort
from flask_login import login_user ,logout_user,current_user
from passlib.hash import pbkdf2_sha256 as hasher
from datetime import datetime
from database import Database
from course import Course
from forms import LoginForm
from user import User,get_user
from Homework import Homework
from Project import Project
from Attendance import Attendance
from VF_Cond import Cond
from Midterm import Midterm

def logout_page():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("home_page"))

def home_page():
    today=datetime.today()
    day_name=today.strftime("%A")
    form = LoginForm()
    if request.method=="GET":
        return render_template("homepage.html",day=day_name,form=form)
    else:
        if form.validate_on_submit():
            username = form.data["username"]
            user = get_user(username)
            if user is not None:
                password = form.data["password"]
                if hasher.verify(password, user.password):
                    login_user(user)
                    flash("You have logged in.")
                    next_page = request.args.get("next", url_for("guide_page"))
                    return redirect(next_page)
            flash("Invalid credentials.")
        return render_template("homepage.html",day=day_name,form=form)

def courses_page():
    db = Database("postgres://eqxokbcjiseyei:3bc64a91ec58aab73ba937f8652296acf5ab9b2671aba9deb9420dfbe25e5cf6@ec2-46-137-188-105.eu-west-1.compute.amazonaws.com:5432/d1f2968dk53lod")
    if request.method =="GET":
        courses=db.get_courses()
        return render_template("coursespage.html", courses=courses)
    else:
        form_course_keys=request.form.getlist("course_keys")
        for form_course_key in form_course_keys:
            db.delete_course(int(form_course_key))
            return redirect(url_for("courses_page"))

def course_page(course_key):
    db = current_app.config["db"]
    course=db.get_course(course_key)
    return render_template("coursepage.html", course=course)


def course_add_page():

    if request.method == "GET":
        values={"name":"","department":"","description":"","lecturerName":"","VF_conditions":""}
        return render_template("course_add.html",values=values)
    else:
        valid=validate_course_form(request.form)
        if not valid:
            return render_template("course_add.html",values=request.form)
        form_name = request.form["name"]
        form_department = request.form["department"]
        form_description = request.form["description"]
        form_lecturerName = request.form["lecturerName"]
        form_VF_conditions = request.form["VF_conditions"]
        course = Course(form_name,form_department,form_description,form_lecturerName,form_VF_conditions)
        db = current_app.config["db"]
        course_key = db.add_course(course)
        return redirect(url_for("courses_page"))



def course_edit_page(course_key):
    if request.method == "GET":
        db = current_app.config["db"]
        course =db.get_course(course_key)
        if course is None:
            abort(404)
        values={"name":course.name,"department":course.department,"description":course.description,"lecturerName":course.lecturerName,"VF_conditions":course.VF_conditions}
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

def user_page():
    return render_template("userpage.html")

def guide_page():
    return render_template("guide.html")

def conditionAdding_page(course_key):
    db = current_app.config["db"]
    course=db.get_course(course_key)
    if request.method == "GET":
        return render_template("VFadd.html",course=course)
    else:

        Number_of_Midterm = request.form["Number_of_Midterm"]
        weighted_of_Midterm = request.form["weighted_of_Midterm"]
        if weighted_of_Midterm=="0":
            is_important=False
        else:
            is_important=True

        midterm=Midterm(Number_of_Midterm,weighted_of_Midterm,is_important,course_key)

        Number_of_Homework = request.form["Number_of_Homework"]
        weighted_of_Homework = request.form["weighted_of_Homework"]
        if weighted_of_Homework=="0":
            is_important=False
        else:
            is_important=True

        homework=Homework(Number_of_Homework,weighted_of_Homework,is_important,course_key)

        Number_of_Project = request.form["Number_of_Project"]
        weighted_of_Project = request.form["weighted_of_Project"]
        if weighted_of_Project=="0":
            is_important=False
        else:
            is_important=True
        project=Project(Number_of_Project,weighted_of_Project,is_important,course_key)

        attendance = request.form["attendance"]
        upper_limit_percent = request.form["upper_limit_percent"]
        if attendance==1:
            is_important=True
        else:
            is_important=False

        attendance=Attendance(upper_limit_percent,is_important,course_key)
        db = current_app.config["db"]
        db.add_midterm(midterm)
        db.add_homework(homework)
        db.add_project(project)
        db.add_attendance(attendance)
        return redirect(url_for("conditions_page",course_key=course_key))

def conditions_page(course_key):
    db = current_app.config["db"]
    course=db.get_course(course_key)
    midterm=db.get_midterm(course_key)
    homework=db.get_homework(course_key)
    project=db.get_project(course_key)
    attendance=db.get_attendance(course_key)
    midterm_score=[]
    if request.method == "GET":
        return render_template("VFcond.html",midterm=midterm,homework=homework,project=project,attendance=attendance,course=course)
    else:
        midterm.midterm_score[0] = request.form["Midterm1"]
        midterm.midterm_score[1] = request.form["Midterm2"]

        homework.homework_score[0] = request.form["Homework1"]
        homework.homework_score[1] = request.form["Homework2"]
        homework.homework_score[2] = request.form["Homework3"]
        homework.homework_score[3] = request.form["Homework4"]

        project.project_score[0]= request.form["Project1"]
        project.project_score[1]= request.form["Project2"]

        attendance.attendance[0]=request.form.get("week1")
        print(attendance.attendance[0])
        attendance.attendance[1]=request.form.get("week2")
        attendance.attendance[2]=request.form.get("week3")
        attendance.attendance[3]=request.form.get("week4")
        attendance.attendance[4]=request.form.get("week5")
        attendance.attendance[5]=request.form.get("week6")
        attendance.attendance[6]=request.form.get("week7")
        attendance.attendance[7]=request.form.get("week8")
        attendance.attendance[8]=request.form.get("week9")
        attendance.attendance[9]=request.form.get("week10")
        attendance.attendance[10]=request.form.get("week11")
        attendance.attendance[11]=request.form.get("week12")
        attendance.attendance[12]=request.form.get("week13")
        attendance.attendance[13]=request.form.get("week14")

        return render_template("VFcond.html",midterm=midterm,homework=homework,project=project,attendance=attendance,course=course)



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
