class GeometricFigure:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    def get_info(self):
        print(f'Площадь: {self.area}, периметр {self.perimeter}')


rectangle = GeometricFigure('100', '40')

rectangle.get_info()


