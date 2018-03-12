class TodoStorage:
    def __init__(self):
        self._todos = []

    def add_todo(self, name):
        self._todos.append([name, False])

    def complete_todo(self, todo_id):
        self._todos[todo_id][1] = True

    @property
    def todos(self):
        return list(self._todos)
