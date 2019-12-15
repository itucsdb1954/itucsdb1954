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
