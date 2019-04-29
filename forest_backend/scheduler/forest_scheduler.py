from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from forest_backend.logic.growth import Growth
import logging
import time

class ForestScheduler():
    scheduler = None

    def __init__(self):
        self.create_logger()
        executors = {
            'default': ThreadPoolExecutor(2),
            'processpool': ProcessPoolExecutor(5)
        }

        self.scheduler = BackgroundScheduler(executors=executors)
        growth = Growth()
        self.scheduler.add_job(func=growth.germinate, trigger="interval", minutes=2)
        self.scheduler.add_job(func=growth.sprout, trigger="interval", minutes=2)
        #self.scheduler.start()

    def create_logger(self):
        # create logger with 'spam_application'
        logger = logging.getLogger('forest_backend_scheduler')
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('scheduler.log')
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)

    def start_scheduler(self):
        self.scheduler.start()

if __name__ == '__main__':
    FOREST_SCHEDULER = ForestScheduler()
    FOREST_SCHEDULER.start_scheduler()

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        FOREST_SCHEDULER.scheduler.shutdown()