from app import celery


@celery.task()
def add(a, b):
    return a+b


@celery.task()
def multiple(a, b):
    return a*b
