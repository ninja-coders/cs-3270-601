import sqlite3

from contextlib import contextmanager


class TodoDB:
    def __init__(self, db_name='./db/todo.db'):
        self._db_name = db_name

    def initialize(self, add_test_data=False):
        if self._todos_table_exists():
            return

        with self.conn() as conn:
            cur = conn.cursor()

            cur.execute('CREATE TABLE todos (id INTEGER PRIMARY KEY AUTOINCREMENT, todo VARCHAR, complete BOOL DEFAULT false)')

            conn.commit()

        if add_test_data:
            self._insert_test_data()

    def _insert_test_data(self):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO todos (todo) VALUES ('learn python');")
            cur.execute("INSERT INTO todos (todo) VALUES ('learn sqlite3');")
            cur.execute("INSERT INTO todos (todo) VALUES ('build app');")
            conn.commit()

    def _todos_table_exists(self):
        with self.cursor() as cur:
            result = list(cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='todos'"))
            if len(result) > 0:
                return True

        return False

    @contextmanager
    def conn(self):
        conn = sqlite3.connect(self._db_name)
        try:
            yield conn
        finally:
            conn.close()

    @contextmanager
    def cursor(self):
        with self.conn() as conn:
            cur = conn.cursor()
            yield cur

    def get_all_todos(self):
        with self.cursor() as cur:
            return list(cur.execute('SELECT * FROM todos'))

    def get_todo(self, todo_id):
        with self.cursor() as cur:
            results = list(cur.execute(f'SELECT * FROM todos WHERE id = {todo_id}'))
            if len(results) > 0:
                return results[0]
            else:
                return []

    def complete_todo(self, todo_id):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute(f"UPDATE todos SET complete = 'true' WHERE id = {todo_id}")
            conn.commit()

    def create_todo(self, todo):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute(f"INSERT INTO todos (todo) VALUES ('{todo}')")
            conn.commit()
