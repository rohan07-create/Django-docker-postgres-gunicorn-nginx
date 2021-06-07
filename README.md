# Django-docker-postgres-gunicorn-nginx
## Description
The Project is all about deployment of Django based basic web-app using Docker, Gunicorn and Nginx.
By default Django uses dbsqlite3 in this project we are using postgresql.
Gunicorn works and provide our Django site through wsgi. 
Nginx serves our static files.

## Installation
First Install docker for your Machine
[With the help of Docker documentation](https://docs.docker.com/engine/install/)

## To run:
```bash
 docker-compose up -d
```

## To stop:
```bash
 docker-compose down
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author
[Rohan Chourasiya](https://github.com/rohan07-create)
