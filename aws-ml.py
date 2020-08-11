from flask import Flask, request, jsonify
import numpy as np
import joblib
import json

pkl_file = 'iris-trained-model.pkl'
custom_port = "5000"

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome Ml Prediction, call /predict/"

@app.route('/predict/', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)

if __name__ == '__main__':
    model = joblib.load(pkl_file)
    app.run(host='0.0.0.0', port=custom_port)