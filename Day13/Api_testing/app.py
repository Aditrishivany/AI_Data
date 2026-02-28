from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
current_id = 1


# GET all tasks
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


# GET single task
@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200


# POST create task
@app.route("/api/tasks", methods=["POST"])
def create_task():
    global current_id

    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    # Title validation
    if "title" not in data or not isinstance(data["title"], str):
        return jsonify({"error": "Title is required"}), 400

    # completed validation
    completed = data.get("completed", False)
    if not isinstance(completed, bool):
        return jsonify({"error": "Completed must be boolean"}), 400

    task = {
        "id": current_id,
        "title": data["title"],
        "description": data.get("description", ""),
        "completed": completed
    }

    tasks.append(task)
    current_id += 1

    return jsonify(task), 201


# PUT update task
@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    if "title" in data:
        if not isinstance(data["title"], str):
            return jsonify({"error": "Invalid title"}), 400
        task["title"] = data["title"]

    if "description" in data:
        task["description"] = data["description"]

    if "completed" in data:
        if not isinstance(data["completed"], bool):
            return jsonify({"error": "Completed must be boolean"}), 400
        task["completed"] = data["completed"]

    return jsonify(task), 200


# DELETE task
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
