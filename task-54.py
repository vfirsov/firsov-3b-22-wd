import json


class ToDoList:
    def __init__(self):
        self.todos = ToDoList.load_from_file()

    def add(self, todo):
        self.todos.append(todo)
        ToDoList.save_to_file(self.todos)

    def remove(self, todo):
        self.todos.remove(todo)

    def print_todos(self):
        print(self.todos)

    @staticmethod
    def load_from_file():
        try:
            with open("todos.txt", "r") as todos_from_test:
                return json.load(todos_from_test)
        except OSError:
            return []

    @staticmethod
    def save_to_file(todos):
        try:
            todos_json_object = json.dumps(todos, indent=4)

            with open("todos.txt", "w") as todos_file:
                todos_file.write(todos_json_object)

        except OSError:
            print("Could not write file:")
            exit()


my_home_todos = ToDoList()
# my_home_todos.add('todo 1')
# my_home_todos.add('todo 2')
my_home_todos.print_todos()
