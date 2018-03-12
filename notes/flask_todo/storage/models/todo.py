class Todo:
    def __init__(self, todo, completed):
        self._todo = todo
        self._completed = completed

    @property
    def todo(self):
        return self._todo

    @property
    def completed(self):
        return self._completed
