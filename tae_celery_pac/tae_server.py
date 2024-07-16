from celery import Celery
from tae_celery_pac.tasks.taskBasic.cel_main import TaskBasicQueue

app = Celery(
    "main",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@app.task
def add(a,b):
    return a+b

@app.task
def TaskQueue(message):
    return TaskBasicQueue(message)
    #  return "My TaskBasicQueue: {0}".format(message)
    
def main():
    print("making available to celery.... TaskQueue and add")
    app.worker_main(argv = ['worker', '--loglevel=info'])

if __name__ == '__main__':
    main()
    
                        # '--concurrency={}'.format(os.environ['CELERY_CONCURRENCY']), '--without-gossip'])
    