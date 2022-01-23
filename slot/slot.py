from flask import Flask, render_template
import time
import requests, os, json

CAPTEUR_VIRTUEL_API_SERVER = os.environ['CAPTEUR_VIRTUEL_API_SERVER']
CAPTEUR_REEL_API_SERVER = os.environ['CAPTEUR_REEL_API_SERVER']
app = Flask(__name__)
data = []

@app.route('/')
def show_data():
    response_virtual = requests.get(CAPTEUR_VIRTUEL_API_SERVER+"/data").json()
    response_arduino = requests.get(CAPTEUR_REEL_API_SERVER+"/data").json()
    data.append(response_virtual[0])
    data.append(response_arduino[0])
    return render_template('show_data.html', datas=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')