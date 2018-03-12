from flask import Flask

from endpoints.todo_endpoints import register_endpoints
from storage.todo_storage import TodoStorage


if __name__ == '__main__':
    app = Flask(__name__)
    todos = TodoStorage()
    register_endpoints(app, todos)
    app.run()
