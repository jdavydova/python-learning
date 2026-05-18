from person import Person

class Professor(Person):

    def __init__(self, first_name, last_name, age, subjects):
        super().__init__(first_name, last_name, age)
        self.subject = subjects

    def print_subjects(self):
        print(self.subject)

    def add_subject(self, subject):
        self.subject.append(subject)

    def remove_subject(self, subject):
        self.subject.remove(subject)
