from flask import Flask, jsonify, request

from todo_db import TodoDB

db = TodoDB()
db.initialize(add_test_data=True)

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(db.get_all_todos())


@app.route('/<todo_id>')
def get_todo(todo_id):
    return jsonify(db.get_todo(todo_id))


@app.route('/<todo_id>', methods=['PUT'])
def complete_todo(todo_id):
    db.complete_todo(todo_id)
    return 'OK'


@app.route('/', methods=['POST'])
def create_todo():
    print(request.data)   # This gives you the raw body
    new_todo = request.get_json()
    db.create_todo(new_todo['todo'])
    return jsonify(db.get_all_todos())


if __name__ == '__main__':
    app.run()
