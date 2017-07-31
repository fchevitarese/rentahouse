Rent a house!
===================
To run the project you will need:

- Create a virtualenv
- Rename the .env.initial to .env
- Install dependencies ```pip install -r requirements.txt```
- Run migrations: ```python manage.py migrate```
- Run collectstatic: ```python manage.py collectstatic```
- Run the server: ```python manage.py runserver```
- Open the url of the app: ```http://localhost:8000```
- Register a new account, and insert your property.

----------

I've provided a Dockerfile and a docker-compose file in case you want to try out running it on Docker.

To run a container you will need:

 - Docker
 - docker-compose

I will not provide any info about installing these tools. There are plenty of them over the internet.

To run the container:
------------------------------
- In the project path run the command ```docker-compose build``` to build your container.
- Run ```docker-compose up``` to run the container. If you want it running on background you can run the command ```docker-compose up -d```

Docker-compose will run ```python manage.py migrate``` and ```python manage.py collectstatic --noinput``` commands.

To access the application just open the url: ```http://localhost```
