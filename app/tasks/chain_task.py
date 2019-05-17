import time
from app import celery
from celery import chain


@celery.task()
def run_chain_tasks():
    chains = chain(
        chain_first_task.si(),
        chain_second_task.si()
    )
    chains.apply_async()


@celery.task()
def chain_first_task():
    time.sleep(5)
    print("### exec \'chain_first_task\' ###")


@celery.task()
def chain_second_task():
    print("### exec \'chain_second_task\' ###")
