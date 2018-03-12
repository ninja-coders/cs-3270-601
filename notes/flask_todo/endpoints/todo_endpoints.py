from flask import jsonify, request

def register_endpoints(app, todos):
    @app.route('/')
    def get_all_todos():
        return jsonify(todos.todos)

    @app.route('/todo', methods=['POST'])
    def create_todo():
        new_todo = request.get_json()
        todo_text = new_todo['text']
        todos.add_todo(todo_text)
        return 'OK'        

    @app.route('/todo/<todo_id>', methods=['PUT'])
    def complete_todo(todo_id):
        todos.complete_todo(int(todo_id))
        return 'OK'
