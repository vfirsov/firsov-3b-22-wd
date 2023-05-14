class Auto:
    def __init__(self, mark, model, year, price):
        self.mark = mark
        self.model = model
        self.year = year
        self.price = price

    def get_info(self):
        return self.mark + ' - ' + self.model + ', ' + str(self.year) + ', ' + str(self.price)


auto = Auto('Хунци', 'H9', 2023, 14000000)

print(auto.get_info())
