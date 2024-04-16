#!/usr/bin/python3
"""Exports data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":

    URL = "https://jsonplaceholder.typicode.com/"
    EMPLOYEE_ID = sys.argv[1]

    TODOS = requests.get("{}/users/{}/todos".format(URL, EMPLOYEE_ID),
                         params={"_expand": "user"})
    data = TODOS.json()

    filename = '{}.json'.format(EMPLOYEE_ID)

    with open(filename, 'w') as jsonfile:
        for task in data:
            json.dump({EMPLOYEE_ID: [{"task": task.get("title"),
                                      "completed": task.get("completed"),
                                      "username": task.get("user")
                                      .get("username")}]}, jsonfile)
