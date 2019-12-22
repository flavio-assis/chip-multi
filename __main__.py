import time
import schedule
from src.job import job
from src.logger import Logger
from src.config import get_config


rt = get_config()['RUNNING_TIME']
logger = Logger()


def main():
    logger.send('Starting Application')
    schedule.every().day.at(rt).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == '__main__':
    main()


