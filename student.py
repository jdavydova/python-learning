from person import Person

class Student(Person):

    def __init__(self, first_name, last_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures

    def print_lectures(self):
        print(self.lectures)

    def add_lecture(self, new_lecture):
        self.lectures.append(new_lecture)

    def remove_lecture(self, new_lecture):
        self.lectures.remove(self.lectures[new_lecture])