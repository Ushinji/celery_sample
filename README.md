# What is ?
Flask application using a `celery` library.

# Need
* Docker

# Getting started

* Clone a repository
```
$ git clone git@github.com:Ushinji/celery_sample.git
$ cd path/to/repo
```

* Run a bootstrap script

```
$ ./scripts/development/bootstrap.sh

$ docker-compose ps
         Name                       Command               State                 Ports              
---------------------------------------------------------------------------------------------------
celery_sample_app_1      pipenv run start                 Up      0.0.0.0:5000->5000/tcp           
celery_sample_db_1       docker-entrypoint.sh mysqld      Up      0.0.0.0:3316->3306/tcp, 33060/tcp
celery_sample_redis_1    docker-entrypoint.sh redis ...   Up      0.0.0.0:6379->6379/tcp           
celery_sample_worker_1   pipenv run start_worker          Up 
```
