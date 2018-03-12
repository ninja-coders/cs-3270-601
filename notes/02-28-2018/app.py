from flask import Flask

from storage import TodoStorage
from endpoint import create_endpoints

if __name__ == '__main__':
    app = Flask(__name__)
    todos = TodoStorage()
    create_endpoints(app, todos)
    app.run()

