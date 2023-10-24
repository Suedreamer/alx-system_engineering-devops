#!/usr/bin/python3
"""Exports user tasks to JSON format."""

from json import dump
from requests import get
from sys import argv

if __name__ == '__main__':
    # Get user ID from command-line argument
    user_id = argv[1]

    # Fetch the user's username from the API
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(user_url)
    username = response.json().get('username')

    # Fetch the user's tasks from the API
    tasks_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(tasks_url)
    tasks = response.json()

    # Create a dictionary to store user tasks
    user_tasks = {user_id: []}

    # Iterate through the tasks and add them to the dictionary
    for task in tasks:
        user_tasks[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    # Create and open a JSON file for writing
    with open('{}.json'.format(user_id), 'w') as file:
        # Write the user tasks to the JSON file
        dump(user_tasks, file)
