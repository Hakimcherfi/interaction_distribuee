from flask import Flask, jsonify
import random
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime
import time

app = Flask(__name__)

CLIENT = MongoClient("mongodb://agregat:27017")
DB=CLIENT.database

@app.route('/data',methods=["GET"])
def get_data():
        reponse = [{"capteur":"virtuel","temperature":"{:.2f}".format(random.random()*30),"time":"{}".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S")),"seconds":"{}".format(time.time())}]
        return jsonify(reponse)


if __name__=='__main__':
        app.run(debug=True,host='0.0.0.0')