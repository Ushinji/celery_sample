import time
from app import celery
from celery import chain, group


@celery.task()
def run_group_tasks():
    object_ids = [1, 3, 5]
    groups = group(
        chain(
            first_task.si(object_id),
            second_task.si(object_id)
        ) for object_id in object_ids
    )
    groups.apply_async()


@celery.task()
def first_task(object_id):
    time.sleep(5)
    print(f"### exec \'first_task\'. object_id: \'{object_id}\' ###")


@celery.task()
def second_task(object_id):
    print(f"### exec \'second_task\'. object_id: \'{object_id}\' ###")
