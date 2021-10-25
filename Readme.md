# GooseCity
This is a Django application that runs as the back-end of a database and data management system for the web and React-Bootstrap run the frout-end. 
It aosl can view products and add them to card.

## Style Guide
https://google.github.io/styleguide/jsguide.html

https://google.github.io/styleguide/pyguide.html

## External Requirements
Requires pipenv, React, Django, Node.js.

* [Django](https://www.djangoproject.com/)
* [Node.js](https://nodejs.org/en/)
* [MongoDB](https://www.mongodb.com/)
* [pipenv](https://pypi.org/project/pipenv/)

## Setup
After cloning the repo, run the following commands:

>cd GooseCity <br>
>pipenv shell <br>
>cd backend <br>
>python manage.py makemigrations todo <br>
>python manage.py migrate todo <br>
>cd ../frontend <br>
>npm install <br>

## Running

>pipenv shell <br>
>cd backend <br>
>python manage.py runserver <br>
>cd frontend <br>
>npm start <br>

server runs at http://localhost:8000/ <br>
ui runs at http://localhost:3000/ <br>

## Deployment
Webapps need a deployment section that explains how to get it deployed on the internet. These should be detailed enough so anyone can re-deploy if needed. 
>heroku login<br>
>cd goosecity-main/<br>
>git init<br>
>heroku git:remote -a goosecity<br>
>git add .<br>
>git commit -am "make it better"<br>
>git push heroku master<br>

## Author
Zeliang Zhuo - zzhuo@email.sc.edu <br>
Jiabei He - jiabei@email.sc.edu
Chenhao Cui- cuic@email.sc.edu
