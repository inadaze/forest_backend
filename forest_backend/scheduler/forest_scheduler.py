""" Scheduler to setup backend jobs for updating trees """
import logging
import time
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from forest_backend.logic.growth import Growth

# NOTE: because this is executed as a script all imports must be from forest_backend
# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912
class ForestScheduler():
    """ Creates all necessary jobs to update trees """
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

    def create_logger(self):
        """
        Creates logger for Scheduler
        Writes to scheduler.log
        """
        logger = logging.getLogger('forest_backend_scheduler')
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('scheduler.log')
        file_handler.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    def start_scheduler(self):
        """ Starts the Scheduler process """
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
