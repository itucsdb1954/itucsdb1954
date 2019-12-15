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
* There is functions to access and manipulate "courses" table at the database.For example adding a Course object 
to database is :
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
