from task_10 import Person


class Student(Person):
    def __init__(self, name, surname, course, scores):
        Person.__init__(self, name, surname)
        self.course = course
        self.scores = scores

    def grade_average(self):
        return sum(self.scores) / len(self.scores)


student_first = Student('Victor', 'Firsov', 1, [5, 5, 5, 5, 5, 5, 4])

print(student_first.grade_average())
print(student_first.name)
