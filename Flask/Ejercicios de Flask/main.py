from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

JSON_FILE = "tasks.json"

VALID_STATUS = ["To Do", "In Progress", "Completed"]


def read_tasks():
    if not os.path.exists(JSON_FILE):
        return []

    with open(JSON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def safe_tasks(tasks):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


# 1. OBTENER TODAS LAS TAREAS (GET)
@app.route("/tasks", methods=["GET"])
def get_tasks():

    tasks = read_tasks()

    status = request.args.get("status")

    if status:
        if status not in VALID_STATUS:
            return jsonify({
                "error": "Invalid status. Valid options are: " + ", ".join(VALID_STATUS)
            }), 400

        tasks = [
            task for task in tasks
            if task["status"] == status
        ]

    return jsonify(tasks), 200


# 2. CREAR UNA TAREA (POST)
@app.route("/tasks", methods=["POST"])
def create_task():

    tasks = read_tasks()

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "You must send a valid JSON object."
        }), 400

    identifier = data.get("identifier")
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")

    
    if identifier is None or identifier == "":
        return jsonify({
            "error": "The identifier is required"
        }), 400

    
    if any(t["identifier"] == identifier for t in tasks):
        return jsonify({
            "error": "A task with that identifier already exists"
        }), 409

    
    if not isinstance(title, str) or not title.strip():
        return jsonify({
            "error": "The title is required"
        }), 400

    
    if not isinstance(description, str) or not description.strip():
        return jsonify({
            "error": "The description is required"
        }), 400

    
    if not isinstance(status, str) or status not in VALID_STATUS:
        return jsonify({
            "error": "Invalid status. Valid options are: " + ", ".join(VALID_STATUS)
        }), 400

    new_task = {
        "identifier": identifier,
        "title": title.strip(),
        "description": description.strip(),
        "status": status
    }

    tasks.append(new_task)
    safe_tasks(tasks)

    return jsonify({
        "message": "Task created successfully",
        "task": new_task
    }), 201


# 3. EDITAR UNA TAREA (PUT)
@app.route("/tasks/<int:identifier>", methods=["PUT"])
def edit_task(identifier):

    tasks = read_tasks()

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "You must send a valid JSON object."
        }), 400

    
    task = next(
        (t for t in tasks if t["identifier"] == identifier),
        None
    )

    if task is None:
        return jsonify({
            "error": "Task not found"
        }), 404

    title = data.get("title")
    description = data.get("description")
    status = data.get("status")

    
    if not isinstance(title, str) or not title.strip():
        return jsonify({
            "error": "The title is required"
        }), 400

    
    if not isinstance(description, str) or not description.strip():
        return jsonify({
            "error": "The description is required"
        }), 400

    
    if not isinstance(status, str) or status not in VALID_STATUS:
        return jsonify({
            "error": "Invalid status"
        }), 400

    
    task["title"] = title.strip()
    task["description"] = description.strip()
    task["status"] = status

    safe_tasks(tasks)

    return jsonify({
        "message": "Task updated successfully",
        "task": task
    }), 200


# 4. ELIMINAR UNA TAREA (DELETE)
@app.route("/tasks/<int:identifier>", methods=["DELETE"])
def delete_task(identifier):

    tasks = read_tasks()

    task = next(
        (t for t in tasks if t["identifier"] == identifier),
        None
    )

    if task is None:
        return jsonify({
            "error": "Task not found"
        }), 404

    tasks.remove(task)
    safe_tasks(tasks)

    return jsonify({
        "message": "Task deleted successfully"
    }), 200



if __name__ == "__main__":
    app.run(host="localhost", debug=True)
