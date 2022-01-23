import serial
import time
import os
from flask import Flask,jsonify
from datetime import datetime
import csv
import requests

serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = os.environ['PORT_ARDUINO']
app = Flask(__name__)

AGREGAT_API_SERVER = os.environ['AGREGAT_API_SERVER']

def write_data():
        while True:
                serialInst.open()
                packet = serialInst.readline()
                serialInst.close()
                data = packet.decode('utf').strip("\n")
                data = {"capteur":"arduino","temperature":"{}".format(data).strip('\r'),"time":"{}".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S")),"seconds":"{}".format(time.time())}
                requests.post(AGREGAT_API_SERVER,data = data)
                time.sleep(10)

write_data()

if __name__=='__main__':
        app.run(debug=True,host='0.0.0.0')