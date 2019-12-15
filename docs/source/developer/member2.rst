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
		vf_condition INTEGER
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

	def add_course(self,course):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO courses (department,course_name, lecturer_name,course_description,VF_condition) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (course.department, course.name, course.lecturerName, course.description,course.VF_conditions))
            connection.commit()
            course_key = cursor.lastrowid
        return course_key
* Deleting course from database by using key:
.. code-block:: python

	 def delete_course(self,course_key):
         with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM courses WHERE (ID = %s)"
            cursor.execute(query, (course_key,))
            connection.commit()
* Getting a course from database by using key:
.. code-block:: python

	 def get_course(self,course_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT department, course_name, lecturer_name,course_description, VF_condition FROM courses WHERE (id = %s)"
            cursor.execute(query, (course_key,))
            department, name, lecturerName, description, VF_conditions = cursor.fetchone()
        course_=Course(name,department,description,lecturerName,VF_conditions)
        return course_
* Getting all courses from database:
.. code-block:: python

	def get_courses(self):
        courses = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT id,department,course_name,lecturer_name,course_description,VF_condition FROM courses ORDER BY ID"
            cursor.execute(query)
            for course_key, department,name, lecturerName, description, VF_conditions in cursor:
                course=Course(name, department,description,lecturerName,VF_conditions)
                courses.append((course_key, course) )
        return courses
* Updating course at database by using key :
.. code-block:: python

	def update_course(self,course_key,Course):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE courses SET department = %s, course_name = %s, lecturer_name = %s, course_description = %s, VF_condition = %s WHERE (ID = %s)"
            cursor.execute(query, (Course.department,Course.name,Course.lecturerName,Course.description,Course.VF_conditions, course_key))
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
			is_important BOOLEAN
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

		def add_homework(self,Homework):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO homeworks(number_of_homework, homework_weight, homework_score1,homework_score2,homework_score3,homework_score4,is_important) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (Homework.number_of_homework, Homework.homework_weight, Homework.homework_score[0], Homework.homework_score[1], Homework.homework_score[2], Homework.homework_score[3], Homework.is_important))
            connection.commit()
            homework_key = cursor.lastrowid
        return homework_key

* Deleting homework from database by using key:
.. code-block:: python

	def delete_homework(self,homework_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM homeworks WHERE (ID = %s)"
            cursor.execute(query, (homework_key,))
            connection.commit()
			
* Getting a homework from database by using key:
.. code-block:: python

	def get_homework(self,homework_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT number_of_homework, homework_weight, homework_score1,homework_score2,homework_score3,homework_score4,is_important FROM homeworks WHERE (id = %s)"
            cursor.execute(query, (homework_key,))
            number_of_homework, homework_weight, homework_score1,homework_score2,homework_score3,homework_score4,is_important = cursor.fetchone()
            homework_ = Homework(number_of_homework, homework_weight,is_important,homework_key)
            homework_.homework_score[0]= homework_score1
            homework_.homework_score[1]= homework_score2
            homework_.homework_score[2]= homework_score3
            homework_.homework_score[3]= homework_score4
        return homework_
		
* Updating course at database by using key :
.. code-block:: python

	def update_homework(self,homework_key,homework):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE homeworks SET number_of_homework = %s, homework_weight = %s, homework_score1 = %s, homework_score2 = %s, homework_score3 = %s, homework_score4 = %s, is_important = %s WHERE (ID = %s)"
            cursor.execute(query, (homework.number_of_homework,homework.homework_weight,homework.homework_score[0],homework.homework_score[1],homework.homework_score[2],homework.homework_score[3],homework.is_important, homework_key))
            connection.commit()
        return homework_key
	
