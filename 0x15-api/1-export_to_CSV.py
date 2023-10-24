#!/usr/bin/python3
"""Exports user tasks to a CSV file."""

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

    # Create and open a CSV file for writing
    with open('{}.csv'.format(user_id), 'w') as file:
        for task in tasks:
            # Write each task as a CSV row
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, username, task.get('completed'),
                               task.get('title')))
