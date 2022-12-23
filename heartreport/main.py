from flask import Flask, render_template, request
from flask.helpers import url_for
from ai import Predictor
from config import app
import json
from db import Report

predictor = Predictor('./ai/model')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predict',methods=['POST'])
def predict():
    resd = dict(request.form)
    report = Report(**resd)
    report.save()
    d = json.loads(report.to_json())
    d.pop('_id') 
    print(d)
    pred = predictor.predict(d)

    if pred < 0.2:
        risk = 1
    elif pred >= 0.2 and pred < 0.5:
        risk = 2
    elif pred >= 0.5 and pred < 0.7:
        risk = 3
    else:
        risk = 4

    return render_template('result.html', pred=int(pred*100), risk=risk)

if __name__ == "__main__":
    app.run(debug=True)
