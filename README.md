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

## Installation

git clone the repository
```
git clone https://github.com/utuedey/Todo_list_api.git
```
 change directory
 ```
 cd Todo_list_api
 ```
 Create a virtual env
 ```
 python3 -m venv environment_name
 ```
 activate the environment
 ```
 source environment_name/Scripts/activate
 ````
start the app using the command below
```
python app.py
```
You can now successfully use the web service

# Credits 
- [Miguel Grinberg ] <https://blog.miguelgrinberg.com/index>

# Author
- [Joseph Utuedeye] <https://twitter.com/joecodes2>