Parts Implemented by ALPER MERİÇ
================================

courses Table
-------------
* "courses" Table holds the course information in the database.It's id references "user_course" table.Content of table is below:
.. code-block:: python

	INIT_STATEMENTS = [
	"""
	CREATE TABLE IF NOT EXISTS courses(
		id SERIAL PRIMARY KEY,
		department VARCHAR(50),
		course_name VARCHAR(100) ,
		course_description VARCHAR(100) ,
		lecturer_name VARCHAR(100) ,
		vf_condition INTEGER,
		username VARCHAR(50) NOT NULL
	);
	"""
	]

* There is a "Course" class to use at database operations:
.. code-block:: python

	class Course:
		def __init__(self,name,department,description,lecturerName,VF_conditions):
			self.department=department
			self.name=name
			self.lecturerName=lecturerName
			self.description=description
			self.VF_conditions=VF_conditions
* There is functions to access and manipulate "courses" table at the database.For example adding a Course object to database is :
.. code-block:: python

	def add_course(self,course,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO courses (department,course_name, lecturer_name,course_description,VF_condition,username) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (course.department, course.name, course.lecturerName, course.description,course.VF_conditions,username))
            connection.commit()
            course_key = cursor.lastrowid
        return course_key
* Deleting course from database by using key:
.. code-block:: python

	 def delete_course(self,course_key,username):
         with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM courses WHERE (ID = %s AND username = %s)"
            cursor.execute(query, (course_key,username,))
            connection.commit()
* Getting a course from database by using key:
.. code-block:: python

	def get_course(self,course_key,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT department, course_name, lecturer_name,course_description, VF_condition FROM courses WHERE (id = %s AND username = %s)"
            cursor.execute(query, (course_key,username))
            department, name, lecturerName, description, VF_conditions = cursor.fetchone()
        course_=Course(name,department,description,lecturerName,VF_conditions)
        return course_
* Getting all courses from database:
.. code-block:: python

	def get_courses(self,username):
        courses = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT id,department,course_name,lecturer_name,course_description,VF_condition FROM courses WHERE(username=%s) ORDER BY ID"
            cursor.execute(query,(username,))
            for course_key, department,name, lecturerName, description, VF_conditions in cursor:
                course=Course(name, department,description,lecturerName,VF_conditions)
                courses.append((course_key, course) )
        return courses
* Updating course at database by using key :
.. code-block:: python

	def update_course(self,course_key,Course,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE courses SET department = %s, course_name = %s, lecturer_name = %s, course_description = %s, VF_condition = %s WHERE (ID = %s AND username=%s)"
            cursor.execute(query, (Course.department,Course.name,Course.lecturerName,Course.description,Course.VF_conditions, course_key,username))
            connection.commit()
        return course_key

homeworks Table
---------------
* "homeworks" Table stores homework points at database.It's "id" references "vf_condition" table.Content of table is below:
.. code-block:: python

	INIT_STATEMENTS = [
	"""
		CREATE TABLE IF NOT EXISTS homeworks(
			id SERIAL PRIMARY KEY,
			number_of_homework INTEGER ,
			homework_weight INTEGER CHECK(homework_weight<100 AND homework_weight>=0),
			homework_score1 INTEGER DEFAULT(0),
			homework_score2 INTEGER DEFAULT(0),
			homework_score3 INTEGER DEFAULT(0),
			homework_score4 INTEGER DEFAULT(0),
			is_important BOOLEAN,
			username VARCHAR(50) NOT NULL
		);
	"""
	]
	
* There is a "Homework" class to use at database operations:
.. code-block:: python

	class Homework:
    	def __init__(self,number_of_homework,homework_weight,is_important,course_key):
        	self.number_of_homework=number_of_homework
		self.homework_weight=homework_weight
		self.homework_score=[0,0,0,0]
		self.is_important=is_important
		self.id=course_key
		
* There is functions to access and manipulate "homeworks" table at the database.For example adding a Homework object 
to database is :
.. code-block:: python

	def add_homework(self,Homework,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO homeworks(number_of_homework, homework_weight, homework_score1,homework_score2,homework_score3,homework_score4,is_important,username) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
            cursor.execute(query, (Homework.number_of_homework, Homework.homework_weight, Homework.homework_score[0], Homework.homework_score[1], Homework.homework_score[2], Homework.homework_score[3], Homework.is_important,username))
            connection.commit()
            homework_key = cursor.lastrowid
        return homework_key

* Deleting homework from database by using key:
.. code-block:: python

	def delete_homework(self,homework_key,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM homeworks WHERE (ID = %s AND username=%s)"
            cursor.execute(query, (homework_key,username))
            connection.commit()
			
* Getting a homework from database by using key:
.. code-block:: python

	def get_homework(self,homework_key,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT number_of_homework, homework_weight, homework_score1,homework_score2,homework_score3,homework_score4,is_important FROM homeworks WHERE (id = %s AND username=%s)"
            cursor.execute(query, (homework_key,username))
            number_of_homework, homework_weight, homework_score1,homework_score2,homework_score3,homework_score4,is_important = cursor.fetchone()
            homework_ = Homework(number_of_homework, homework_weight,is_important,homework_key)
            homework_.homework_score[0]= homework_score1
            homework_.homework_score[1]= homework_score2
            homework_.homework_score[2]= homework_score3
            homework_.homework_score[3]= homework_score4
        return homework_ homework_score1,homework_score2,homework_score3,homework_score4,is_important FROM homeworks WHERE (id = %s)"
            cursor.execute(query, (homework_key,))
            number_of_homework, homework_weight, homework_score1,homework_score2,homework_score3,homework_score4,is_important = cursor.fetchone()
            homework_ = Homework(number_of_homework, homework_weight,is_important,homework_key)
            homework_.homework_score[0]= homework_score1
            homework_.homework_score[1]= homework_score2
            homework_.homework_score[2]= homework_score3
            homework_.homework_score[3]= homework_score4
        return homework_
		
* Updating homework at database by using key :
.. code-block:: python

	 def update_homework(self,homework_key,homework,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE homeworks SET number_of_homework = %s, homework_weight = %s, homework_score1 = %s, homework_score2 = %s, homework_score3 = %s, homework_score4 = %s, is_important = %s WHERE (ID = %s AND username=%s)"
            cursor.execute(query, (homework.number_of_homework,homework.homework_weight,homework.homework_score[0],homework.homework_score[1],homework.homework_score[2],homework.homework_score[3],homework.is_important, homework_key,username))
            connection.commit()
        return homework_key
	

midterms Table
--------------
"midterms" table stores midterms points at database.It's "id" references "vf_condition" table.Content of table given below:
.. code-block:: python

	INIT_STATEMENTS = [
		"""
		CREATE TABLE IF NOT EXISTS midterms(
			id SERIAL PRIMARY KEY,
			number_of_midterm INTEGER ,
			midterm_weight INTEGER CHECK(midterm_weight<100 AND midterm_weight>=0),
			midterm_score1 INTEGER DEFAULT(0),
			midterm_score2 INTEGER DEFAULT(0),
			is_important BOOLEAN,
			username VARCHAR(50) NOT NULL
		);
		"""
	]
* There is a "Midterm" class to use at database operations:
.. code-block:: python

	class Midterm:
   	def __init__(self,number_of_midterm,midterm_weight,is_important,course_key):
        	self.number_of_midterm=number_of_midterm
        	self.midterm_weight=midterm_weight
        	self.midterm_score=[0,0]
        	self.is_important=is_important
        	self.id=course_key
		
* There is functions to access and manipulate "midterms" table at the database.For example adding a Midterm object to database is :
.. code-block:: python

	 def add_midterm(self,Midterm,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO midterms(number_of_midterm, midterm_weight, midterm_score1,midterm_score2,is_important,username) VALUES (%s, %s, %s, %s, %s,%s)"
            cursor.execute(query, (Midterm.number_of_midterm, Midterm.midterm_weight, Midterm.midterm_score[0],Midterm.midterm_score[1], Midterm.is_important,username))
            connection.commit()
            midterm_key = cursor.lastrowid
        return midterm_key
		
* Deleting midterm from database by using key:
.. code-block:: python

	def delete_midterm(self,midterm_key,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM midterms WHERE (ID = %s AND username=%s)"
            cursor.execute(query, (midterm_key,username))
            connection.commit()
* Getting a midterm from database by using key:
.. code-block:: python

	def get_midterm(self,midterm_key,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT number_of_midterm, midterm_weight, midterm_score1,midterm_score2,is_important FROM midterms WHERE (id = %s AND username=%s)"
            cursor.execute(query, (midterm_key,username))
            number_of_midterm, midterm_weight, midterm_score1,midterm_score2,is_important = cursor.fetchone()
            midterm_ = Midterm(number_of_midterm, midterm_weight,is_important,midterm_key)
            midterm_.midterm_score[0]=midterm_score1
            midterm_.midterm_score[1]=midterm_score2
        return midterm_
* Updating midterm at database by using key :
.. code-block:: python

	def update_midterm(self,midterm_key,Midterm,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE midterms SET number_of_midterm = %s, midterm_weight = %s, midterm_score1 = %s, midterm_score2 = %s, is_important = %s WHERE (id = %s AND username=%s)"
            cursor.execute(query, (Midterm.number_of_midterm,Midterm.midterm_weight,Midterm.midterm_score[0],Midterm.midterm_score[1],Midterm.is_important, midterm_key,username))
            connection.commit()
        return midterm_key
COURSE ADDING PAGE
------------------
* Program adds course by function given below:
.. code-block:: python

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
		username=session["username"]
		course_key = db.add_course(course,username)
		return redirect(url_for("courses_page"))
		
COURSES LIST PAGE
----------------
* Can see all courses in your user database by this function:
.. code-block:: python

	def courses_page():
	    username=session["username"]
	    db = Database("postgres://eqxokbcjiseyei:3bc64a91ec58aab73ba937f8652296acf5ab9b2671aba9deb9420dfbe25e5cf6@ec2-46-137-188-105.eu-west-1.compute.amazonaws.com:5432/d1f2968dk53lod")
	    if request.method =="GET":
		courses=db.get_courses(username)
		return render_template("coursespage.html", courses=courses)
	    else:
		form_course_keys=request.form.getlist("course_keys")
		for form_course_key in form_course_keys:
		    db.delete_course(int(form_course_key),username)
		    db.delete_midterm(int(form_course_key),username)
		    db.delete_project(int(form_course_key),username)
		    db.delete_homework(int(form_course_key),username)
		    db.delete_attendance(int(form_course_key),username)
		return redirect(url_for("courses_page"))
		
COURSE EDIT PAGE
----------------
Can edit courses by this function :
.. code-block:: python

	def course_edit_page(course_key):
	    username=session["username"]
	    if request.method == "GET":
		db = current_app.config["db"]
		course =db.get_course(course_key,username)
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
		db.update_course(course_key,course,username)
		return redirect(url_for("course_page",course_key=course_key))

USER PAGE
---------
* Can generate output if a vf condition not satisfied:
.. code-block:: python

	def user_page():
	    username=session["username"]
	    coursesVF=[]
	    db = current_app.config["db"]
	    courses=db.get_courses(username)
	    for course_key,course in courses:
		check=True
		result=0
		midterm=db.get_midterm(course_key,username)
		if midterm.is_important==True:
		    for i in range(midterm.number_of_midterm):
			    result=result+midterm.midterm_weight*midterm.midterm_score[i]/100
		    if(result<30):
			check=False
		result=0
		homework=db.get_homework(course_key,username)
		if homework.is_important==True:
		    for i in range(homework.number_of_homework):
			    result=result+homework.homework_weight*homework.homework_score[i]/100
		    if(result<30):
			check=False
		result=0
		project=db.get_project(course_key,username)
		if project.is_important==True:
		    for i in range(project.number_of_project):
			    result=result+project.project_weight*project.project_score[i]/100
		    if(result<30):
			check=False
		if(check==False):
		    coursesVF.append((course_key, course) )

	    return render_template("userpage.html",courses=coursesVF)
	    
CONDITION ADDING PAGE
---------------------
Adding a vf condition to a course provided by this function:
.. code-block:: python

	def conditionAdding_page(course_key):
	    username=session["username"]
	    db = current_app.config["db"]
	    course=db.get_course(course_key,username)
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
		if attendance=="1":
		    is_important=True
		else:
		    is_important=False

		attendance=Attendance(upper_limit_percent,is_important,course_key)


		db.add_midterm(midterm,username)
		db.add_homework(homework,username)
		db.add_project(project,username)
		db.add_attendance(attendance,username)
		Cond_=Cond(course_key,course_key,course_key,course_key)
		vf_condition_key=db.add_Vfconditions(Cond_,username)
		return redirect(url_for("conditions_page",course_key=course_key))
		
CONDITION EDITING PAGE
----------------------
Conditions can be edited by this function:
.. code-block:: python

	def conditionEditing_page(course_key):
	    username=session["username"]
	    db = current_app.config["db"]
	    course=db.get_course(course_key,username)
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
		if attendance=="1":
		    is_important=True
		else:
		    is_important=False

		attendance=Attendance(upper_limit_percent,is_important,course_key)


		db.update_midterm(course_key,midterm,username)
		db.update_homework(course_key,homework,username)
		db.update_project(course_key,project,username)
		db.update_attendances(course_key,attendance,username)
		Cond_=Cond(course_key,course_key,course_key,course_key)
		db.update_Vfconditions(course_key,Cond_,username)
		return redirect(url_for("course_page",course_key=course_key))

CONDITIONS LIST PAGE
--------------------
Can see vf conditions from this function:
.. code-block:: python

	def conditions_page(course_key):
	    username=session["username"]
	    db = current_app.config["db"]
	    course=db.get_course(course_key,username)
	    midterm=db.get_midterm(course_key,username)
	    homework=db.get_homework(course_key,username)
	    project=db.get_project(course_key,username)
	    attendance=db.get_attendance(course_key,username)


	    midterm_score=[]
	    if request.method == "GET":
		return render_template("VFcond.html",midterm=midterm,homework=homework,project=project,attendance=attendance,course=course)
	    else:
		if midterm.is_important:
		    midterm.midterm_score[0] = request.form["Midterm1"]
		    if midterm.number_of_midterm>1:
			midterm.midterm_score[1] = request.form["Midterm2"]
		    db.update_midterm(course_key,midterm,username)

		if homework.is_important:
		    homework.homework_score[0] = request.form["Homework1"]
		    if homework.number_of_homework>1:
			homework.homework_score[1] = request.form["Homework2"]
			if homework.number_of_homework>2:
			    homework.homework_score[2] = request.form["Homework3"]
			    if homework.number_of_homework>3:
				homework.homework_score[3] = request.form["Homework4"]
		    db.update_homework(course_key,homework,username)

		if project.is_important:
		    project.project_score[0]= request.form["Project1"]
		    if project.number_of_project>1:
			project.project_score[1]= request.form["Project2"]
		    db.update_project(course_key,project,username)

		if attendance.is_important:
		    attendance.attendance[0]=int(request.form["week1"])
		    attendance.attendance[1]=request.form["week2"]
		    attendance.attendance[2]=request.form["week3"]
		    attendance.attendance[3]=request.form["week4"]
		    attendance.attendance[4]=request.form["week5"]
		    attendance.attendance[5]=request.form["week6"]
		    attendance.attendance[6]=request.form["week7"]
		    attendance.attendance[7]=request.form["week8"]
		    attendance.attendance[8]=request.form["week9"]
		    attendance.attendance[9]=request.form["week10"]
		    attendance.attendance[10]=request.form["week11"]
		    attendance.attendance[11]=request.form["week12"]
		    attendance.attendance[12]=request.form["week13"]
		    attendance.attendance[13]=request.form["week14"]
		    db.update_attendances(course_key,attendance,username)

		return render_template("VFcond.html",midterm=midterm,homework=homework,project=project,attendance=attendance,course=course)

