import json
import os
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import simplejson

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQLAlchemy(app)

json_data = []
dat = {}

@app.route('/')
def index():
    return render_template('index.html')

def process_pause_list(in_str):
  s = in_str[3:-2]
  s = s.replace('},{', '}&{').split('&')
  s = [json.loads(i) for i in s]
  return s

@app.route('/analyze', methods=['POST', 'GET'])
def analysis():
    if request.method == 'POST':
        d = process_pause_list(str(request.get_data()))
        dat["POST"] = d
        return render_template('analysis_page.html', output=dat["POST"])
    else:
        return render_template('analysis_page.html', output=dat)

def main():
    return 1
main()