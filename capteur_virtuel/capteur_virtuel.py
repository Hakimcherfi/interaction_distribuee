import random
from datetime import datetime
import time
import requests
import os

AGREGAT_API_SERVER = os.environ['AGREGAT_API_SERVER']

def write_data():
        while True:
                data = {"capteur":"virtuel","temperature":"{:.2f}".format(random.random()*30),"time":"{}".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S")),"seconds":"{}".format(time.time())}
                requests.post(AGREGAT_API_SERVER,data = data)
                time.sleep(10)

write_data()

if __name__=='__main__':
        app.run(debug=True,host='0.0.0.0')
