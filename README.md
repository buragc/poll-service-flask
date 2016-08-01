[![Build Status](https://travis-ci.org/buragc/poll-service-flask.svg?branch=master)](https://travis-ci.org/buragc/poll-service-flask)
--------------------

# poll-svc
poll-svc is a Python based, RESTFul, microservice back-end that implements polling scenarios backed by a SQLite DB.

## Future
The plan is to add the following functionality to the project to make it fully functional
* Feature: Create a new poll
* Feature: Answer a poll
* Feature: Sweep out polls older than 30 days


## Installation
Installation instructions will go here

## Create DB
To create the database before the first run, we use manage.py
```
python manage.py createdb --drop_first
```

## Running
To run the web server we use manage.py runserver command. 
```
python manage.py runserver
```

### Create a poll
Creating a poll is simple, POST to /polls endpoint with the poll question and up to three poll options
```
curl -X POST -H "Content-Type: application/json" -d "{\"question\": \"here is a sample poll\", \"poll_opt0\":\"First option\", \"poll_opt1\":\"Second option\", \"poll_opt2\":\"Third option\"}" http://127.0.0.1:5000/polls/
```
This request, if successful, will return a JSON object with the id of the newly created poll in the form of 
```
{id: '5b3c1084-e249-4422-8c8e-88bf14c6b4cb'}
```


### Retrieve a poll
Retrieving a poll, send a GET request to the /polls/<id> endpoint where <id> is the unique identifier of the poll
```
curl http://127.0.0.1:5000/polls/5b3c1084-e249-4422-8c8e-88bf14c6b4cb
```