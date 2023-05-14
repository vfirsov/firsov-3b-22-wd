class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_info(self):
        return 'Кот по имени: ' + self.name + ', возраст: ' + str(self.age) + ', цвет: ' + self.color


auto = Cat('Бонифаций', '3', 'Белый')

print(auto.get_info())

