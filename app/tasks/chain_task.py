import time
from app import celery
from celery import chain


@celery.task()
def run_chain_tasks():
    chains = chain(
        chain_first_task.s(),
        chain_second_task.s()
    )
    chains.apply_async()


@celery.task()
def chain_first_task():
    time.sleep(5)
    print("### exec \'chain_first_task\' ###")
    chain_id = 12345
    return chain_id


@celery.task()
def chain_second_task(chain_id):
    print("### exec \'chain_second_task\' ###")
    print(chain_id)
