class Homework:
    def __init__(self,number_of_homework,homework_weight,is_important,course_key):
        self.number_of_homework=number_of_homework
        self.homework_weight=homework_weight
        self.homework_score=[0,0,0,0]
        self.is_important=is_important
        self.id=course_key
