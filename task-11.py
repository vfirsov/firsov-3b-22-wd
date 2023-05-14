class Dog:
    def __init__(self, dog_name, breed, age):
        self.dog_name = dog_name
        self.breed = breed
        self.age = age

    def get_info(self):
        return self.dog_name + ' ' + self.breed + ' ' + self.age


first_rectangle = Dog('King', 'Московская сторожевая', '10')

print(first_rectangle.get_info())
