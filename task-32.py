class SchoolBoy:
    def __init__(self, name, class_name):
        self.name = name
        self.className = class_name

    def teach(self):
        print('школьник учится')


mike = SchoolBoy('Mike', '10')
mike.teach()
