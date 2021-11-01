# Django-docker-postgres-gunicorn-nginx
## Description
![django](https://img.shields.io/badge/Made%20With-Django-green?style=for-the-badge&logo=django)  ![pgsql](https://img.shields.io/badge/Database-PostgreSQL-blue?style=for-the-badge&logo=postgresql)

The Project is all about deployment of Django based basic web-app using Docker, Gunicorn and Nginx.
By default Django uses dbsqlite3 in this project we are using postgresql.
Gunicorn works and provide our Django site through wsgi. 
Nginx serves our static files.

## Installation
![docker](https://img.shields.io/badge/Containerized%20With-Docker-blue?style=for-the-badge&logo=docker)


First Install docker for your Machine.
[With the help of Docker documentation](https://docs.docker.com/engine/install/)

## To run:
```bash
 docker-compose up -d
```
After making any changes make sure to build it once again
```bash
 docker-compose build
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
