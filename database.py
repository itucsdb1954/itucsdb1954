import psycopg2 as dbapi2
from course import Course
from VF_Cond import Cond
from Midterm import Midterm
from Homework import Homework
from Project import Project
from Attendance import Attendance
from user import User

class Database:
    def __init__(self,dbfile):
        self.dbfile=dbfile

#users
    def add_user(self,User):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO users (username,full_name,mail,pass) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (User.username, User.name, User.email,User.password))
            connection.commit()
            user_key = cursor.lastrowid
        return user_key
#course
    def add_course(self,course):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO courses (department,course_name, lecturer_name,course_description,VF_condition) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (course.department, course.name, course.lecturerName, course.description,course.VF_conditions))
            connection.commit()
            course_key = cursor.lastrowid
        return course_key

    def delete_course(self,course_key):
         with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM courses WHERE (ID = %s)"
            cursor.execute(query, (course_key,))
            connection.commit()


    def get_course(self,course_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT department, course_name, lecturer_name,course_description, VF_condition FROM courses WHERE (id = %s)"
            cursor.execute(query, (course_key,))
            department, name, lecturerName, description, VF_conditions = cursor.fetchone()
        course_=Course(name,department,description,lecturerName,VF_conditions)
        return course_

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

    def update_course(self,course_key,Course):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE courses SET department = %s, course_name = %s, lecturer_name = %s, course_description = %s, VF_condition = %s WHERE (ID = %s)"
            cursor.execute(query, (Course.department,Course.name,Course.lecturerName,Course.description,Course.VF_conditions, course_key))
            connection.commit()
        return course_key


#Midterm
    def add_midterm(self,Midterm):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO midterms(number_of_midterm, midterm_weight, midterm_score1,midterm_score2,is_important) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (Midterm.number_of_midterm, Midterm.midterm_weight, Midterm.midterm_score[0],Midterm.midterm_score[1], Midterm.is_important))
            connection.commit()
            midterm_key = cursor.lastrowid
        return midterm_key

    def delete_midterm(self,midterm_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM midterms WHERE (ID = %s)"
            cursor.execute(query, (midterm_key,))
            connection.commit()

    def get_midterm(self,midterm_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT number_of_midterm, midterm_weight, midterm_score1,midterm_score2,is_important FROM midterms WHERE (id = %s)"
            cursor.execute(query, (midterm_key,))
            number_of_midterm, midterm_weight, midterm_score1,midterm_score2,is_important = cursor.fetchone()
            midterm_ = Midterm(number_of_midterm, midterm_weight,is_important,midterm_key)
            midterm_.midterm_score[0]=midterm_score1
            midterm_.midterm_score[1]=midterm_score2
        return midterm_
    """def get_midterms(self):
        midterms = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT id,number_of_midterm, midterm_weight, midterm_score1,midterm_score2,is_important FROM midterms ORDER BY id"
            cursor.execute(query)
            for midterm_key, number_of_midterm, midterm_weight, midterm_score1,midterm_score2,is_important in cursor:
                midterms.append((midterm_key, Midterm(number_of_midterm, midterm_weight,is_important)))
                midterms[midterm_key].midterm_score[0]=midterm_score1
        		midterms[midterm_key].midterm_score[1]=midterm_score2
        return midterms
	"""
    def update_midterm(self,midterm_key,Midterm):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE midterms SET number_of_midterm = %s, midterm_weight = %s, midterm_score1 = %s, midterm_score2 = %s, is_important = %s WHERE (id = %s)"
            cursor.execute(query, (Midterm.number_of_midterm,Midterm.midterm_weight,Midterm.midterm_score[0],Midterm.midterm_score[1],Midterm.is_important, midterm_key))
            connection.commit()
        return midterm_key

#Homeworks
    def add_homework(self,Homework):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO homeworks(number_of_homework, homework_weight, homework_score1,homework_score2,homework_score3,homework_score4,is_important) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (Homework.number_of_homework, Homework.homework_weight, Homework.homework_score[0], Homework.homework_score[1], Homework.homework_score[2], Homework.homework_score[3], Homework.is_important))
            connection.commit()
            homework_key = cursor.lastrowid
        return homework_key

    def delete_homework(self,homework_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM homeworks WHERE (ID = %s)"
            cursor.execute(query, (homework_key,))
            connection.commit()

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
    """ def get_homeworks(self):
        homeworks = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT id,number_of_homework, homework_weight, homework_score1,homework_score2,homework_score3,homework_score4,is_important FROM homeworks ORDER BY ID"
            cursor.execute(query)
            for homework_key,number_of_homework, homework_weight, homework_score1,homework_score2,homework_score3,homework_score4,is_important in cursor:
                homeworks.append((homework_key, Homework(number_of_homework, homework_weight,is_important)))
                homeworks[homework_key].homework_score[0]= homework_score1
        		homeworks[homework_key].homework_score[1]= homework_score2
        		homeworks[homework_key].homework_score[2]= homework_score3
        		homeworks[homework_key].homework_score[3]= homework_score4
        return homeworks
    """
    def update_homework(self,homework_key,homework):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE homeworks SET number_of_homework = %s, homework_weight = %s, homework_score1 = %s, homework_score2 = %s, homework_score3 = %s, homework_score4 = %s, is_important = %s WHERE (ID = %s)"
            cursor.execute(query, (homework.number_of_homework,homework.homework_weight,homework.homework_score[0],homework.homework_score[1],homework.homework_score[2],homework.homework_score[3],homework.is_important, homework_key))
            connection.commit()
        return homework_key
#project

    def add_project(self,project):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO projects(number_of_project,project_weight,project_score1,project_score2,is_important) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (project.number_of_project, project.project_weight, project.project_score[0], project.project_score[1], project.is_important))
            connection.commit()
            project_key = cursor.lastrowid
        return project_key

    def delete_project(self,project_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM projects WHERE (ID = %s)"
            cursor.execute(query, (project_key,))
            connection.commit()

    def get_project(self,project_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT number_of_project,project_weight,project_score1,project_score2,is_important FROM projects WHERE (id = %s)"
            cursor.execute(query, (project_key,))
            number_of_project,project_weight,project_score1,project_score2,is_important = cursor.fetchone()
            project_ = Project(number_of_project,project_weight,is_important,project_key)
            project_.project_score[0]=project_score1
            project_.project_score[1]=project_score2
        return project_
    """def get_projects(self):
        projects = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT id,number_of_project,project_weight,project_score1,project_score2,is_important FROM projects ORDER BY ID"
            cursor.execute(query)
            for project_key,number_of_homework, homework_weight, homework_score1,homework_score2,homework_score3,homework_score4,is_important in cursor:
                projects.append((project_key, Project(number_of_project,project_weight,project_score1,project_score2,is_important)))
        return projects
	"""
    def update_project(self,project_key,Project):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE projects SET number_of_project = %s, project_weight = %s, project_score1 = %s, project_score2 = %s,is_important = %s WHERE (ID = %s)"
            cursor.execute(query, (Project.number_of_project,Project.project_weight,Project.project_score[0],Project.project_score[1],Project.is_important, project_key))
            connection.commit()
        return project_key


#attendance
    def add_attendance(self,Attendance):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO attendances(upper_limit_percent,attendance_hour1,attendance_hour2,attendance_hour3,attendance_hour4,attendance_hour5,attendance_hour6,attendance_hour7,attendance_hour8,attendance_hour9,attendance_hour10,attendance_hour11,attendance_hour12,attendance_hour13,attendance_hour14,is_important) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (Attendance.upper_limit_percent, Attendance.attendance[0], Attendance.attendance[1], Attendance.attendance[2], Attendance.attendance[3], Attendance.attendance[4], Attendance.attendance[5], Attendance.attendance[6], Attendance.attendance[7], Attendance.attendance[8], Attendance.attendance[9], Attendance.attendance[10], Attendance.attendance[11], Attendance.attendance[12], Attendance.attendance[13],Attendance.is_important))
            connection.commit()
            attendance_key = cursor.lastrowid
        return attendance_key

    def delete_attendance(self,attendance_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM attendances WHERE (ID = %s)"
            cursor.execute(query, (attendance_key,))
            connection.commit()

    def get_attendance(self,attendance_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT upper_limit_percent,attendance_hour1,attendance_hour2,attendance_hour3,attendance_hour4,attendance_hour5,attendance_hour6,attendance_hour7,attendance_hour8,attendance_hour9,attendance_hour10,attendance_hour11,attendance_hour12,attendance_hour13,attendance_hour14,is_important FROM attendances WHERE (id = %s)"
            cursor.execute(query, (attendance_key,))
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

    """def get_attendances(self):
        attendances = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT id,upper_limit_percent,attendance_hour1,attendance_hour2,attendance_hour3,attendance_hour4,attendance_hour5,attendance_hour6,attendance_hour7,attendance_hour8,attendance_hour9,attendance_hour10,attendance_hour11,attendance_hour12,attendance_hour13,attendance_hour14,is_important FROM attendances ORDER BY ID"
            cursor.execute(query)
            for attendances_key,upper_limit_percent,attendance_hour1,attendance_hour2,attendance_hour3,attendance_hour4,attendance_hour5,attendance_hour6,attendance_hour7,attendance_hour8,attendance_hour9,attendance_hour10,attendance_hour11,attendance_hour12,attendance_hour13,attendance_hour14,is_important in cursor:
                attendances.append((attendances_key, Project(upper_limit_percent,attendance_hour1,attendance_hour2,attendance_hour3,attendance_hour4,attendance_hour5,attendance_hour6,attendance_hour7,attendance_hour8,attendance_hour9,attendance_hour10,attendance_hour11,attendance_hour12,attendance_hour13,attendance_hour14,is_important)))
        return attendances
	"""
    def update_attendances(self,attendance_key,Attendance):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE attendances SET upper_limit_percent = %s, attendance_hour1 = %s, attendance_hour2 = %s,attendance_hour3 = %s,attendance_hour4 = %s,attendance_hour5 = %s,attendance_hour6 = %s,attendance_hour7 = %s,attendance_hour8 = %s,attendance_hour9 = %s,attendance_hour10 = %s,attendance_hour11 = %s,attendance_hour12 = %s,attendance_hour13 = %s,attendance_hour14 = %s,is_important = %s WHERE (ID = %s)"
            cursor.execute(query, (Attendance.upper_limit_percent,Attendance.attendance[0],Attendance.attendance[1],Attendance.attendance[2],Attendance.attendance[3],Attendance.attendance[4],Attendance.attendance[5],Attendance.attendance[6],Attendance.attendance[7],Attendance.attendance[8],Attendance.attendance[9],Attendance.attendance[10],Attendance.attendance[11],Attendance.attendance[12],Attendance.attendance[13],Attendance.is_important, attendance_key))
            connection.commit()
        return attendance_key

#VF_condition

    def add_Vfconditions(self,attendance_key,midterm_key,homework_key,project_key):
        if attendance_key>0 and midterm_key>0 and homework_key>0 and project_key>0:
            with dbapi2.connect(self.dbfile) as connection:
                cursor = connection.cursor()
                query = "INSERT INTO vf_conditions(attendance,midterm,homework,project) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (attendance_key,midterm_key,homework_key,project_key))
                connection.commit()
                vfconditions_key = cursor.lastrowid
            return vfconditions_key

    def delete_Vfconditions(self,vfconditions_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM vf_conditions WHERE (ID = %s)"
            cursor.execute(query, (vfconditions_key))
            connection.commit()

    def get_Vfconditions(self,vfconditions_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT attendance,midterm,homework,project FROM vf_conditions WHERE (id = %s)"
            cursor.execute(query, (vfconditions_key))
            attendance,midterm,homework,project = cursor.fetchone()
            Cond_ = Cond(attendance,midterm,homework,projec)
        return Cond_

    def update_Vfconditions(self,vfconditions_key,Cond):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE vf_conditions SET attendance = %s, midterm = %s,homework = %s,project = %s, WHERE (ID = %s)"
            cursor.execute(query, (Cond.attendance,Cond.midterm,Cond.homework,Cond.project,vfconditions_key))
            connection.commit()
        return vfconditions_key
