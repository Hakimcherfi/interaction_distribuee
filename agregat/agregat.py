from flask import Flask, jsonify,request
import time
import requests, os, json
import csv

app = Flask(__name__)
data = []

@app.route('/',methods=["GET"])
def return_data():
    return jsonify(data)

@app.route('/',methods=["POST"])
def write_data():
    data.append({'capteur':request.form.get("capteur"),'temperature':request.form.get("temperature"),'time':request.form.get("time"),'seconds':request.form.get("seconds")})
    return '''<h1>Donnée prise en compte : {}</h1>'''.format(request.form.get("data"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')