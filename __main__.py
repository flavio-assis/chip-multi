import time
import schedule
from src import job


def main():
    schedule.every().day.at("18:30").do(job)

    while 1:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()

