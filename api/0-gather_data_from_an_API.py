#!/usr/bin/python3
"""Returns information about an employee's TODO list progress."""
import requests
import sys
import json

if __name__ == "__main__":

    URL = "https://jsonplaceholder.typicode.com/"
    EMPLOYEE_ID = sys.argv[1]

    TODOS = requests.get("{}/users/{}/todos".format(URL, EMPLOYEE_ID),
                         params={"_expand": "user"})
    data = TODOS.json()

    EMPLOYEE_NAME = data[0].get("user").get("name")
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    for task in data:
        if task.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for title in TASK_TITLE:
        print("\t {}".format(title))
