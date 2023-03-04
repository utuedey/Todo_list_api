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
  
| HTTP Method | URl | Action |
| ------- | -------- | ----------- |
| GET |http://[hostname]/todo/api/v1.0/tasks| Retrieve a list of tasks |
| GET | http://[hostname]/todo/api/v1.0/tasks/[task_id] | Retrieve task |
| POST | http://[hostname]/todo/api/v1.0/tasks | Create a new task |
| PUT | http://[hostname]/todo/api/v1.0/tasks/[task_id] | Update an existing task |
| DELETE | http://[hostname]/todo/api/v1.0/tasks/[task_id] | Delete a task |

# Usage
The users of this web service can use the service to add remove and modify tasks.
Using a web browser to test a web service isn't the best idea since web browsers cannot easily generate all types of HTTP requests.instead, use Curl instead:

start the web service by running the command below
```
python app.py
```
Then open a console window and run the following command
```
curl -i http://[localhost]/todo/api/v1.0/task
```
