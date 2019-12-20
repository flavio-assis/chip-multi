import time
import schedule
from src import job
from flask import Flask
import json


app = Flask(__name__)

@app.route('/')
def check_life():
    return json.dumps({"Message": "Great! I'm up!"})


def main():
    schedule.every().day.at("18:30").do(job)
    app.run(host='0.0.0.0',
            port=5000)

    while 1:
        schedule.run_pending()
        time.sleep(1)



if __name__ == '__main__':
    main()


