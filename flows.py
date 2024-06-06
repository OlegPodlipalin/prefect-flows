from prefect import flow, task, get_run_logger


@flow(log_prints=True, name="hello_world_flow")
def hello_world():
    logger = get_run_logger()
    logger.info("Hello world from logger")
    print("Hello workd from print")
    
    
@task(log_prints=True, name="hello_from_task_1")
def hello_from_task_1(logger):
    logger.info("Task 1 hello from logger")
    print("Task 1 hello from print")


@task(log_prints=True, name="hello_from_task_2")
def hello_from_task_2(logger):
    logger.info("Task 2 hello from logger")
    print("Task 2 hello from print")
    

@flow(log_prints=True, name="hello_from_tasks")
def hello_from_tasks():
    logger = get_run_logger()
    hello_from_task_1(logger)
    hello_from_task_2(logger)

@flow(log_prints=False, name="updated_flow")
def updated_flow():
    logger = get_run_logger()
    logger.info("This is an updated flow from logger")
    print("This is an updated flow from print")