class TodoStorage:
    def __init__(self):
        self._todos = []

    def add_todo(self, todo):
        self._todos.append({'text': todo, 'complete': False})

    def complete_todo(self, todo_id):
        self._todos[todo_id]['complete'] = True

    @property
    def todos(self):
        return self._todos 
