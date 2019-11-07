from course import Course

class Database:
    def __init__(self):
        self.courses = {}
        self._last_course_key = 0

    def add_course(self,course):
        self._last_course_key += 1
        self.courses[self._last_course_key]= course
        return self._last_course_key

    def delete_course(self,course_key):
        if course_key in self.courses:
            del self.courses[course_key]

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
