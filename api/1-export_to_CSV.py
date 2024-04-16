#!/usr/bin/python3
"""Exports data in the CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":

    URL = "https://jsonplaceholder.typicode.com/"
    EMPLOYEE_ID = sys.argv[1]

    TODOS = requests.get("{}/users/{}/todos".format(URL, EMPLOYEE_ID),
                         params={"_expand": "user"})
    data = TODOS.json()

    EMPLOYEE_NAME = data[0].get("user").get("username")
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    filename = '{}.csv'.format(EMPLOYEE_ID)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for task in data:
            writer.writerows([[EMPLOYEE_ID, EMPLOYEE_NAME,
                               str(task.get("completed")), task.get("title")]])
