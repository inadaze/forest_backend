from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BlockingScheduler
from forest_backend.scheduler.growth import Growth

class ForestScheduler():
    scheduler = None

    def __init__(self):
        executors = {
            'default': ThreadPoolExecutor(1),
            'processpool': ProcessPoolExecutor(5)
        }

        self.scheduler = BlockingScheduler(executors=executors)
        growth = Growth()
        self.scheduler.add_job(func=growth.sprout, trigger="interval", seconds=3)
        self.scheduler.start()