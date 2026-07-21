import json
import os

DATA_FILE = "data/database.json"


def save_data(users):
    data = []

    for user in users.values():
        user_data = {
            "name": user.name,
            "email": user.email,
            "projects": []
        }

        for project in user.projects:
            project_data = {
                "title": project.title,
                "description": project.description,
                "due_date": project.due_date,
                "tasks": []
            }

            for task in project.tasks:
                project_data["tasks"].append({
                    "title": task.title,
                    "status": task.status,
                    "assigned_to": task.assigned_to
                })

            user_data["projects"].append(project_data)

        data.append(user_data)

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)