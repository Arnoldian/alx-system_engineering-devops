#!/usr/bin/python3

import json
import requests
import sys

def export_to_json(user_id):
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com/'
    
    # Fetch user information
    user_response = requests.get(f'{base_url}users/{user_id}')
    user = user_response.json()
    
    # Fetch tasks for the user
    tasks_response = requests.get(f'{base_url}todos', params={'userId': user_id})
    tasks = tasks_response.json()
    
    # Prepare data to be exported
    user_tasks = []
    for task in tasks:
        user_tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user['username']
        })
    
    # Create the final dictionary
    data = {str(user_id): user_tasks}
    
    # Write data to JSON file
    with open(f'{user_id}.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <USER_ID>")
    else:
        try:
            user_id = int(sys.argv[1])
            export_to_json(user_id)
        except ValueError:
            print("USER_ID must be an integer")
