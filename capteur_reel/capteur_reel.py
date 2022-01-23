import serial
import time
import os
from flask import Flask,jsonify
from datetime import datetime

serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = os.environ['PORT_ARDUINO']


app = Flask(__name__)

@app.route('/data',methods=["GET"])
def get_data():
        serialInst.open()
        packet = serialInst.readline()
        serialInst.close()
        data = packet.decode('utf').strip("\n")
        data = [{"capteur":"arduino","temperature":"{}".format(data),"time":"{}".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S")),"seconds":"{}".format(time.time())}]
        return jsonify(data)

if __name__=='__main__':
        app.run(debug=True,host='0.0.0.0')