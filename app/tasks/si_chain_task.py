import time
from app import celery
from celery import chain


@celery.task()
def run_si_chain_tasks():
    chains = chain(
        si_chain_first_task.si(),
        si_chain_second_task.si()
    )
    chains.apply_async()


@celery.task()
def si_chain_first_task():
    time.sleep(5)
    print("### exec \'si_chain_first_task\' ###")


@celery.task()
def si_chain_second_task():
    print("### exec \'si_chain_second_task\' ###")
