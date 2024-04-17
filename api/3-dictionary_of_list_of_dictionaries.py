#!/usr/bin/python3
"""Exports data in the JSON format for all employees."""
import json
import requests

if __name__ == "__main__":

    URL = "https://jsonplaceholder.typicode.com/"

    users = requests.get("{}/users".format(URL)).json()

    filename = 'todo_all_employees.json'

    users_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        data = requests.get("{}/users/{}/todos".format(URL, user_id),
                            params={"_expand": "user"}).json()

        tasks = []
        for task in data:
            tasks.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
                })
        users_tasks[user_id] = tasks

    with open(filename, 'w') as jsonfile:
        json.dump(users_tasks, jsonfile)
