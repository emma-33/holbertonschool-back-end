#!/usr/bin/python3
"""Exports data in the JSON format for all employees."""
import json
import requests
import sys

if __name__ == "__main__":

    URL = "https://jsonplaceholder.typicode.com/"

    users = requests.get("{}/users".format(URL)).json()

    filename = 'todo_all_employees.json'

    with open(filename, 'w') as jsonfile:
        for user in users:
            TODOS = requests.get("{}/users/{}/todos"
                                 .format(URL, user.get("id")),
                                 params={"_expand": "user"})
            data = TODOS.json()
            for task in data:
                json.dump({task.get("id"): [{"task": task.get("title"),
                                             "completed": task.
                                             get("completed"),
                                             "username": task.get("user")
                                             .get("username")}]}, jsonfile)
