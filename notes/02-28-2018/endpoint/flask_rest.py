from flask import jsonify, request


def create_endpoints(app, todos):
    @app.route('/')
    def index_route():
        return jsonify(todos.todos)

    @app.route('/todo/<todo_id>', methods=['PUT'])
    def complete_task(todo_id):
        print(todo_id)
        todos.complete_todo(todo_id)
        return jsonify('OK')

    @app.route('/todo', methods=['POST'])
    def create_task():
        new_todo = request.get_json()
        todos.add_todo(new_todo['text'])
        return jsonify('OK')
