# TODO LIST API

A simple web service for a Todo list application built using flask

 # Root url to access this service
 ```
 http://[hostname]todo/api/v1.0/
 ```

# Introduction
 This is an extremely simple application, we only have tasks,
 so our only resource will be the task in our todo list.

 our tasks resource will use HTTP Methods as follows:
 ________________________________________________________________________________________
 |HTTP Method |              URl                               |       Action    |       |
 |____________|________________________________________________|_________________|_______|
 |GET         |http://[hostname]/todo/api/v1.0/tasks           | Retrieve a list of tasks|
 |____________|________________________________________________|_________________________|
 |GET         |http://[hostname]/todo/api/v1.0/tasks/[task_id] | Retrieve a task         |
 |____________|________________________________________________|_________________________|
 |POST        |http://[hostname]/todo/api/v1.0/tasks           | Create a new task       |
 |____________|________________________________________________|_________________________|
 |PUT         |http://[hostname]/todo/api/v1.0/tasks/[task_id] | Update an existing task |
 |____________|________________________________________________|_________________________|
 |DELETE      |http://[hostname]/todo/api/v1.0/tasks/[task_id] | Delete a task           |
 |____________|________________________________________________|_________________________|
 