#!/usr/bin/python3

import json
import requests

def fetch_data():
    # Fetch user data
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users_response.json()

    # Fetch tasks data
    tasks_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = tasks_response.json()

    # Organize data into the required format
    data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [task for task in tasks if task['userId'] == user_id]
        data[user_id] = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in user_tasks
        ]

    return data

def export_to_json(data, filename="todo_all_employees.json"):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    data = fetch_data()
    export_to_json(data)
