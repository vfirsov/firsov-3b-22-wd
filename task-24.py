class Employ:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def presentation(self):
        print(f'name: {self.name}, age: {self.age}, salary: {self.salary}')


junior = Employ('Victor', '33', '100500$')
junior.presentation()

