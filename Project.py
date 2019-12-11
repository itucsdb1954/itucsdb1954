class Project:
    def __init__(self,number_of_project,project_weight,is_important,course_key):
        self.number_of_project=number_of_project
        self.project_weight=project_weight
        self.project_score=[0,0]
        self.is_important=is_important
        self.id=course_key
