#!/usr/bin/python3
"""The module contains the entry point of the web sevice"""


from flask import Flask, jsonify, url_for
from flask import abort, make_response
from flask import request
from flask_httpauth import HTTPBasicAuth
import unicodedata


app = Flask(__name__)
auth = HTTPBasicAuth()

tasks = [
    {
    "id": 1,
    "title": u"Buy groceries",
    "description": u"Milk, Cheese, Pizza, Fruit, Tylenol",
    "done": False
    },
    {
    "id": 2,
    "title": u"Learn Python",
    "description": u"Need to find a good python tutorial on the web",
    "done": False
    }
]

def make_public_task(task):
    """Create a new task with a new field uri"""
    new_task = {}
    for field in task:
        if field == 'id':
            new_task["uri"] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


@app.errorhandler(404)
def not_found(error):
    """Return JSON format of 404 error message"""
    return make_response(jsonify({'error': "Not found"}), 404)


@auth.get_password
def get_password(username):
    if username == "Jovial":
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({"error": "unauthorized access "}), 403)

@app.route("/todo/api/v1.0/tasks", methods=["GET"])
@auth.login_required
def get_tasks():
    """Returns data of tasks"""
    return jsonify({"tasks": [make_public_task(task) for task in tasks]})


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """Returns data of a single task"""
    task = [task for task in tasks if task["id"] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': make_public_task(task[0])})


@app.route("/todo/api/v1.0/tasks", methods=["POST"])
def create_task():
    """Create new task"""
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        "id": tasks[-1]['id'] + 1,
        "title": request.json['title'],
        "description": request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task':task}), 201


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Update an existing task"""
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicodedata:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicodedata:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get("title", task[0]['title'])
    task[0]['description'] = request.json.get("description", task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task"""
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True)