<h1>Courses API</h1>

<h3>Setup:</h3>

$ git clone https://github.com/monkdok/courses_api.git

$ cd courses_api

Create a virtual environment to install dependencies in and activate it:

$ virtualenv venv

$ source venv/bin/activate

Then install the dependencies:

(env)$ pip install -r requirements.txt


Environment:

(env)$ mkdir .env && cd .env && echo .env

env_example located in the root of project. Just change the values of the variables to your own.
Then go back to the root directory.

Migrate tables to db:
(env)$ ./manage.py makemigrations courses users
(env)$ ./manage.py migrate

Create initial data:
(env)$ python manage.py loaddata courses/fixtures/*
(env)$ python manage.py loaddata users

(env)$ ./manage.py makemigrations courses users
(env)$ ./manage.py migrate


Run local server:

(env)$ python manage.py runserver

Navigate to http://127.0.0.1:8000/courses/.


Running the tests:

(env)$ ./manage.py test


admin credentials:
emali: admin@gmail.com
pass: admin