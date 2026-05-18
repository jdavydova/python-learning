class Lecture:
    def __init__(self, name, max_numb_of_students, duration, professors):
        self.name = name
        self.max_numb_of_students = max_numb_of_students
        self.duration = duration
        self.professors = professors


    def name_and_duration(self):
        print(f"{self.name}, {self.duration}")

    def add_professor(self, professor):
        self.professors.append(professor)

    
