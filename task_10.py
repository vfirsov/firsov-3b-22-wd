class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_info(self):
        return self.name + ' ' + self.surname

