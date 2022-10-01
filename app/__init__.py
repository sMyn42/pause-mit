import os
from flask import Flask, request, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze')
def analysis():
    return render_template('analysis_page.html')


def main():
    return 1
main()