from crypt import methods
from flask import Flask, render_template,jsonify
import time
import requests, os, json

AGREGAT_API_SERVER = os.environ['AGREGAT_API_SERVER']
app = Flask(__name__)

@app.route('/')
def display_data():
    data = requests.get(AGREGAT_API_SERVER+"/").json()
    return render_template('show_data.html', datas=data)

@app.route('/get_data')
def get_data():
    data = requests.get(AGREGAT_API_SERVER+"/").json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')