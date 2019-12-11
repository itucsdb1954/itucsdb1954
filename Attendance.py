class Attendance:
    def __init__(self,upper_limit_percent,is_important,course_key):
        self.upper_limit_percent=upper_limit_percent
        self.attendance=[1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.is_important=is_important
        self.id=course_key
