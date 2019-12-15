Parts Implemented by AHMET ÖZDEMİR
================================

users Table
-----------
"users Table" holds the information of users such as username,password,mail(content of users table below).We get the 
information from register page and save it to database.We are using this table to access different combinations of courses.

.. code-block:: sql
	"""CREATE TABLE IF NOT EXISTS users(
		id SERIAL PRIMARY KEY,
		username VARCHAR(50) NOT NULL UNIQUE,
		full_name VARCHAR(100) NOT NULL ,
		mail VARCHAR(100) ,
		pass VARCHAR(50) NOT NULL
	);"""
There is a USER class to use in database operations
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
		
There is functions to access and manipulate users table at the database.For example adding a user object 
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

Deleting user from database:
.. code-block:: python
    def delete_user(self,user_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM users WHERE (ID = %s)"
            cursor.execute(query,user_key)
            connection.commit()

Getting information of a user from "username" attribute:
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
