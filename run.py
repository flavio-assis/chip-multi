from api.app import app
import json
from datetime import datetime
from src.job import job

@app.route('/')
def home():
    return json.dumps({"Message": "Tudo certo por aqui ;)"})

@app.route('/run')
def run_now():
    try:
        job()
        return json.dumps({"Job finished at": f"{datetime.now().strftime('%F %T')}"})

    except Exception as error:
        return json.dumps({"ERROR": f'{error}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port='5000')
