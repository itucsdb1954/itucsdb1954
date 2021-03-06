Parts Implemented by AHMET ÖZDEMİR
================================

users Table
-----------
* "users Table" holds the information of users such as username,password,mail(content of users table below).We get the 
information from register page and save it to database.We are using this table to access different combinations of courses.

.. code-block:: python

	INIT_STATEMENTS = [
		"""
		CREATE TABLE IF NOT EXISTS users(
		id SERIAL PRIMARY KEY,
		username VARCHAR(50) NOT NULL UNIQUE,
		full_name VARCHAR(100) NOT NULL ,
		mail VARCHAR(100) ,
		pass VARCHAR(50) NOT NULL
		);
		"""
		]
	
* There is a USER class to use in database operations

.. code-block:: python

	class User(UserMixin):
		def __init__(self, username,password):
			self.username = username
			self.name=""
			self.email=""
			self.password = password
			self.active = True
			self.is_admin = False

		def get_id(self):
			return self.username

		@property
		def is_active(self):
			return self.active


	def get_user(user_id):
		password = current_app.config["PASSWORDS"].get(user_id)
		user = User(user_id, password) if password else None
		if user is not None:
			user.is_admin = user.username in current_app.config["ADMIN_USERS"]
		return user	
	
* There is functions to access and manipulate users table at the database.For example adding a user object 
to database is :


.. code-block:: python

	def add_user(self,User):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO users (username,full_name,mail,pass) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (User.username, User.name, User.email,User.password))
            connection.commit()
            user_key = cursor.lastrowid
        return user_key

* Deleting user from database:

.. code-block:: python

    def delete_user(self,user_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM users WHERE (ID = %s)"
            cursor.execute(query,user_key)
            connection.commit()

* Getting information of a user from "username" attribute:

.. code-block:: python

    def get_user(self,Username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT username,full_name,mail,pass FROM users WHERE (username = %s)"
            connection.commit()
            cursor.execute(query,[Username])
            username,name,email,password=cursor.fetchone()
            user=User(username,password)
            user.email=email
            user.name=name
        return user

attendances Table
-----------------
* "attendances Table" holds information of attendances in a course .It's "id" column references to "vf_conditions table".Content of table 
is below:

.. code-block:: python

	INIT_STATEMENTS = [
	"""
	CREATE TABLE IF NOT EXISTS attendances(
		id SERIAL PRIMARY KEY,
		upper_limit_percent INTEGER CHECK(upper_limit_percent<100 AND upper_limit_percent>=0),
		attendance_hour1 INTEGER DEFAULT(0),
		attendance_hour2 INTEGER DEFAULT(0),
		attendance_hour3 INTEGER DEFAULT(0),
		attendance_hour4 INTEGER DEFAULT(0),
		attendance_hour5 INTEGER DEFAULT(0),
		attendance_hour6 INTEGER DEFAULT(0),
		attendance_hour7 INTEGER DEFAULT(0),
		attendance_hour8 INTEGER DEFAULT(0),
		attendance_hour9 INTEGER DEFAULT(0),
		attendance_hour10 INTEGER DEFAULT(0),
		attendance_hour11 INTEGER DEFAULT(0),
		attendance_hour12 INTEGER DEFAULT(0),
		attendance_hour13 INTEGER DEFAULT(0),
		attendance_hour14 INTEGER DEFAULT(0),
		is_important BOOLEAN,
		username VARCHAR(50) NOT NULL
	);
	"""
* There is a "Attendance" class to use in database operations :

.. code-block:: python

	class Attendance:
    def __init__(self,upper_limit_percent,is_important,course_key):
        self.upper_limit_percent=upper_limit_percent
        self.attendance=[1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.is_important=is_important
        self.id=course_key
		

* There is functions to access and manipulate "attendances" table at the database.For example adding a Attendance object 
to database is :

.. code-block:: python

	def add_attendance(self,Attendance,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO attendances(upper_limit_percent,attendance_hour1,attendance_hour2,attendance_hour3,attendance_hour4,attendance_hour5,attendance_hour6,attendance_hour7,attendance_hour8,attendance_hour9,attendance_hour10,attendance_hour11,attendance_hour12,attendance_hour13,attendance_hour14,is_important,username) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s)"
            cursor.execute(query, (Attendance.upper_limit_percent, Attendance.attendance[0], Attendance.attendance[1], Attendance.attendance[2], Attendance.attendance[3], Attendance.attendance[4], Attendance.attendance[5], Attendance.attendance[6], Attendance.attendance[7], Attendance.attendance[8], Attendance.attendance[9], Attendance.attendance[10], Attendance.attendance[11], Attendance.attendance[12], Attendance.attendance[13],Attendance.is_important,username))
            connection.commit()
            attendance_key = cursor.lastrowid
        return attendance_key

* Deleting attendance from database:
.. code-block:: python

    def delete_attendance(self,attendance_key,usernam):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM attendances WHERE (ID = %s AND username=%s)"
            cursor.execute(query, (attendance_key,username))
            connection.commit()
			
* Getting attendance by using key:
.. code-block:: python

    def get_attendance(self,attendance_key,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT upper_limit_percent,attendance_hour1,attendance_hour2,attendance_hour3,attendance_hour4,attendance_hour5,attendance_hour6,attendance_hour7,attendance_hour8,attendance_hour9,attendance_hour10,attendance_hour11,attendance_hour12,attendance_hour13,attendance_hour14,is_important FROM attendances WHERE (id = %s AND username=%s)"
            cursor.execute(query, (attendance_key,username))
            upper_limit_percent,attendance_hour1,attendance_hour2,attendance_hour3,attendance_hour4,attendance_hour5,attendance_hour6,attendance_hour7,attendance_hour8,attendance_hour9,attendance_hour10,attendance_hour11,attendance_hour12,attendance_hour13,attendance_hour14,is_important = cursor.fetchone()
            attendance_ = Attendance(upper_limit_percent,is_important,attendance_key)
            attendance_.attendance[0]=attendance_hour1
            attendance_.attendance[1]=attendance_hour2
            attendance_.attendance[2]=attendance_hour3
            attendance_.attendance[3]=attendance_hour4
            attendance_.attendance[4]=attendance_hour5
            attendance_.attendance[5]=attendance_hour6
            attendance_.attendance[6]=attendance_hour7
            attendance_.attendance[7]=attendance_hour8
            attendance_.attendance[8]=attendance_hour9
            attendance_.attendance[9]=attendance_hour10
            attendance_.attendance[10]=attendance_hour11
            attendance_.attendance[11]=attendance_hour12
            attendance_.attendance[12]=attendance_hour13
            attendance_.attendance[13]=attendance_hour14
        return attendance_

* Updating attendance at database by using key :
.. code-block:: python
    
     def update_attendances(self,attendance_key,Attendance,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE attendances SET upper_limit_percent = %s, attendance_hour1 = %s, attendance_hour2 = %s,attendance_hour3 = %s,attendance_hour4 = %s,attendance_hour5 = %s,attendance_hour6 = %s,attendance_hour7 = %s,attendance_hour8 = %s,attendance_hour9 = %s,attendance_hour10 = %s,attendance_hour11 = %s,attendance_hour12 = %s,attendance_hour13 = %s,attendance_hour14 = %s,is_important = %s WHERE (ID = %s AND username=%s)"
            cursor.execute(query, (Attendance.upper_limit_percent,Attendance.attendance[0],Attendance.attendance[1],Attendance.attendance[2],Attendance.attendance[3],Attendance.attendance[4],Attendance.attendance[5],Attendance.attendance[6],Attendance.attendance[7],Attendance.attendance[8],Attendance.attendance[9],Attendance.attendance[10],Attendance.attendance[11],Attendance.attendance[12],Attendance.attendance[13],Attendance.is_important, attendance_key,username))
            connection.commit()
        return attendance_key

projects Table
--------------
* "projects" Table holds the project notes in the database.It's id references "vf_conditions" table.Content of table is below:
.. code-block:: python

	INIT_STATEMENTS = [
		"""
	CREATE TABLE IF NOT EXISTS projects(
	id SERIAL PRIMARY KEY,
    number_of_project INTEGER ,
    project_weight INTEGER CHECK(project_weight<100 AND project_weight>=0)  ,
    project_score1 INTEGER DEFAULT(0),
    project_score2 INTEGER DEFAULT(0),
    is_important BOOLEAN,
    username VARCHAR(50) NOT NULL
	);
	"""
	]

		
* There is a "Project" class to use at database operations:
.. code-block:: python

	class Project:
		def __init__(self,number_of_project,project_weight,is_important,course_key):
			self.number_of_project=number_of_project
			self.project_weight=project_weight
			self.project_score=[0,0]
			self.is_important=is_important
			self.id=course_key

* There is functions to access and manipulate "projects" table at the database.For example adding a Project object 
to database is :
.. code-block:: python

	def add_project(self,project,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO projects(number_of_project,project_weight,project_score1,project_score2,is_important,username) VALUES (%s, %s, %s, %s, %s,%s)"
            cursor.execute(query, (project.number_of_project, project.project_weight, project.project_score[0], project.project_score[1], project.is_important,username))
            connection.commit()
            project_key = cursor.lastrowid
        return project_key

* Deleting project from database by using key:
.. code-block:: python

	def delete_project(self,project_key,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM projects WHERE (ID = %s AND username=%s)"
            cursor.execute(query, (project_key,username))
            connection.commit()
			
* Getting project from database by using key:
.. code-block:: python

	def get_project(self,project_key,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT number_of_project,project_weight,project_score1,project_score2,is_important FROM projects WHERE (id = %s AND username=%s)"
            cursor.execute(query, (project_key,username))
            number_of_project,project_weight,project_score1,project_score2,is_important = cursor.fetchone()
            project_ = Project(number_of_project,project_weight,is_important,project_key)
            project_.project_score[0]=project_score1
            project_.project_score[1]=project_score2
        return project_
	
* Updating project at database by using key :
.. code-block:: python
	
	 def update_project(self,project_key,Project,username):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE projects SET number_of_project = %s, project_weight = %s, project_score1 = %s, project_score2 = %s,is_important = %s WHERE (ID = %s AND username=%s)"
            cursor.execute(query, (Project.number_of_project,Project.project_weight,Project.project_score[0],Project.project_score[1],Project.is_important, project_key,username))
            connection.commit()
        return project_key


REGISTER PAGE
-------------
* Program store the user's login data  into database by using "users" table.Signing up done by a function given below:
.. code-block:: python

	def register_page():
    		db = current_app.config["db"]
    		form = RegistrationForm()
    		if request.method=="GET":
        		return render_template("register.html")
    		else:
        		name=request.form["Name"]
			Username=request.form["Username"]
			email=request.form["Email Address"]
			#password=sha256_crypt.encrypt((str(request.form["Password"])))
			password=request.form["Password"]
			user=User(Username,password)
			user.email=email
			user.name=name
			db.add_user(user)
  		return redirect(url_for("home_page"))
	
