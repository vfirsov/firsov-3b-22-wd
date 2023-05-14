from task_10 import Person


class Student(Person):
    def __init__(self, name, surname, age, specialty):
        Person.__init__(self, name, surname)
        self.age = age
        self.specialty = specialty

    def get_info(self):
        return self.name + ' - ' + self.surname + ', ' + str(self.age) + ', ' + self.specialty


student_first = Student('Victor', 'Firsov', 33, 'Frontend Developer')

print(student_first.get_info())
