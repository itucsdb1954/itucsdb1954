from course import Course
from VF_Cond import Cond
from Midterm import Midterm
from Homework import Homework
from Project import Project
from Attendance import Attendance

class Database:
    def __init__(self):
        self.courses = {}
        self._last_course_key = 0
        self._last_VF_key=0
        self._last_Project_key=0
        self._last_Midterm_key=0
        self._last_Homework_key=0
        self._last_Attendance_key=0
        self.Midterm={ }
        self.Homework={ }
        self.Project={ }
        self.Attendance={ }

    def add_course(self,course):
        self._last_course_key += 1
        self.courses[self._last_course_key]= course
        return self._last_course_key

    def delete_course(self,course_key):
        if course_key in self.courses:
            del self.courses[course_key]
            self._last_course_key=self._last_course_key-1


    def get_course(self,course_key):
        course = self.courses.get(course_key)
        if course is None:
            return None
        course_ = Course(course.name,course.department,course.description,course.lecturerName,course.VF_conditions)
        return course_

    def get_courses(self):
        courses = []
        for course_key,course in self.courses.items():
            course_=Course(course.name,course.department,course.description,course.lecturerName,course.VF_conditions)
            courses.append((course_key,course_))
        return courses

    def update_course(self,course_key,course):
        self.courses[course_key]=course
        return




    def add_Midterm(self,Midterm):
        self._last_Midterm_key+=1
        self.Midterm[self._last_Midterm_key]=Midterm
        return self._last_Midterm_key

    def get_midterm(self,course_key):
        midterm = self.Midterm.get(course_key)
        if midterm is None:
            return None
        midterm_ = Midterm(midterm.number_of_midterm,midterm.midterm_weight,midterm.is_important,course_key)
        return midterm_
    def add_midterm_score(self,midterm_score,course_key):
        self.Midterm[course_key].midterm_score[0]=midterm_score[0]
        self.Midterm[course_key].midterm_score[1]=midterm_score[1]
        return


    def add_Homework(self,Homework):
        self._last_Homework_key+=1
        self.Homework[self._last_Homework_key]=Homework
        return self._last_Homework_key
    def get_homework(self,course_key):
        homework = self.Homework.get(course_key)
        if homework is None:
            return None
        homework_ = Homework(homework.number_of_homework,homework.homework_weight,homework.is_important,course_key)
        return homework_



    def add_Project(self,Project):
        self._last_Project_key+=1
        self.Project[self._last_Project_key]=Project
        return self._last_Project_key

    def get_project(self,course_key):
        project = self.Project.get(course_key)
        if project is None:
            return None
        project_ = Project(project.number_of_project,project.project_weight,project.is_important,course_key)
        return project_



    def add_Attendance(self,Attendance):
        self._last_Attendance_key+=1
        self.Attendance[self._last_Attendance_key]=Attendance
        return self._last_Attendance_key

    def get_attendance(self,course_key):
        attendance = self.Attendance.get(course_key)
        if attendance is None:
            return None
        attendance_ = Attendance(attendance.upper_limit_percent,attendance.is_important,course_key)
        return attendance_
