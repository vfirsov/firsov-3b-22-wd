class Book:
    def __init__(self, title, year, author, genre):
        self.title = title
        self.year = year
        self.author = author
        self.genre = genre

    def get_info(self):
        return self.title + ', ' + self.author + ' (' + self.year + '), ' + self.genre


book = Book('Тестовая книга', '2019', 'Джоан Р.', 'Action')

print(book.get_info())

