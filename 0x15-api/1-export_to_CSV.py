#!/usr/bin/python3
"""
Module records tasks owned by specific employee
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {user_id} not found.")
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch tasks data
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    # Prepare CSV data
    csv_data = []
    for task in tasks_data:
        csv_data.append([
            user_id,
            username,
            task.get("completed"),
            task.get("title")
        ])

    # Write to CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)

    print(f"Data exported to {csv_filename}")
